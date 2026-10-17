
var SUBS={'명사절':['주어','목적어','보어','동격'],'형용사절':['주격 관계대명사','목적격 관계대명사','관계부사','계속적 용법(which)'],'부사절':['시간','이유','양보','조건','목적']};
var FMS=[['1형식','I sleep.','나는 잔다.','S + V',['I','sleep']],['2형식','I am happy.','나는 행복하다.','S + V + 보어 · I = happy',['I','am','happy']],['3형식','I like apples.','나는 사과를 좋아한다.','S + V + 목적어 · I ≠ apples',['I','like','apples']],['4형식','I give him a book.','나는 그에게 책을 준다.','S + V + 간접목적어 + 직접목적어 · him ≠ a book',['I','give','him','a book']],['5형식','I make him happy.','나는 그를 행복하게 만든다.','S + V + 목적어 + 목적격보어 · him = happy',['I','make','him','happy']]];
function gqInit(){var s=C.s;if(!s.gq)return;if(!C.cq){C.cq={};s.gq.cl.forEach(function(x){C.cq[x.ci]={k:false,s:false};});C.fmOk=false;}}
function gqDone(){var s=C.s;if(!s.gq)return true;gqInit();return C.fmOk&&s.gq.cl.every(function(x){var q=C.cq[x.ci];return q.k&&q.s;});}
function gqSent(activeCi){
  var s=C.s,cls={};s.gq.cl.forEach(function(x){cls[x.ci]=x;});
  var h='<div class="gqs">';
  s.ch.forEach(function(c,ci){
    var sp=(ci&&!c.g)?' ':'';
    if(c.r==='수식어'){
      var x=cls[ci];
      if(x&&(C.fmOk||C.cq[ci].k)){h+=sp+'<span class="gqk'+(activeCi===ci&&!C.cq[ci].s?' act':'')+'">'+esc(c.t)+'</span>';}
      else if(x){h+=sp+'<span class="gqm'+(activeCi===ci?' act':'')+'">'+esc(c.t.split(/\s+/)[0].replace(/[^A-Za-z’\']/g,''))+' ...</span>';}
      else h+=sp+'<span class="gqm">가림</span>';
    }else if(c.r==='접속사'){h+=sp+'<span class="gqc">'+esc(c.t)+'</span>';}
    else h+=sp+'<span class="gqh">'+esc(c.t)+'</span>';
  });
  return h+'</div>';
}
function gqHtml(){
  var s=C.s;if(!s.gq)return '';gqInit();var h='';
  var sk=s.ch.filter(function(c){return c.r!=='수식어'&&c.r!=='접속사';});
  h+='<div class="card" style="margin-top:10px"><p class="ask">'+(C.fmOk?'뼈대 확인 완료':'꾸밈말을 가렸어요. 이 뼈대는 누구와 닮은꼴일까요?')+'</p>'+gqSent(-1);
  if(!C.fmOk){
    h+='<div class="gqf">'+FMS.map(function(f,i){return '<button class="opt gqo'+((C.bk&&C.bk['f'+(i+1)])?' bad':'')+'" data-act="xq" data-t="fm" data-v="'+(i+1)+'"><b>'+f[0]+'</b> '+f[1]+'<span class="gqko">'+f[2]+'</span><span class="gqfo">'+f[3]+'</span></button>';}).join('')+'</div>';
  }else{
    var f=FMS[s.gq.fm-1];
    h+='<p class="msg ok"><b>'+f[0]+'</b> · '+f[3].split(' · ')[0]+'<br>'+sk.map(function(c,i){return esc(c.t)+' <span class="arr">↔</span> '+esc(f[4][i]||'');}).join('<br>')+'</p>';
  }
  h+='</div>';
  if(!C.fmOk)return h;
  s.gq.cl.forEach(function(x){
    var q=C.cq[x.ci],c=s.ch[x.ci];
    h+='<div class="card" style="margin-top:10px"><p class="ask">'+(q.s?'절 확인 완료':'테이프를 뗐어요. 이건 어떤 절일까요?')+'</p>'+gqSent(x.ci);
    if(!q.k){
      h+='<div class="qopts">'+['명사절','형용사절','부사절'].map(function(k){return '<button class="opt'+((C.bk&&C.bk[x.ci+k])?' bad':'')+'" data-act="xq" data-t="kind" data-ci="'+x.ci+'" data-v="'+k+'">'+k+'</button>';}).join('')+'</div>';
    }else if(!q.s){
      h+='<p class="msg ok">'+x.kind+' 맞아요. 어떤 종류일까요?</p><div class="qopts">'+SUBS[x.kind].map(function(k){return '<button class="opt'+((C.bk&&C.bk[x.ci+'s'+k])?' bad':'')+'" data-act="xq" data-t="sub" data-ci="'+x.ci+'" data-v="'+k+'">'+k+'</button>';}).join('')+'</div>';
    }else{
      h+='<p class="msg ok">'+x.kind+' · '+x.sub+'</p>';
    }
    h+='</div>';
  });
  return h;
}
