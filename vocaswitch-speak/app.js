(function(){
  var $ = function(id){ return document.getElementById(id); };
  var Q = new URLSearchParams(location.search);
  var NQ    = parseInt(Q.get('n'))     || 7;    // 뽑는 문장 수
  var TH    = parseInt(Q.get('th'))    || 65;   // 통과 기준(%)
  var PEN   = parseInt(Q.get('pen'))   || 3;    // 이 개수 이상 틀리면 벌칙
  var TIME  = Q.has('time') ? parseInt(Q.get('time')) : -1; // 제한시간(초), 0이면 없음, 안 쓰면 문장 길이에 맞춰 자동
  function limitSec(){ if (TIME >= 0) return TIME; var n = cur ? cur.ko.replace(/\([^)]*\)/g,'').replace(/\s/g,'').length : 20; return Math.min(75, Math.max(25, 15 + Math.round(n * 1.1))); }
  var RETRY = Q.has('retry') ? parseInt(Q.get('retry')) : 1; // 문장당 다시 말하기 횟수
  var TEACHER = Q.get('t') === '1';
  var BOOKS = window.BOOKS || {};
  var PKEY = window.APPKEY || 'vs_oral_v1';

  $('rule').innerHTML = NQ + '문장이 랜덤으로 나옵니다. 영어 문장을 보고 한국어 해석을 말하세요.' + '<br>통과컷 ' + (PEN-1) + '개 (틀린 문장 ' + (PEN-1) + '개까지 통과)' + '<br>통과하지 못하면 오늘의 ' + NQ + '문장을 책의 같은 번호 옆에 다시 씁니다.';

  // 저장된 프로필
  function setBook(b){
    $('book').value = b || '';
    document.querySelectorAll('.bk').forEach(function(x){ x.classList.toggle('on', x.dataset.b === b); });
    var n = (BOOKS[b] || []).length;
    $('bkinfo').textContent = b ? b : 'UNIT을 선택하세요';
    $('err').textContent = '';
  }
  document.querySelectorAll('.bk').forEach(function(x){ x.onclick = function(){ setBook(x.dataset.b); }; });
  try { var p = JSON.parse(localStorage.getItem(PKEY) || '{}'); if (p.name) $('name').value = p.name; if (p.book) setBook(p.book); } catch(e){}

  var attemptLog = [], picks = [], idx = -1, cur = null, results = [], tries = 0, graded = false, timerId = null, left = 0;
  var prof = {};

  function show(id){ ['sStart','sTest','sEnd'].forEach(function(s){ $(s).classList.toggle('on', s === id); }); window.scrollTo(0,0); }
  function esc(s){ return String(s).replace(/[&<>]/g, function(c){ return {'&':'&amp;','<':'&lt;','>':'&gt;'}[c]; }); }
  function shuffle(a){ a = a.slice(); for (var i=a.length-1;i>0;i--){ var j=Math.floor(Math.random()*(i+1)); var t=a[i]; a[i]=a[j]; a[j]=t; } return a; }
  function stamp(){
    var d = new Date(), w = ['일','월','화','수','목','금','토'][d.getDay()];
    var hh = ('0'+d.getHours()).slice(-2), mm = ('0'+d.getMinutes()).slice(-2);
    return (d.getMonth()+1) + '/' + d.getDate() + '(' + w + ') ' + hh + ':' + mm;
  }

  // 소리
  var AC = window.AudioContext || window.webkitAudioContext, ac = null;
  var SOUND = Q.get('sound') === '1';   // 기본은 소리 없음 (민망하지 않게). 링크 끝에 ?sound=1 을 붙이면 딩동/땡 소리가 나옴
  function tone(freq, start, dur, type){
    if (!SOUND || !AC) return; if (!ac) ac = new AC();
    var o = ac.createOscillator(), g = ac.createGain();
    o.type = type || 'sine'; o.frequency.value = freq; o.connect(g); g.connect(ac.destination);
    var t = ac.currentTime + start; g.gain.setValueAtTime(0.25, t); g.gain.exponentialRampToValueAtTime(0.001, t + dur);
    o.start(t); o.stop(t + dur);
  }
  function dingdong(){ tone(880,0,.35); tone(660,.3,.6); }
  function ddang(){ tone(150,0,.5,'sawtooth'); tone(120,.15,.6,'sawtooth'); }

  // 시작
  $('startBtn').onclick = function(){
    var name = $('name').value.trim(), book = $('book').value, f = 1, t = 1;
    var arr = BOOKS[book], err = $('err'); f = 1; t = arr ? arr.length : 0;
    if (!name){ err.textContent = '이름을 입력하세요.'; return; }
    if (!book){ err.textContent = 'UNIT을 눌러 선택하세요.'; return; }
    if (!arr){ err.textContent = '문장 데이터를 불러오지 못했어요. 새로고침 해 보세요.'; return; }
    if (!f || !t || f > t){ err.textContent = '번호 범위를 정확히 입력하세요. (예: 221 ~ 230)'; return; }
    if (f < 1 || t > arr.length){ err.textContent = book + '은 1~' + arr.length + '번까지 있어요.'; return; }
    if (t - f + 1 < NQ){ err.textContent = '범위에 문장이 ' + NQ + '개는 있어야 해요.'; return; }
    if (t - f + 1 > 60){ err.textContent = '범위가 너무 넓어요. 60문장 이내로 입력하세요.'; return; }
    err.textContent = '';
    prof = { name: name, book: book, from: f, to: t };
    try { localStorage.setItem(PKEY, JSON.stringify(prof)); } catch(e){}
    var nums = []; for (var i=f;i<=t;i++) if (arr[i-1]) nums.push(i);
    picks = shuffle(nums).slice(0, NQ).map(function(n){ return { n:n, en:arr[n-1][0], ko:arr[n-1][1] }; });
    idx = -1; cur = null; results = [];
    $('card').className = 'card spin'; $('card').textContent = '룰렛 돌리기를 누르세요';
    $('result').className = 'result'; $('heard').textContent = '-'; $('timer').textContent = '';
    $('spinBtn').style.display = 'none';
    $('micBtn').disabled = true; $('nextBtn').style.display = 'none'; $('retryBtn').style.display = 'none';
    $('prog').textContent = '0 / ' + NQ + ' 문장 · ' + book;
    show('sTest');
    showNext();
  };

  // 다음 문장을 바로 보여 준다 (돌아가는 연출 없음)
  function showNext(){
    if (idx + 1 >= picks.length) return;
    $('micBtn').disabled = true;
    $('result').className = 'result'; $('result').innerHTML = ''; $('heard').textContent = '-';    idx++; cur = picks[idx]; tries = 0; graded = false; attemptLog = [];
    var c = $('card'); c.className = 'card'; c.textContent = cur.en;
    $('prog').textContent = (idx+1) + ' / ' + NQ + ' 문장 · ' + prof.book;
    $('spinBtn').style.display = 'none';
    beginAttempt();
  }
  $('spinBtn').onclick = showNext;

  function beginAttempt(){
    attemptNo++; graded = false; $('micBtn').disabled = false; $('heard').textContent = '-';
    $('retryBtn').style.display = 'none';
    $('result').className = 'result'; $('result').innerHTML = '';
    lastHeard = ''; baseText = ''; finalText = ''; alts = [];
    var LIM = limitSec();
    if (LIM){
      left = LIM; $('timer').className = 'timer'; $('timer').textContent = left + '초';
      clearInterval(timerId);
      timerId = setInterval(function(){
        left--; $('timer').textContent = left > 0 ? left + '초' : '시간 끝';
        if (left <= 5) $('timer').className = 'timer low';
        if (left <= 0){ clearInterval(timerId); onTimeUp(); }
      }, 1000);
    }
  }
  function stopTimer(){ clearInterval(timerId); }
  var attemptNo = 0;
  function onTimeUp(){
    if (graded) return;
    var my = attemptNo;
    wantStop = true; if (listening && rec){ try { rec.stop(); } catch(e){} setTimeout(function(){ if (!graded && my === attemptNo) finishAttempt(false, 0, lastHeard); }, 600); }
    else finishAttempt(false, 0, lastHeard);
  }

  // 판정: 정답 해석의 '낱말'이 말한 내용에 들어 있는지를 본다 (어순·어미가 달라도 괜찮게)
  //  - 낱말의 앞 2글자가 들어 있으면 거의 맞은 것으로 치고, 같은 뜻의 흔한 말(세일=할인 등)도 인정
  var SYN = [['세일','할인'],['아끼','절약'],['아껴','절약'],['레시피','조리법'],['시속','시간당'],['상품','물품'],['제품','물품'],
             ['개학','등교'],['탁자','테이블'],['엄마','어머니'],['아빠','아버지'],['안으로','실내'],['담을','추가'],['담아','추가'],
             ['고르','선택'],['빨리','신속'],['즉시','곧'],['바로','즉시'],['직장','일하는'],['근무','일하는'],['정원','마당'],['뜰','마당'],['라커','사물함'],['로커','사물함'],['락커','사물함'],['어떠한','어떤'],['어떤','어떠한'],['남기','남겨'],['남겨','남기'],['안된다','말아야'],['안돼','말아야'],['안됩니','말아야'],['하지마','말아야'],['않아야','말아야'],['안된다','않아야'],['휴대폰','핸드폰'],['휴대전화','핸드폰'],['스마트폰','핸드폰'],['핸드폰','휴대전화'],['휴대폰','휴대전화'],['스마트폰','휴대전화'],['멀어','걸어갔'],['떨어','걸어갔'],['떠나','걸어갔'],['떠났','걸어갔'],['뜻입니','뜻인가'],['뜻인가','뜻입니'],['베프','친한'],['베프','친구'],['베프','가장'],['단짝','친한'],['단짝','친구'],['단짝','가장']];
  var STOPCH = '이가은는을를에의도로와과만께';
  function norm(s){ return String(s).toLowerCase().replace(/[^가-힣a-z0-9]/g,''); }
  function scoreDetail(spoken, answer){
    answer = String(answer).replace(/\([^)]*\)/g, ' ');
    var sp = norm(spoken), miss = [];
    var words = answer.split(/\s+/).map(function(w){ return w.replace(/[^가-힣0-9]/g,''); }).filter(function(w){ return w.length >= 2; });
    var FUNC=['당신','너의','그의','그들','자신','우리','나는','있다','있는','있기','있어','있지','있었','때문','위해','위한','것이','것을','것은','합니','않아','않다','않는','않았','주세','이다','한다','된다','하고','해야','하는','그리','그러','것이다'];
    var cw = words.filter(function(w){ return !FUNC.some(function(f){ return w.indexOf(f)===0; }); });
    if (cw.length) words = cw;
    if (!sp) return { pct: 0, miss: words };
    if (!words.length){ var a = norm(answer); return { pct: (a && sp.indexOf(a) >= 0) ? 100 : 0, miss: [] }; }
    var tot = 0, got = 0;
    words.forEach(function(w){
      var wt = w.length; tot += wt;
      var p2 = w.slice(0,2), hit = 0;
      if (sp.indexOf(w) >= 0) hit = 1;
      else if (sp.indexOf(p2) >= 0) hit = 0.9;
      else {
        for (var i=0;i<SYN.length;i++){
          if (w.indexOf(SYN[i][1]) === 0 && sp.indexOf(SYN[i][0]) >= 0){ hit = 0.8; break; }
          if (w.indexOf(SYN[i][0]) === 0 && sp.indexOf(SYN[i][1]) >= 0){ hit = 0.8; break; }
        }
        if (!hit && w.length >= 3 && STOPCH.indexOf(w[0]) < 0 && sp.indexOf(w[0]) >= 0) hit = 0.3;
      }
      if (hit < 0.8) miss.push(w);
      got += wt * hit;
    });
    return { pct: Math.round(got / tot * 100), miss: miss };
  }
  function score(spoken, answer){ return scoreDetail(spoken, answer).pct; }

  var lastHeard = '';
  function cmpBox(spoken, sc, showAns){
    var h = '<div class="cmp"><div><b>내가 말한 것</b> ' + (spoken ? esc(spoken) : '(직접 확인)') + '</div>';
    if (showAns) h += '<div><b>정답 해석 · ' + cur.n + '번</b>' + esc(cur.ko) + '</div>';
    if (spoken){ var d = scoreDetail(spoken, cur.ko); if (d.miss.length && showAns) h += '<div><b>못 알아들은 말</b> ' + esc(d.miss.join(', ')) + '</div>'; }
    if (sc != null && sc >= 0) h += '<div class="pct">일치 ' + sc + '% (기준 ' + TH + '%)</div>';
    return h + '</div>';
  }
  // 마지막 시도가 아닐 때는 정답·일치율·못 알아들은 말을 절대 보여주지 않는다 (내가 말한 것만)
  function spokenOnly(spoken){ return '<div class="cmp"><div><b>내가 말한 것</b> ' + (spoken ? esc(spoken) : '(인식된 말 없음)') + '</div></div>'; }
  function finishAttempt(pass, sc, spoken){
    if (graded) return; graded = true; stopTimer(); attemptLog.push({ t: spoken || '', sc: sc }); $('micBtn').disabled = true; $('timer').textContent = '';
    var r = $('result');
    if (pass){
      r.className = 'result ok'; r.innerHTML = '딩동! 맞았어요' + cmpBox(spoken, sc, true); dingdong();
      record(true);
    } else if (tries < RETRY){
      tries++;
      r.className = 'result no'; r.innerHTML = '땡! 한 번 더 말해 봐요<div class="ans">(남은 기회 ' + (RETRY - tries + 1) + '번)</div>' + spokenOnly(spoken); ddang();
      $('retryBtn').style.display = '';
      return;
    } else {
      r.className = 'result no'; r.innerHTML = '땡! 틀렸어요' + cmpBox(spoken, sc, true); ddang();
      record(false);
    }
  }
  function record(ok){
    results[idx] = { n:cur.n, en:cur.en, ko:cur.ko, ok:ok, log: attemptLog.slice() };
    $('retryBtn').style.display = 'none';
    $('nextBtn').style.display = '';
    $('nextBtn').textContent = (idx + 1 >= picks.length) ? '결과 보기' : '다음 문장';
  }
  $('retryBtn').onclick = function(){ beginAttempt(); };

  $('nextBtn').onclick = function(){
    $('nextBtn').style.display = 'none';    if (idx + 1 >= picks.length){ finish(); return; }
    showNext();
  };

  function finish(){
    var wrong = results.filter(function(r){ return !r.ok; }).length;
    var f = $('final');
    if (wrong >= PEN){ f.className = 'final bad'; f.innerHTML = NQ + '문장 중 ' + wrong + '개 틀림<br>통과컷 ' + (PEN-1) + '개 초과<br>오늘의 ' + NQ + '문장을 책에 다시 써요'; }
    else { f.className = 'final good'; f.innerHTML = '통과!<br>' + NQ + '문장 중 ' + wrong + '개 틀림'; }
    $('meta').innerHTML = '<b>' + esc(prof.name) + '</b> · ' + esc(prof.book) + '<br>' + stamp();
    var html = '';
    results.forEach(function(r){
      var say = '';
      (r.log || []).forEach(function(l, k){
        var label = (r.log.length > 1 ? (k+1) + '차 ' : '') + '말한 것';
        say += '<div class="say"><b>' + label + '</b>' + (l.t ? esc(l.t) : '(인식된 말 없음)') + ' <span style="color:#999">(일치 ' + l.sc + '%)</span></div>';
      });
      html += '<div class="item ' + (r.ok ? '' : 'x') + '"><span class="tag">' + (r.ok ? '○' : '×') + ' ' + prof.book + ' ' + r.n + '번</span>' + esc(r.en) + '<div class="ko"><b style="color:#888;font-size:12px">정답</b> ' + esc(r.ko) + '</div>' + say + '</div>';
    });
    $('list').innerHTML = html;
    if (wrong >= PEN){
      var w = '<div class="write">책의 같은 번호 옆에 이 ' + NQ + '문장의 해석을 다시 쓰세요</div>';
      results.forEach(function(r){ w += '<div class="item"><b>' + r.n + '번</b> ' + esc(r.en) + '<div class="ko">' + esc(r.ko) + '</div></div>'; });
      $('writeBox').innerHTML = w;
    } else $('writeBox').innerHTML = '';
    show('sEnd'); if (window.__releaseMic) window.__releaseMic();
  }
  $('againBtn').onclick = function(){ show('sStart'); };

  // 음성 인식 (한국어)
  var SR = window.SpeechRecognition || window.webkitSpeechRecognition, rec = null, listening = false;
  if (!SR){ $('micBtn').textContent = '이 브라우저는 음성 인식이 안 돼요 (크롬을 쓰세요)'; }
  var wantStop = false, silT = null, baseText = '', finalText = '', alts = [], errored = false, micStream = null, handlersSet = false;
  function silenceMs(){ var n = cur ? cur.ko.replace(/\([^)]*\)/g,'').replace(/\s/g,'').length : 20; return Math.min(6000, 2500 + n * 50); }
  // 마이크 허용창이 자꾸 뜨지 않게: 허용 확인은 처음 한 번만 한다
  var micAsked = false;
  function ensureMic(cb){
    if (micAsked || !navigator.mediaDevices || !navigator.mediaDevices.getUserMedia){ cb(); return; }
    micAsked = true;   // 허용 확인은 처음 한 번만, 확인 직후 바로 닫는다 (열어 둔 채로 두면 폰에서 음성 인식이 소리를 못 받음)
    navigator.mediaDevices.getUserMedia({ audio: true }).then(function(st){
      try { st.getTracks().forEach(function(t){ t.stop(); }); } catch(e){}
      setTimeout(cb, 400);
    }).catch(function(){ cb(); });
  }
  function releaseMic(){ try { if (micStream) micStream.getTracks().forEach(function(t){ t.stop(); }); } catch(e){} micStream = null; }
  function setHandlers(){
    if (handlersSet) return; handlersSet = true;
    rec.lang = 'ko-KR'; rec.interimResults = true; rec.maxAlternatives = 5; rec.continuous = true;
    rec.onstart = function(){ listening = true; $('micBtn').textContent = '듣는 중... 다 말하면 누르세요'; $('micBtn').className = 'big red'; if (!baseText) $('heard').textContent = '...'; };
    rec.onresult = function(e){
      alts = [];
      for (var j=0;j<5;j++){
        var segs = [];
        for (var i=0;i<e.results.length;i++){
          var rr = e.results[i], t = (rr[j] || rr[0]).transcript.trim(); if (!t) continue;
          var last = segs.length ? segs[segs.length-1] : '';
          if (last && t.indexOf(last) === 0) segs[segs.length-1] = t;       // 폰이 같은 말을 점점 길게 되풀이해 주는 경우 → 가장 긴 것만
          else if (last && last.indexOf(t) === 0) {}                         // 더 짧은 되풀이는 무시
          else segs.push(t);
        }
        alts.push((baseText ? baseText + ' ' : '') + segs.join(' '));
      }
      finalText = alts[0]; lastHeard = alts[0]; $('heard').textContent = alts[0];
      clearTimeout(silT);
      silT = setTimeout(function(){ wantStop = true; try { rec.stop(); } catch(e){} }, silenceMs());
    };
    rec.onerror = function(e){
      if (e.error === 'no-speech' && finalText.trim()) return;
      if (e.error === 'aborted') return;
      errored = true; wantStop = true; listening = false; $('micBtn').textContent = '말하기 시작'; $('micBtn').className = 'big blue';
      $('heard').textContent = (e.error === 'not-allowed' || e.error === 'service-not-allowed') ? '마이크 허용이 필요해요. 주소창 왼쪽 자물쇠에서 마이크를 허용하세요.' : ('인식 오류: ' + e.error + ' (다시 눌러 주세요)');
    };
    rec.onend = function(){
      listening = false; clearTimeout(silT);
      if (graded) { $('micBtn').textContent = '말하기 시작'; $('micBtn').className = 'big blue'; return; }
      // (끊겼을 때 자동으로 다시 시작하지 않는다: 시작할 때마다 마이크 허용창이 또 뜨기 때문)
      $('micBtn').textContent = '말하기 시작'; $('micBtn').className = 'big blue';
      if (errored) return;
      if (finalText.trim()){
        var best = finalText, sc = score(finalText, cur.ko);
        alts.forEach(function(t){ var x = score(t, cur.ko); if (x > sc){ sc = x; best = t; } });
        $('heard').textContent = best;
        finishAttempt(sc >= TH, sc, best);
      }
      else $('heard').textContent = '소리가 안 들렸어요. 다시 눌러 말해 주세요.';
    };
  }
  function startRec(){
    if (!rec){ rec = new SR(); }
    setHandlers();
    finalText = baseText; alts = []; errored = false;
    try { rec.start(); } catch(e){}
  }
  $('micBtn').onclick = function(){
    if (!SR || !cur || graded) return;
    if (listening){ wantStop = true; try { rec.stop(); } catch(e){} return; }
    wantStop = false; baseText = ''; lastHeard = '';
    ensureMic(startRec);
  };
  window.addEventListener('pagehide', releaseMic);
  window.__releaseMic = releaseMic;
})();
