/* 동남비타민영어학원 - 학생 자료 서버 (로그인 + 지문 자료 보관 + 진도 자동저장)
   쓰는 법
   1) 구글 시트를 새로 만든다 (남편 선생님 계정).
   2) 확장 프로그램 > Apps Script > 이 코드 전체를 붙여넣고 아래 ADMIN_KEY 를 나만 아는 문자열로 바꾼다.
   3) 배포 > 새 배포 > 유형 "웹 앱" > 실행: 나 / 액세스: 모든 사용자 > 배포 > 웹 앱 URL 복사.
   4) 시트의 [학생] 탭에 학생을 적는다 (처음 한 번 아무 요청이 오면 탭이 자동으로 생겨요).
      이름 | 번호(4자리) | 상태(재원 또는 퇴원) | 반 | 마지막접속
      상태를 "퇴원"으로 바꾸면 그 학생은 다음 접속부터 자료가 열리지 않아요. 다른 학생은 영향이 없어요.
   5) seed.html 로 지문 자료를 시트에 올린다 (한 번만, 자료를 고쳤을 때 다시).
   코드를 고치면 배포 > 배포 관리 > 편집 > 새 버전 으로 다시 배포해야 반영돼요. */
var ADMIN_KEY = '여기를-내가-정한-긴-문자열로-바꾸세요';
var CHUNK = 40000;          // 셀 하나에 넣는 글자 수 (셀 한도 50,000자)
var MAX_FAIL = 10;          // 같은 이름으로 번호를 연속 틀릴 수 있는 횟수
var LOCK_SEC = 900;         // 잠기는 시간(초) = 15분

function json_(o){ return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }
function js_(s){ return ContentService.createTextOutput(s).setMimeType(ContentService.MimeType.JAVASCRIPT); }
function ss_(){ return SpreadsheetApp.getActiveSpreadsheet(); }

function roster_(){
  var sh = ss_().getSheetByName('학생');
  if(!sh){
    sh = ss_().insertSheet('학생');
    sh.appendRow(['이름','번호','상태','반','마지막접속']);
    sh.getRange('B:B').setNumberFormat('@');
    sh.setFrozenRows(1);
  }
  return sh;
}
function store_(){
  var sh = ss_().getSheetByName('자료');
  if(!sh){
    sh = ss_().insertSheet('자료');
    sh.appendRow(['키','순번','내용']);
    sh.getRange('A:A').setNumberFormat('@');
    sh.getRange('C:C').setNumberFormat('@');
    sh.setFrozenRows(1);
  }
  return sh;
}

/* 학생 확인: 'ok' | 'pin'(이름 또는 번호 불일치) | 'out'(퇴원) | 'lock'(잠김) */
function check_(name, pin, touch){
  var cache = CacheService.getScriptCache(), lk = 'fail:' + name;
  var f = Number(cache.get(lk)) || 0;
  if(f >= MAX_FAIL) return 'lock';
  var sh = roster_(), v = sh.getDataRange().getValues(), i;
  for(i = 1; i < v.length; i++){
    if(String(v[i][0]).trim() === name){
      if(String(v[i][1]).trim().padStart(4,'0') !== pin){ cache.put(lk, String(f + 1), LOCK_SEC); return 'pin'; }
      var st = String(v[i][2] || '').trim();
      if(st === '퇴원' || st === '중지' || st === '정지') return 'out';
      if(touch) sh.getRange(i + 1, 5).setValue(new Date());
      cache.remove(lk);
      return 'ok';
    }
  }
  cache.put(lk, String(f + 1), LOCK_SEC);
  return 'pin';
}
function rosterSize_(){ var sh = roster_(); return Math.max(0, sh.getLastRow() - 1); }

function readData_(key){
  var sh = store_(), last = sh.getLastRow();
  if(last < 2) return null;
  var hits = sh.getRange(2, 1, last - 1, 1).createTextFinder(key).matchEntireCell(true).findAll();
  if(!hits.length) return null;
  var parts = [];
  hits.forEach(function(r){
    var row = r.getRow();
    parts.push({ i: Number(sh.getRange(row, 2).getValue()), t: String(sh.getRange(row, 3).getValue()) });
  });
  parts.sort(function(a, b){ return a.i - b.i; });
  return parts.map(function(p){ return p.t.substring(1); }).join('');   // 맨 앞 'J' 표시 제거
}

function doGet(e){
  var p = e.parameter || {}, act = String(p.act || '');
  var name = String(p.name || '').trim(), pin = String(p.pin || '').trim();

  if(act === 'login'){
    var cb = String(p.cb || '');
    if(!/^[A-Za-z0-9_]+$/.test(cb)) return json_({ ok: false, err: 'bad' });
    var r = (name && /^\d{4}$/.test(pin)) ? check_(name, pin, true) : 'pin';
    return js_(cb + '(' + JSON.stringify(r === 'ok' ? { ok: true } : { ok: false, err: r }) + ');');
  }

  if(act === 'data'){
    var kind = String(p.kind || ''), id = String(p.id || '');
    if(['data','voca','verb'].indexOf(kind) < 0 || !/^[A-Za-z0-9_-]+$/.test(id)) return js_('window.MOGO_DENY="bad";');
    var st = (name && /^\d{4}$/.test(pin)) ? check_(name, pin, false) : 'pin';
    if(st !== 'ok') return js_('window.MOGO_DENY="' + st + '";');
    var body = readData_(kind + ':' + id);
    if(body === null) return js_('window.MOGO_DENY="none";');
    return js_(body);
  }

  if(act === 'check'){                      // 관리자: 올라간 자료 목록
    if(String(p.admin || '') !== ADMIN_KEY) return json_({ ok: false, err: 'admin' });
    var sh = store_(), last = sh.getLastRow(), cnt = {};
    if(last >= 2){
      sh.getRange(2, 1, last - 1, 1).getValues().forEach(function(r){ cnt[r[0]] = (cnt[r[0]] || 0) + 1; });
    }
    return json_({ ok: true, keys: cnt, students: rosterSize_() });
  }

  /* 진도 자동저장 (get / put) - 학생 명단이 있으면 명단으로 확인 */
  if(act === 'get' || act === 'put'){
    if(!name || !/^\d{4}$/.test(pin)) return json_({ ok: false, err: 'bad' });
    var lock = LockService.getScriptLock(); lock.waitLock(15000);
    try{
      if(rosterSize_() > 0){
        var c = check_(name, pin, false);
        if(c !== 'ok') return json_({ ok: false, err: c === 'out' ? 'out' : 'pin' });
      }
      var tab = String(p.scope || '진도').replace(/[\[\]\*\?:\/\\]/g, '').slice(0, 40) || '진도';
      var ss = ss_(), sh2 = ss.getSheetByName(tab) || ss.insertSheet(tab);
      if(sh2.getLastRow() === 0){
        sh2.appendRow(['이름','번호','수정시각','체크수','최종수정','코드']);
        sh2.getRange('B:B').setNumberFormat('@');
      }
      var v = sh2.getDataRange().getValues(), row = -1, i;
      for(i = 1; i < v.length; i++){ if(String(v[i][0]).trim() === name){ row = i + 1; break; } }
      if(row > 0 && String(v[row - 1][1]).padStart(4,'0') !== pin) return json_({ ok: false, err: 'pin' });
      if(act === 'get'){
        if(row < 0) return json_({ ok: true, ts: 0, data: '' });
        return json_({ ok: true, ts: Number(v[row - 1][2]) || 0, data: String(v[row - 1][5] || '') });
      }
      var ts = Number(p.ts) || Date.now();
      if(row < 0){ row = sh2.getLastRow() + 1; sh2.getRange(row, 2).setNumberFormat('@'); }
      else if((Number(v[row - 1][2]) || 0) > ts) return json_({ ok: true, stale: true });
      sh2.getRange(row, 1, 1, 6).setValues([[name, pin, ts, Number(p.cnt) || 0, new Date(ts), String(p.data || '')]]);
      return json_({ ok: true });
    } finally { lock.releaseLock(); }
  }
  return json_({ ok: false, err: 'act' });
}

/* 관리자: 자료 올리기 (seed.html 이 호출) - 본문: {admin, key, idx, total, chunk} */
function doPost(e){
  var b;
  try{ b = JSON.parse(e.postData.contents); }catch(err){ return json_({ ok: false, err: 'json' }); }
  if(String(b.admin || '') !== ADMIN_KEY) return json_({ ok: false, err: 'admin' });
  var key = String(b.key || '');
  if(!/^(data|voca|verb):[A-Za-z0-9_-]+$/.test(key)) return json_({ ok: false, err: 'key' });
  var lock = LockService.getScriptLock(); lock.waitLock(30000);
  try{
    var sh = store_(), last = sh.getLastRow();
    if(Number(b.idx) === 0 && last >= 2){                       // 첫 조각: 같은 키의 옛 조각 삭제
      var hits = sh.getRange(2, 1, last - 1, 1).createTextFinder(key).matchEntireCell(true).findAll();
      hits.map(function(r){ return r.getRow(); }).sort(function(a, b){ return b - a; }).forEach(function(r){ sh.deleteRow(r); });
    }
    var row = sh.getLastRow() + 1;
    sh.getRange(row, 1, 1, 3).setNumberFormat('@').setValues([[key, Number(b.idx), 'J' + String(b.chunk || '')]]);
    return json_({ ok: true });
  } finally { lock.releaseLock(); }
}
