var XPAT=[
 {en:'I sleep.',k:'1형식',f:'S + V',tok:[['I','주어','나는'],['sleep','동사','잔다']]},
 {en:'I am happy.',rel:'I = happy',k:'2형식',f:'S + V + 보어',tok:[['I','주어','나는'],['am','동사','~이다'],['happy','보어','행복한']]},
 {en:'I like apples.',rel:'I ≠ apples',k:'3형식',f:'S + V + 목적어',tok:[['I','주어','나는'],['like','동사','좋아한다'],['apples','목적어','사과를']]},
 {en:'I give him a book.',rel:'him ≠ a book',k:'4형식',f:'S + V + 간접목적어 + 직접목적어',tok:[['I','주어','나는'],['give','동사','준다'],['him','간접목적어','그에게'],['a book','직접목적어','책을']]},
 {en:'I make him happy.',rel:'him = happy',k:'5형식',f:'S + V + 목적어 + 목적격보어',tok:[['I','주어','나는'],['make','동사','만든다'],['him','목적어','그를'],['happy','목적격보어','행복하게']]}
];
var XCOL={'주어':'#1e40af','동사':'#475569','목적어':'#15803d','보어':'#c2410c','간접목적어':'#0e7490','직접목적어':'#4d7c0f','목적격보어':'#b45309'};
function xSeq(s){
  function rec(n){
    var q=[{t:'verb',n:n}];if(n.x.glue!=null)q.push({t:'glue',n:n});
    n.x.rounds.forEach(function(r,i){q.push({t:'pat',r:i,n:n});q.push({t:'pair',r:i,n:n});});
    (n.deep||[]).forEach(function(d){
      d.A.ctx=n.ch[d.ci].t.replace(/^[\u201c"]|[\u201d",.?!]+$/g,'');d.A.kind=d.opts?d.opts[d.ans]:'따옴표 안의 문장';
      if(d.opts)q.push({t:'kind',n:n,d:d});
      q=q.concat(rec(d.A));
    });
    return q;
  }
  if(s._q)return s._q;
  s._q=rec(s);return s._q;
}
function xVerbs(s){var o=[];s.ch.forEach(function(c,i){if(c.r==='동사')o.push(i);});return o;}
function xNew(){C.xs={sel:[],fb:null,done:false,mu:null,mt:null,md:{},mtd:{},pk:null,bad:{}};}
function xSkel(s,r){return s.x.rounds[r].ci.filter(function(i){var c=s.ch[i];return c.r!=='수식어'&&c.r!=='접속사';});}
function xMasked(s,r,i){var c=s.ch[i];return s.x.rounds[r].ci.indexOf(i)<0||c.r==='수식어'||c.r==='접속사';}
function xMiss(i,picked,nn){C.mist[1]++;var c=(nn||C.s).ch[i];logW({day:S.day,n:C.s.n,kind:'role',t:c.t,right:c.r,picked:picked});}
function xMaskedLine(s,r){
  var o='<div class="xs">',prev=false;
  s.ch.forEach(function(c,i){
    if(xMasked(s,r,i)){if(!prev)o+='<span class="xc"><span class="xw mask">가림</span><small></small></span>';prev=true;}
    else{prev=false;o+='<span class="xc"><span class="xw">'+esc(c.t)+'</span><small>'+esc(c.k||'')+'</small></span>';}
  });
  return o+'</div>';
}
function vX(){
  if(!C.xs)xNew();
  var seq=xSeq(C.s),e=seq[C.xi],s=e.n,st=C.xs,h='';
  var tt={verb:'동사 찾기',glue:'접착제 찾기',pat:'뼈대 닮은꼴 찾기',pair:'닮은꼴과 선잇기',kind:'덩어리 정체 찾기'}[e.t];
  h+='<p class="xph"><b>엑스레이 분석</b> · '+tt+' ('+(C.xi+1)+'/'+seq.length+')</p>';
  var next='<button class="primary" data-act="xnext">다음 단계</button>';
  if(s!==C.s)h+='<p class="xhint" style="background:#ecfdf5;border-radius:8px;padding:6px 10px">안쪽 분석 · <b>'+esc(s.ctx)+'</b> ('+esc(s.kind)+')</p>';
  if(e.t==='kind'){
    var d=e.d;
    h+='<p class="ask">가려진 덩어리 <b>'+esc(s.ch[d.ci].t.replace(/^[\u201c"]|[\u201d"]+$/g,''))+'</b> 는 무엇일까요?</p><p class="xhint">'+esc(s.ch[d.ci].k||'')+'</p>';
    h+='<div class="xopts">'+d.opts.map(function(o,k){return '<button class="xo'+(st.bad[k]?' no':'')+'" data-act="xk" data-i="'+k+'"'+(st.bad[k]?' disabled':'')+'><span class="xk">'+esc(o)+'</span></button>';}).join('')+'</div>';
    if(st.fb)h+='<p class="msg no">'+st.fb+'</p>';
    return h;
  }
  if(e.t==='verb'||e.t==='glue'){
    var verbs=xVerbs(s);
    h+='<p class="ask">'+(e.t==='verb'?(s!==C.s&&xVerbs(s).length===1&&/^(to |\S+ing$)/.test(s.ch[xVerbs(s)[0]].t)?'동사 자리를 누르세요':'동사를 모두 누르세요'):'두 동사를 붙이는 접착제를 누르세요')+'</p>';
    h+='<p class="xhint">'+(e.t==='verb'?'동사는 "~하다, ~이다"로 끝나는 말이에요. 모두 '+verbs.length+'개예요.':'앞 문장과 뒤 문장을 이어 붙여 주는 말이에요.')+'</p>';
    function cell(i,cl,dis){var c=s.ch[i];return '<span class="xc"><button class="xw '+cl+'" data-act="xw" data-i="'+i+'"'+(dis?' disabled':'')+'>'+esc(c.t)+'</button><small>'+esc(c.k||'')+'</small></span>';}
    if(e.t==='glue'&&st.done){
      var g=s.x.glue,A=[],B=[];
      s.ch.forEach(function(c,i){if(i<g)A.push(i);else if(i>g)B.push(i);});
      h+='<div class="xg"><span class="xcap">앞 문장</span><div class="xs">'+A.map(function(i){return cell(i,verbs.indexOf(i)>=0?'ok':'',true);}).join('')+'</div></div>'
        +'<div class="xs">'+cell(g,'glue',true)+'</div>'
        +'<div class="xg"><span class="xcap">뒤 문장</span><div class="xs">'+B.map(function(i){return cell(i,verbs.indexOf(i)>=0?'ok':'',true);}).join('')+'</div></div>';
    }else{
      h+='<div class="xs">'+s.ch.map(function(c,i){
        var cl='';
        if(e.t==='verb'){if(st.done&&verbs.indexOf(i)>=0)cl='ok';else if(st.sel.indexOf(i)>=0)cl='sel';else if(st.bad[i])cl='no';}
        else{if(verbs.indexOf(i)>=0)cl='ok';else if(st.bad[i])cl='no';}
        return cell(i,cl,st.done||!!st.bad[i]);
      }).join('')+'</div>';
    }
    if(e.t==='verb'&&!st.done&&verbs.length>1)h+='<button class="primary" data-act="xchk"'+(st.sel.length?'':' disabled')+'>확인</button>';
    if(st.fb)h+='<p class="msg no">'+st.fb+'</p>';
    if(st.done){
      if(e.t==='verb')h+='<p class="msg ok">동사는 '+verbs.map(function(i){return '<b>'+esc(s.ch[i].t.replace(/[,.]$/,''))+'</b>';}).join(', ')+' 예요.</p>';
      else h+='<p class="msg ok">접착제는 <b>'+esc(s.ch[s.x.glue].t)+'</b> 예요. '+esc(s.ch[s.x.glue].k)+' 하고 앞뒤 문장을 이어 줘요. 문장을 하나씩 나눠서 뼈대를 찾아요.</p>';
      h+=next;
    }
    return h;
  }
  var r=e.r,ans=s.x.rounds[r].fm-1,P=XPAT[ans];
  if(e.t==='pat'){
    h+='<p class="ask">가림판을 빼고 남은 뼈대는 누구와 닮은꼴?</p><p class="xhint">꾸밈말은 가렸어요. 남은 뼈대의 동사 뒤에 무엇이 오는지 보세요.</p>'+xMaskedLine(s,r);
    h+='<div class="xopts">'+XPAT.map(function(p,k){
      return '<button class="xo'+(st.bad[k]?' no':'')+'" data-act="xp" data-i="'+k+'"'+(st.bad[k]?' disabled':'')+'><span class="xk">'+p.k+'</span><span class="xe">'+p.en+'</span><span class="xf">'+p.f+(p.rel?' · '+p.rel:'')+'</span></button>';
    }).join('')+'</div>';
    if(st.fb)h+='<p class="msg no">'+st.fb+'</p>';
    return h;
  }
  var sk=xSkel(s,r),n=P.tok.length,ord=[],q;
  for(q=0;q<n;q++)ord.push((q+1)%n);
  h+='<p class="ask">뼈대 '+sk.length+'칸을 '+P.en+' 와 짝지어요</p><p class="xhint">같은 자리끼리 짝을 지어요. 문장 한 칸, 닮은꼴 한 칸을 차례로 누르세요.</p>'+xMaskedLine(s,r);
  h+='<div class="xp" id="xp"><svg class="xpl" id="xpl"></svg><div><div class="xrl">내 문장의 뼈대</div>';
  sk.forEach(function(i,j){var c=s.ch[i],dn=st.md[j]!=null;
    h+='<div class="xpi"><button class="xpb'+(dn?' dn r-'+CLS[c.r]:'')+(st.mu===j?' on':'')+'" id="xl'+j+'" data-act="xmu" data-i="'+j+'">'+esc(c.t)+'</button><small>'+(dn?'<span class="xrp r-'+CLS[c.r]+'">'+(LBL[c.r]||c.r)+'</span>'+esc(c.k||''):'')+'</small></div>';});
  h+='</div><div><div class="xrl">닮은꼴</div>';
  ord.forEach(function(j){var t=P.tok[j],dn=st.mtd[j];
    h+='<div class="xpi"><button class="xpb'+(dn?' dn r-'+CLS[t[1]]:'')+(st.mt===j?' on':'')+'" id="xr'+j+'" data-act="xmt" data-i="'+j+'">'+esc(t[0])+'</button><small>'+(dn?'<span class="xrp r-'+CLS[t[1]]+'">'+t[1]+'</span>'+esc(t[2]):'')+'</small></div>';});
  h+='</div></div>';
  if(st.fb)h+='<p class="msg no">'+st.fb+'</p>';
  if(st.done)h+='<p class="msg ok"><b>'+P.k+'</b> · '+P.f+' · '+P.en+' 와 같은 뼈대예요.</p>'+next;
  return h;
}
function xDraw(){
  var c=document.getElementById('xp'),sv=document.getElementById('xpl');
  if(!c||!sv||!C||!C.xs||!C.s.x)return;
  var e=xSeq(C.s)[C.xi];if(!e||e.t!=='pair')return;
  var cr=c.getBoundingClientRect(),h='',sk=xSkel(e.n,e.r);
  sv.setAttribute('viewBox','0 0 '+cr.width+' '+cr.height);
  Object.keys(C.xs.md).forEach(function(j){
    var a=document.getElementById('xl'+j),b=document.getElementById('xr'+C.xs.md[j]);if(!a||!b)return;
    var ar=a.getBoundingClientRect(),br=b.getBoundingClientRect(),x1=ar.right-cr.left,y1=ar.top+ar.height/2-cr.top,x2=br.left-cr.left,y2=br.top+br.height/2-cr.top,m=(x2-x1)/2;
    h+='<path d="M'+x1+' '+y1+' C'+(x1+m)+' '+y1+' '+(x2-m)+' '+y2+' '+x2+' '+y2+'" fill="none" stroke="'+(XCOL[e.n.ch[sk[j]].r]||'#0f766e')+'" stroke-width="3.5" stroke-linecap="round"/>';
  });
  sv.innerHTML=h;
}
window.addEventListener('resize',function(){try{xDraw();}catch(e){}});
window.__X={C:function(){return C;},xSeq:xSeq,xVerbs:xVerbs,xSkel:xSkel,XPAT:XPAT};
