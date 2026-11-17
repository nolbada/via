/* 기록 서버 받기 요청을 Firebase 에서 바로 답하는 장치 (261117g). common/sync.js 안에 든 것과 같은 내용이며, sync.js 를 쓰지 않는 화면(숙제 앱 등)이 이 파일을 부른다.
   기록 서버에 "받기만" 하는 요청(act:'put' 에 data 가 빈 것)은 Firebase 에서 바로 답한다. 한 기록은 8조각이라 한 번에 받는다.
   조각이 하나도 없거나 실패·2.5초 초과면 원래 요청을 그대로 서버로 보낸다. 쓰기 요청과 내신 기록(REC|·RECM|)은 건드리지 않는다. 오류가 나도 앱 본체에는 영향이 없다. */
(function(){var W=window;
  try{(function(){
    if(W.__recFs||!W.fetch||!W.Response)return;W.__recFs=1;
    var of=W.fetch;
    function fsRead(id){
      try{
        var smp=/(^|[|:])샘플\d*([|:]|$)/.test(id),base='projects/h-roadmap/databases/(default)/documents/'+(smp?'rec_s':'rec')+'/'+String(id).replace(/%/g,'%25').replace(/\//g,'%2F')+'~',names=[],i;
        for(i=0;i<8;i++)names.push(base+i);
        var ac=W.AbortController?new AbortController():null,tm=ac?setTimeout(function(){ac.abort()},2500):0;
        return of.call(W,'https://firestore.googleapis.com/v1/projects/h-roadmap/databases/(default)/documents:batchGet',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({documents:names}),signal:ac?ac.signal:undefined})
          .then(function(r){clearTimeout(tm);return r.ok?r.json():null})
          .then(function(a){
            if(!Array.isArray(a)||a.length!==8)return null;
            var data={},found=0,j,o,k,x;
            for(j=0;j<a.length;j++){
              x=a[j];if(x.missing)continue;if(!x.found)return null;found++;
              o=x.found.fields&&x.found.fields.j&&x.found.fields.j.stringValue;if(!o)continue;o=JSON.parse(o);
              for(k in o){try{data[k]={v:JSON.parse(String(o[k][0])),t:Number(o[k][1])}}catch(e){}}
            }
            return found?{ok:1,data:data,fs:1}:null;
          }).catch(function(){clearTimeout(tm);return null});
      }catch(e){return Promise.resolve(null)}
    }
    W.fetch=function(u,o){
      try{
        if(typeof u==='string'&&u.indexOf('AKfycbw1YQfKsgAXNk8NYoxOfz4bsCSy66fiim7HoFAUk162ksxrEbmspMs2UifNZ-93sdf05A')>0&&o&&o.method==='POST'&&typeof o.body==='string'&&o.body.length<600){
          var b=JSON.parse(o.body),k,n=0;
          if(b&&b.act==='put'&&typeof b.id==='string'&&b.id.length>=3&&!/^RECM?\|/.test(b.id)&&b.data&&typeof b.data==='object'){
            for(k in b.data)n++;
            if(!n){var self=this,args=arguments;return fsRead(b.id).then(function(r){return r?new W.Response(JSON.stringify(r),{status:200,headers:{'Content-Type':'application/json'}}):of.apply(self,args)})}
          }
        }
      }catch(e){}
      return of.apply(this,arguments);
    };
  })()}catch(e){}
})();
