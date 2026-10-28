(function(){
"use strict";
// 보카링크 본책 정답지 — 초판(2026-08-18 인쇄) 별책 정답지 PART 1·PART 2 기준.
const MEM='vl_key_v1';
const esc=s=>String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
const ld=()=>{try{return JSON.parse(localStorage.getItem(MEM)||'null')||{};}catch(e){return{};}};
const sv=v=>{try{localStorage.setItem(MEM,JSON.stringify(v));}catch(e){}};
(function css(){
 const s=document.createElement('style');
 s.textContent=`.cv-kb{display:block;margin:14px auto 0;padding:9px 24px;border:1.5px solid rgba(255,244,230,.6);border-radius:22px;background:none;color:#fff;font-family:inherit;font-weight:700;font-size:14px;cursor:pointer}.cv-kb:active{background:rgba(255,244,230,.14)}
.ky-card{background:#fff;border:1px solid var(--line);border-radius:16px;padding:4px 14px;margin:6px 0 14px}
.ky-r{display:flex;align-items:baseline;gap:8px;padding:9px 0;border-bottom:1px solid var(--line);font-size:18px;line-height:1.45}.ky-r:last-child{border-bottom:0}
.ky-n{flex:none;min-width:24px;white-space:nowrap;color:var(--sub);font-size:14px;font-weight:700}
.ky-m{flex:1;min-width:0}.ky-m b{font-weight:800}.ky-m small{color:var(--sub);font-size:14px;font-weight:400;margin-left:8px}
.ky-g{display:grid;grid-template-columns:repeat(5,1fr);gap:6px;padding:10px 0}.ky-g div{text-align:center;border:1px solid var(--line);border-radius:10px;padding:6px 0;font-size:19px;font-weight:800;line-height:1.2}.ky-g small{display:block;color:var(--sub);font-size:11px;font-weight:700;margin-bottom:3px}
.ky-p{padding:10px 0;border-bottom:1px solid var(--line);font-size:16px;line-height:1.7}.ky-p:last-child{border-bottom:0}.ky-p b{font-size:18px;margin-right:6px}.ky-p span{color:#333}
.ky-t{display:flex;gap:6px;margin:10px 0 2px}.ky-t button{flex:1;padding:10px 0;border:1.5px solid var(--line);background:#fff;border-radius:12px;font-size:16px;font-weight:700;font-family:inherit;color:var(--ink)}.ky-t button.on{background:var(--ink);color:#fff;border-color:var(--ink)}
.ky-nv{display:flex;gap:8px;margin:6px 0 24px}.ky-nv button{flex:1;padding:13px 0;border:1.5px solid var(--line);background:#fff;border-radius:12px;font-size:16px;font-weight:700;font-family:inherit;color:var(--ink)}.ky-nv button:disabled{opacity:.35}`;
 document.head.appendChild(s);
})();
let $=null,back=null;
const DAYS=Object.keys(window.VL_KEY).map(Number).sort((a,b)=>a-b);
function list(){
 $.innerHTML=`<div class="top"><button class="back" id="kb">← 처음으로</button></div><h1>본책 정답지</h1><div class="sub">초판 본책 기준</div>
 <div class="vt-grid">${DAYS.map(n=>`<button class="vt-d" data-d="${n}">${n}<small>DAY</small></button>`).join('')}</div>`;
 document.getElementById('kb').onclick=()=>{window.scrollTo(0,0);back();};
 $.querySelectorAll('[data-d]').forEach(b=>b.onclick=()=>{window.scrollTo(0,0);view(+b.dataset.d,(ld().part)||1);});
}
const row=(n,a,k)=>`<div class="ky-r"><span class="ky-n">${n}</span><span class="ky-m">${a}${k?`<small>${esc(k)}</small>`:''}</span></div>`;
function p1(d){
 return `<div class="vt-sec">B 유·반의어 사지선다</div><div class="ky-card">${d.b.map((x,i)=>row(i+1,`<b>${x[0]} ${esc(x[1])}</b>`,x[2])).join('')}</div>
 <div class="vt-sec">B 혼동어</div><div class="ky-card">${d.h.map((x,i)=>row(i+1,`<b>${esc(x[0])}</b>`,x[1])).join('')}</div>
 <div class="vt-sec">C 다의어 뜻번호</div><div class="ky-card"><div class="ky-g">${d.c.map((x,i)=>`<div><small>${i+1}</small>${x}</div>`).join('')}</div></div>
 <div class="vt-sec">D 파생어</div><div class="ky-card">${d.d.map((x,i)=>row(i+1,`<b>${x[0]} ${esc(x[1])}</b>`,x[2])).join('')}</div>`;
}
function p2(d){
 return `<div class="vt-sec">짝 잇기</div><div class="ky-card">${d.pair.map(x=>row(x[0]+' - '+x[1],`<b>${esc(x[2])}</b>`,x[3])).join('')}</div>
 <div class="vt-sec">다의어</div><div class="ky-card">${d.poly.map(x=>`<div class="ky-p"><b>${esc(x[0])}</b><span>${esc(x[1])}</span></div>`).join('')}</div>
 <div class="vt-sec">파생어</div><div class="ky-card">${row('어근',`<b>${esc(d.der.root)}</b>`,'')}${d.der.f.map(x=>row(x[0],`<b>${esc(x[1])}</b>`,x[2])).join('')}</div>
 <div class="vt-sec">꺼내 쓰기</div><div class="ky-card">${d.rec.map(x=>row(x[0],`<b>${esc(x[1])}</b>`,x[2])).join('')}</div>`;
}
function view(n,part){
 const d=window.VL_KEY[n],i=DAYS.indexOf(n);
 const st=ld();st.part=part;sv(st);
 $.innerHTML=`<div class="top"><button class="back" id="kb">← DAY 목록</button></div><h1>DAY ${n}</h1><div class="sub">본책 정답지</div>
 <div class="ky-t"><button data-p="1" class="${part===1?'on':''}">PART 1 본책</button><button data-p="2" class="${part===2?'on':''}">PART 2 복습</button></div>
 ${part===1?p1(d):p2(d)}
 <div class="ky-nv"><button id="kpv"${i<=0?' disabled':''}>← DAY ${DAYS[i-1]||''}</button><button id="knx"${i>=DAYS.length-1?' disabled':''}>DAY ${DAYS[i+1]||''} →</button></div>`;
 document.getElementById('kb').onclick=()=>{window.scrollTo(0,0);list();};
 $.querySelectorAll('[data-p]').forEach(b=>b.onclick=()=>{view(n,+b.dataset.p);});
 document.getElementById('kpv').onclick=()=>{window.scrollTo(0,0);view(DAYS[i-1],part);};
 document.getElementById('knx').onclick=()=>{window.scrollTo(0,0);view(DAYS[i+1],part);};
}
window.VLKEY={open:function(el,home){$=el;back=home;list();}};
})();
