/* 동남비타민영어학원 - 진도 자동저장용 Apps Script (학교별 시트 탭 자동 생성: scope 값이 탭 이름)
   사용법: 구글 시트 새로 만들기 > 확장 프로그램 > Apps Script > 이 코드 붙여넣기
   > 배포 > 새 배포 > 유형: 웹 앱 > 실행: 나 / 액세스: 모든 사용자 > 배포 > URL 복사 */
function out_(o){return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON)}
function doGet(e){
  var p=e.parameter||{}, name=String(p.name||'').trim(), pin=String(p.pin||'').trim();
  if(!name||!/^\d{4}$/.test(pin)) return out_({ok:false,err:'bad'});
  var lock=LockService.getScriptLock(); lock.waitLock(15000);
  try{
    var ss=SpreadsheetApp.getActiveSpreadsheet();
    var tab=String(p.scope||'진도').replace(/[\[\]\*\?:\/\\]/g,'').slice(0,40)||'진도';
    var sh=ss.getSheetByName(tab)||ss.insertSheet(tab);
    if(sh.getLastRow()===0){
      sh.appendRow(['이름','번호','수정시각','체크수','최종수정','코드']);
      sh.getRange('B:B').setNumberFormat('@');
    }
    var v=sh.getDataRange().getValues(), row=-1, i;
    for(i=1;i<v.length;i++){ if(String(v[i][0]).trim()===name){row=i+1;break} }
    if(row>0 && String(v[row-1][1]).padStart(4,'0')!==pin) return out_({ok:false,err:'pin'});
    if(p.act==='get'){
      if(row<0) return out_({ok:true,ts:0,data:''});
      return out_({ok:true,ts:Number(v[row-1][2])||0,data:String(v[row-1][5]||'')});
    }
    if(p.act==='put'){
      var ts=Number(p.ts)||Date.now();
      if(row<0){ row=sh.getLastRow()+1; sh.getRange(row,2).setNumberFormat('@') }
      else if((Number(v[row-1][2])||0)>ts) return out_({ok:true,stale:true});
      sh.getRange(row,1,1,6).setValues([[name,pin,ts,Number(p.cnt)||0,new Date(ts),String(p.data||'')]]);
      return out_({ok:true});
    }
    return out_({ok:false,err:'act'});
  } finally { lock.releaseLock() }
}
