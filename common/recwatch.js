/* recwatch 261118a — 기록 한 묶음(8조각)을 "바뀔 때만" 받는 장치. 화면이 주기적으로 다시 읽지 않아도 되게 한다.
   쓰는 법: __recWatch(id, 바뀌면 부를 함수). __recLive(id) 가 참이면 연결되어 있고, __recData(id) 가 지금 내용({key:{v,t}})이다.
   연결이 안 되거나 끊기면 __recLive 가 거짓이 되고, 화면은 예전처럼 주기적으로 읽는다. 주소에 snap=0 을 붙이면 끈다. */
const W=window;
const S=W.__recW={ids:{},err:0,n:0};
W.__recLive=id=>{const x=S.ids[id];return !!(x&&x.ok&&x.got===8)};
W.__recData=id=>{
  const x=S.ids[id];if(!x||!x.ok||x.got!==8)return null;
  const data={};let found=0;
  for(let i=0;i<8;i++){const o=x.part[i];if(!o)continue;found++;for(const k in o){try{data[k]={v:JSON.parse(String(o[k][0])),t:Number(o[k][1])}}catch(e){}}}
  return found?data:null;
};
let dbp=null;
function db(){
  if(!dbp)dbp=(async()=>{
    const {initializeApp}=await import("https://www.gstatic.com/firebasejs/10.14.1/firebase-app.js");
    const F=await import("https://www.gstatic.com/firebasejs/10.14.1/firebase-firestore.js");
    return {F,db:F.getFirestore(initializeApp({apiKey:"AIzaSyC88G-OjMJOqVqnIVqunzh7fvk91wtKKnA",projectId:"h-roadmap",appId:"1:575520405083:web:b9f40b64cb0ae3d1a9317e"},"rec-watch"))};
  })();
  return dbp;
}
W.__recWatch=(id,cb)=>{
  if(/[?&]snap=0/.test(location.search)||S.ids[id])return;
  const x=S.ids[id]={ok:true,got:0,seen:{},part:{},raw:{},subs:[]};
  const col=/(^|[|:])샘플\d*([|:]|$)/.test(id)?"rec_s":"rec";
  let tm=null;
  const fail=()=>{S.err++;x.ok=false;x.subs.forEach(u=>{try{u()}catch(e){}});x.subs=[]};
  db().then(({F,db})=>{
    for(let i=0;i<8;i++){
      x.subs.push(F.onSnapshot(F.doc(db,col,id+"~"+i),snap=>{
        if(snap.metadata.fromCache)return;
        const raw=snap.exists()?String(snap.data().j||""):"";
        const first=!x.seen[i];
        if(!first&&x.raw[i]===raw)return;
        x.raw[i]=raw;
        try{x.part[i]=raw?JSON.parse(raw):null}catch(e){x.part[i]=null}
        if(first){x.seen[i]=1;x.got++}
        S.n++;
        if(!first&&x.got===8&&cb){clearTimeout(tm);tm=setTimeout(()=>{try{cb()}catch(e){}},400)}
      },fail));
    }
  },fail);
};
W.dispatchEvent(new Event("recwatch"));
