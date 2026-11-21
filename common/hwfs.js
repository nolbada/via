/* hwfs 261121a - 숙제 REC 저장소. 구글 Apps Script 를 거치지 않고 Firebase(Firestore)에 직접 읽고 쓴다.
   선생님: 구글 로그인(허용 계정만). 학부모: 로그인 없이 자기 링크 문서 1개만 읽는다.
   hw_c/main   반 명단·항목 설정   {roster, cfg (JSON 문자열), tr, tc (저장 시각)}
   hw_w/<주>    그 주 전체 학생 검사 기록 {r:{학생번호:JSON}, t:{학생번호:시각}}  (주 = 그 주 토요일 날짜)
   hw_p/<토큰>  학부모 화면용 {meta, mt, w:{주:JSON}, wt:{주:시각}, cc:{주:JSON}, ct:{주:시각}}
   화면 쪽 코드는 예전 기록 서버와 같은 모양({키:{v:{s:JSON문자열},t:시각}})으로 받으므로 거의 그대로 쓴다. */
(function () {
  var W = window;
  var CFG = { apiKey: "AIzaSyC88G-OjMJOqVqnIVqunzh7fvk91wtKKnA", authDomain: "nolbada.github.io", projectId: "h-roadmap", appId: "1:575520405083:web:b9f40b64cb0ae3d1a9317e" };
  var OK = ["nolbada727@gmail.com", "ysbada@gmail.com"];
  var DOCS = "https://firestore.googleapis.com/v1/projects/" + CFG.projectId + "/databases/(default)/documents/";
  var V = "https://www.gstatic.com/firebasejs/10.14.1/";
  var OLDER = 6; /* 이번 주·지난주 말고 처음 열 때 한 번 더 읽는 지난 주 수 */

  function tmo(p, ms) {
    return new Promise(function (res, rej) {
      var t = setTimeout(function () { rej(new Error("timeout")); }, ms);
      p.then(function (x) { clearTimeout(t); res(x); }, function (e) { clearTimeout(t); rej(e); });
    });
  }
  function isT(u) { return !!(u && u.email && u.emailVerified !== false && OK.indexOf(String(u.email).toLowerCase()) >= 0); }

  /* ---------- 학부모(로그인 없음): 문서 1개 ---------- */
  function readP(tok) {
    var ac = W.AbortController ? new AbortController() : null;
    var tm = ac ? setTimeout(function () { ac.abort(); }, 12000) : 0;
    return fetch(DOCS + "hw_p/" + encodeURIComponent(tok) + "?key=" + CFG.apiKey, { signal: ac ? ac.signal : undefined })
      .then(function (r) {
        clearTimeout(tm);
        if (r.status === 404) return {};
        if (!r.ok) throw new Error("fs" + r.status);
        return r.json();
      })
      .then(function (doc) {
        var f = doc.fields || {}, d = {};
        function s(x) { return x && x.stringValue != null ? x.stringValue : null; }
        function i(x) { return x && x.integerValue != null ? Number(x.integerValue) : 0; }
        function m(x) { return (x && x.mapValue && x.mapValue.fields) || {}; }
        if (s(f.meta) != null) d.meta = { v: { s: s(f.meta) }, t: i(f.mt) };
        ["w", "cc"].forEach(function (p) {
          var a = m(f[p]), tt = m(f[p === "w" ? "wt" : "ct"]);
          for (var k in a) { var v = s(a[k]); if (v != null) d[p + ":" + k] = { v: { s: v }, t: i(tt[k]) }; }
        });
        return d;
      });
  }

  /* ---------- 선생님(로그인): SDK ---------- */
  var P = null;
  function sdk() {
    if (P) return P;
    P = (async function () {
      var a = await import(V + "firebase-app.js");
      var u = await import(V + "firebase-auth.js");
      var f = await import(V + "firebase-firestore.js");
      var app = a.initializeApp(CFG, "hwfs");
      var auth = u.getAuth(app), db = f.getFirestore(app);
      await new Promise(function (res) { var off = u.onAuthStateChanged(auth, function () { off(); res(); }); });
      return { u: u, f: f, auth: auth, db: db };
    })();
    P.catch(function () { P = null; });
    return P;
  }

  var ST = null; /* 선생님 화면의 메모리 보관소: 지켜보는 문서가 바뀔 때만 갱신되고, 읽기 요청은 여기서 답한다 */
  var LOADED = {};

  function addWeek(out, wk, x) {
    var r = (x && x.r) || {}, t = (x && x.t) || {};
    for (var sid in r) out["w:" + sid + ":" + wk] = { v: { s: r[sid] }, t: Number(t[sid] || 0) };
    LOADED[wk] = 1;
  }
  function compose() {
    var out = {}, c = ST.c;
    if (c) {
      if (c.roster != null) out.roster = { v: { s: c.roster }, t: c.tr || 0 };
      if (c.cfg != null) out.cfg = { v: { s: c.cfg }, t: c.tc || 0 };
    }
    for (var wk in ST.w) addWeek(out, wk, ST.w[wk]);
    return out;
  }
  function fire() {
    clearTimeout(ST.tm);
    ST.tm = setTimeout(function () { ST.cbs.forEach(function (cb) { try { cb(); } catch (e) {} }); }, 400);
  }
  /* cur, prev: 이번 주·지난 주 키. 이 둘과 명단 문서를 지켜보고, 더 지난 주는 한 번만 읽어 메모리에 둔다 */
  function start(cur, prev) {
    if (ST) return ST.ready;
    ST = { c: null, w: {}, cbs: [], subs: [], ok: false, tm: 0, seen: 0 };
    ST.ready = sdk().then(function (s) {
      var f = s.f, db = s.db;
      return new Promise(function (resolve, reject) {
        var need = 3, done = false;
        function got() { if (++ST.seen === need && !done) { done = true; ST.ok = true; resolve(); } }
        function bad(e) { ST.ok = false; if (!done) { done = true; reject(e); } }
        var seen = {};
        function listen(ref, key, apply) {
          ST.subs.push(f.onSnapshot(ref, function (snap) {
            apply(snap.exists() ? snap.data() : null);
            var first = !seen[key]; seen[key] = 1;
            if (first) got();
            else if (!snap.metadata.hasPendingWrites) fire();
          }, bad));
        }
        listen(f.doc(db, "hw_c", "main"), "c", function (x) { ST.c = x; });
        listen(f.doc(db, "hw_w", cur), "w" + cur, function (x) { if (x) ST.w[cur] = x; else delete ST.w[cur]; });
        listen(f.doc(db, "hw_w", prev), "w" + prev, function (x) { if (x) ST.w[prev] = x; else delete ST.w[prev]; });
      }).then(function () {
        var lo = new Date(prev + "T00:00:00Z"); lo.setUTCDate(lo.getUTCDate() - 7 * OLDER);
        var lok = lo.toISOString().slice(0, 10);
        return f.getDocs(f.query(f.collection(db, "hw_w"), f.where(f.documentId(), ">=", lok), f.where(f.documentId(), "<", prev)))
          .then(function (q) { q.forEach(function (d) { ST.w[d.id] = d.data(); LOADED[d.id] = 1; }); });
      });
    });
    ST.ready.catch(function () { ST = null; });
    return ST.ready;
  }

  var H = W.HWFS = {
    loaded: LOADED,
    /* null: 로그인 안 됨 / {email, ok:false}: 허용 안 된 계정 / {email, ok:true} */
    user: function () {
      return sdk().then(function (s) { var u = s.auth.currentUser; return u ? { email: u.email, ok: isT(u) } : null; });
    },
    signIn: function () {
      return sdk().then(function (s) {
        var u = s.u, p = new u.GoogleAuthProvider();
        p.setCustomParameters({ prompt: "select_account" });
        return u.signInWithPopup(s.auth, p).catch(function (e) {
          var c = (e && e.code) || "";
          if (c === "auth/popup-blocked" || c === "auth/operation-not-supported-in-this-environment" || c === "auth/web-storage-unsupported") return u.signInWithRedirect(s.auth, p);
          throw e;
        });
      });
    },
    signOut: function () { return sdk().then(function (s) { return s.u.signOut(s.auth); }); },
    setWeeks: function (cur, prev) { H._cur = cur; H._prev = prev; },
    /* 선생님 화면이 열릴 때: 명단·설정·최근 8주를 한 묶음으로 */
    readT: function () {
      return start(H._cur, H._prev).then(compose);
    },
    /* 더 오래된 주가 필요할 때 그 주만 한 번 읽는다 */
    readWeek: function (wk) {
      if (LOADED[wk]) return Promise.resolve({});
      return sdk().then(function (s) {
        return s.f.getDoc(s.f.doc(s.db, "hw_w", wk)).then(function (d) {
          var out = {};
          if (d.exists()) { ST && (ST.w[wk] = d.data()); addWeek(out, wk, d.data()); } else LOADED[wk] = 1;
          return out;
        });
      });
    },
    live: function () { return !!(ST && ST.ok); },
    watchT: function (cb) { start(H._cur, H._prev).then(function () { ST.cbs.push(cb); }, function () {}); },
    /* 선생님 저장: 한 요청으로 원자적으로. map = {roster|cfg|'w:학생번호:주': 값(객체)} */
    writeT: function (map) {
      return sdk().then(function (s) {
        var f = s.f, db = s.db, b = f.writeBatch(db), now = Date.now(), cd = {}, wk = {}, has = false, n = 0, k, w;
        for (k in map) {
          if (k === "roster") { cd.roster = JSON.stringify(map[k]); cd.tr = now; has = true; }
          else if (k === "cfg") { cd.cfg = JSON.stringify(map[k]); cd.tc = now; has = true; }
          else if (k.indexOf("w:") === 0) {
            var p = k.split(":"), sid = p[1]; w = p[2];
            wk[w] = wk[w] || { r: {}, t: {} };
            wk[w].r[sid] = JSON.stringify(map[k]); wk[w].t[sid] = now;
          }
        }
        if (has) { b.set(f.doc(db, "hw_c", "main"), cd, { merge: true }); n++; }
        for (w in wk) { b.set(f.doc(db, "hw_w", w), wk[w], { merge: true }); n++; }
        if (!n) return null;
        return tmo(b.commit(), 15000);
      });
    },
    readP: readP,
    /* 학부모 화면용 문서 쓰기(선생님·리포트). entries = [[토큰, {meta|'w:주'|'cc:주': 값(객체)}], ...] 최대 400개씩 한 요청 */
    writeManyP: function (entries) {
      return sdk().then(function (s) {
        var f = s.f, db = s.db, now = Date.now(), jobs = [];
        for (var i = 0; i < entries.length; i += 400) {
          (function (part) {
            var b = f.writeBatch(db);
            part.forEach(function (e) {
              var tok = e[0], map = e[1], d = {}, k;
              for (k in map) {
                var str = JSON.stringify(map[k]);
                if (k === "meta") { d.meta = str; d.mt = now; }
                else if (k.indexOf("w:") === 0) { d.w = d.w || {}; d.wt = d.wt || {}; d.w[k.slice(2)] = str; d.wt[k.slice(2)] = now; }
                else if (k.indexOf("cc:") === 0) { d.cc = d.cc || {}; d.ct = d.ct || {}; d.cc[k.slice(3)] = str; d.ct[k.slice(3)] = now; }
              }
              b.set(f.doc(db, "hw_p", tok), d, { merge: true });
            });
            jobs.push(tmo(b.commit(), 20000));
          })(entries.slice(i, i + 400));
        }
        return Promise.all(jobs);
      });
    },
    writeP: function (tok, map) { return H.writeManyP([[tok, map]]); }
  };
})();
