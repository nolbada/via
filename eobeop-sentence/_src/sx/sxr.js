/* 구조 분석(sx) 공용 렌더러 — 앱·추가문제 공통 */
function sxEsc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;')}
function sxMk(t){var s=sxEsc(t);
  s=s.replace(/\{o\|([^}]*)\}/g,'<span class="o">($1)</span>');
  s=s.replace(/\{([avcpk])\|([^}]*)\}/g,'<b class="$1">$2</b>');
  return s.replace(/【/g,'<i class="br">【</i>').replace(/】/g,'<i class="br">】</i>')}
function sxHtml(sx,kos,x2){
  if(!sx||sx.length!=kos.length)return '';
  x2=x2||{};var rel=x2.rel||[];
  var h='<div class="sxw"><div class="sxh">문장 구조 분석</div>';
  if(x2.pt)h+='<div class="sxpt"><span class="tag">어법분석</span><span class="wr">'+sxEsc(x2.pt[0])+' (✖)</span><span>'+sxEsc(x2.pt[1])+'</span></div>';
  h+='<div class="sxlg">굵은 밑줄 동사 · 노란 형광 정답 · 빨강 출제 포인트 · 상자 접속사/관계사 · 【 】 절/준동사구 · 빨간 (괄호) 생략된 말 · 초록 메모</div>';
  h+='<div class="sxf'+(rel.length?' hasrel':'')+'" data-rel="'+sxEsc(JSON.stringify(rel))+'">';
  sx.forEach(function(x,i){if(i)h+='<span class="sxsl">/</span>';var n=x[1]||'',red=n.charAt(0)=='!';if(red)n=n.slice(1);
    h+='<span class="sxs" data-i="'+i+'">'+(n?'<span class="nt2'+(red?' red':'')+'">'+sxEsc(n)+'</span>':'')+'<span class="en2">'+sxMk(x[0])+'</span><span class="ko2">'+sxEsc(kos[i])+'</span></span>'});
  h+='</div>';
  if(x2.st)h+='<div class="sxst"><span class="tag">Study</span><span class="tt">'+sxEsc(x2.st[0])+'</span>'+x2.st[1].map(function(l){return '<div>'+sxEsc(l)+'</div>'}).join('')+'</div>';
  return h+'</div>'}
function sxArcs(root){
  var NS='http://www.w3.org/2000/svg';
  (root||document).querySelectorAll('.sxf.hasrel').forEach(function(f){
    var old=f.querySelector('.sxsvg');if(old)f.removeChild(old);
    var rel;try{rel=JSON.parse(f.getAttribute('data-rel'))}catch(e){return}
    var fr=f.getBoundingClientRect();if(!fr.width)return;
    var svg=document.createElementNS(NS,'svg');svg.setAttribute('class','sxsvg');svg.setAttribute('width',fr.width);svg.setAttribute('height',fr.height);
    svg.innerHTML='<defs><marker id="sxah" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 z" fill="#0a7a2f"/></marker></defs>';
    var drawn=0;
    rel.forEach(function(r){
      var a=f.querySelector('.sxs[data-i="'+r[0]+'"] .en2'),b=f.querySelector('.sxs[data-i="'+r[1]+'"] .en2');if(!a||!b)return;
      var ra=a.getBoundingClientRect(),rb=b.getBoundingClientRect();
      if(Math.abs(ra.top-rb.top)>8)return;
      var y=ra.top-fr.top-2,xa=ra.left+ra.width/2-fr.left,xb=rb.left+rb.width/2-fr.left,xm=(xa+xb)/2,k=r[2],lab=r[3]||'';
      var p=document.createElementNS(NS,'path');p.setAttribute('fill','none');p.setAttribute('stroke','#0a7a2f');p.setAttribute('stroke-width','1.6');
      if(k=='par'){p.setAttribute('stroke','#222');p.setAttribute('d','M'+xa+' '+y+' L'+xa+' '+(y-7)+' L'+xb+' '+(y-7)+' L'+xb+' '+y)}
      else{p.setAttribute('d','M'+xa+' '+y+' Q'+xm+' '+(y-20)+' '+xb+' '+(y-1));p.setAttribute('marker-end','url(#sxah)');if(k=='eq')p.setAttribute('stroke-dasharray','4 3')}
      svg.appendChild(p);drawn++;
      if(lab||k=='par'||k=='eq'){var t=document.createElementNS(NS,'text');t.setAttribute('x',xm);t.setAttribute('y',y-(k=='par'?9:12));t.setAttribute('text-anchor','middle');t.setAttribute('font-size','10.5');t.setAttribute('font-weight','700');t.setAttribute('fill',k=='par'?'#222':'#0a7a2f');t.textContent=lab||(k=='par'?'병렬':'동격');svg.appendChild(t)}
    });
    if(drawn)f.appendChild(svg)});
}
window.addEventListener('resize',function(){sxArcs()});
