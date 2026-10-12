/* FBI 공용: 단어 데이터와 저장소 */
const SETS=[
{id:'23.9-31',label:'23년 9월 31번',w:[['instill','불어넣다, 스며들게 하다'],['potential','잠재적인'],['solely','오로지'],['statistically','통계적으로'],['odds','확률'],['anxiety','불안'],['base','근거를 두다, 기초, 기반'],['distance','거리'],['crash','충돌사고'],['favor','유리함, 호의, 부탁'],['risk','위험'],['logic','논리'],['emotion','감정'],['well-being','웰빙, 복지, 행복'],['deceptive','현혹시키는'],['dilemma','딜레마'],['terrified','겁먹은'],['irrational','비합리적인'],['rational','이성적인'],['risk-taker','위험을 감수하는 사람']]},
{id:'23.9-32',label:'23년 9월 32번',w:[['primatologist','영장류학자'],['downplay','경시하다'],['offender','장본인'],['distance','거리를 두다, 거리'],['qualitatively','질적으로'],['instinct','본능'],['cognitive','인지의'],['castration','거세'],['disempower','힘을 빼앗다'],['dominance','지배'],['biased','편향된'],['devalue','평가절하하다'],['discrimination','차별'],['superiority','우월성'],['uphold','옹호하다, 지지하다'],['terminology','용어'],['strategy','전략'],['technique','기법'],['distinguish','구별하다'],['similarity','유사성']]},
{id:'23.9-33',label:'23년 9월 33번',w:[['engagement','참여'],['achievement','성취'],['relevant','관련된'],['scholarly','학문적인'],['physicist','물리학자'],['biochemist','생화학자'],['bypass','우회하다, 건너뛰다'],['compensate','보완하다, 보상하다'],['voraciously','게걸스럽게(열심히)'],['foster','길러내다, 조성하다'],['enthusiastic','열렬한'],['passionate','열정적인'],['interest','관심, 이익'],['tailor','맞추다'],['significance','중요성'],['pursue','추구하다'],['discourage','좌절시키다'],['seek','찾다'],['utilize','활용하다'],['correspond','부합하다']]}];
const KEY='fbi_vocab_v2',WINT=[1,3,7,14,30,60];
let V={w:{},ans:{},done:{},tested:{},sess:null};
try{const o=JSON.parse(localStorage.getItem(KEY)||'null');if(o)V=Object.assign(V,o)}catch(e){}
function save(){try{localStorage.setItem(KEY,JSON.stringify(V))}catch(e){}}
function setLast(o){try{o.t=Date.now();localStorage.setItem('fbi_last',JSON.stringify(o))}catch(e){}}
const esc=s=>String(s==null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;');
const TODAY=()=>Math.floor((Date.now()-new Date().getTimezoneOffset()*60000)/864e5);
const shuf=a=>{a=a.slice();for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a};
const ALL={},FROM={};SETS.forEach(s=>s.w.forEach(x=>{if(!ALL[x[0]]){ALL[x[0]]=x[1];FROM[x[0]]=s.label}}));
const rec=w=>(V.w[w]=V.w[w]||{box:0,miss:0,due:TODAY(),seen:0,star:0});
const isStar=w=>!!(V.w[w]&&V.w[w].star);
function toggleStar(w){const r=rec(w);r.star=r.star?0:1;save();return r.star}
function starCount(){return Object.keys(V.w).filter(w=>V.w[w].star).length}
const TAGN={new:'오늘 새 단어',cum:'지난 누적',wr:'틀렸던 단어',fresh:'처음 보는 단어',star:'내 단어장'};
