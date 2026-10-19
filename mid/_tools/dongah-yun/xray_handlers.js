  else if((a==='xw'||a==='xchk'||a==='xp'||a==='xk'||a==='xmu'||a==='xmt'||a==='xnext')&&C.ph==='X'){
    if(!C.xs)xNew();
    var xq=xSeq(s),xe=xq[C.xi],xn=xq[C.xi].n,xst=C.xs,xi=Number(t.getAttribute('data-i')),xv=xVerbs(xn);C.touched=1;
    if(a==='xnext'){if(xst.done){C.xi++;if(C.xi>=xq.length){C.ph='R';C.lastDrop=null;}else xNew();window.scrollTo(0,0);}}
    else if(!xst.done){
      if(a==='xw'&&xe.t==='verb'){
        if(xv.length===1){
          if(xi===xv[0]){xst.done=true;xst.fb=null;C.okc=(C.okc||0)+1;}
          else{xst.bad[xi]=1;xMiss(xi,'동사',xn);xst.fb='<b>'+esc(xn.ch[xi].t)+'</b> : 동사가 아니에요. 우리말로 "~하다, ~이다"로 끝나는 말을 찾아요.';}
        }else{var xk=xst.sel.indexOf(xi);if(xk>=0)xst.sel.splice(xk,1);else xst.sel.push(xi);xst.fb=null;}
      }
      else if(a==='xchk'&&xe.t==='verb'){
        var okAll=xst.sel.length===xv.length&&xst.sel.every(function(i){return xv.indexOf(i)>=0;});
        if(okAll){xst.done=true;xst.fb=null;C.okc=(C.okc||0)+1;}
        else{var ls=[];xst.sel.forEach(function(i){if(xv.indexOf(i)<0){xMiss(i,'동사',xn);ls.push('<b>'+esc(xn.ch[i].t)+'</b> : 동사가 아니에요.');}});
          if(!ls.length)ls.push('아직 더 있어요. 동사는 모두 '+xv.length+'개예요.');
          xst.fb=ls.join('<br>');xst.sel=[];}
      }
      else if(a==='xw'&&xe.t==='glue'){
        if(xi===xn.x.glue){xst.done=true;xst.fb=null;C.okc=(C.okc||0)+1;}
        else{xst.bad[xi]=1;xMiss(xi,'접속사',xn);xst.fb='<b>'+esc(xn.ch[xi].t)+'</b> : 접착제가 아니에요. 새 문장이 붙기 시작하는 곳을 찾아요.';}
      }
      else if(a==='xk'&&xe.t==='kind'){
        if(xi===xe.d.ans){C.okc=(C.okc||0)+1;C.xi++;xNew();window.scrollTo(0,0);}
        else{xst.bad[xi]=1;C.mist[1]++;logW({day:S.day,n:C.s.n,kind:'role',t:xn.ch[xe.d.ci].t,right:xe.d.opts[xe.d.ans],picked:xe.d.opts[xi]});xst.fb='아니에요. '+esc(xe.d.why||'덩어리 안을 다시 읽어 보세요.');}
      }
      else if(a==='xp'&&xe.t==='pat'){
        if(xi===xn.x.rounds[xe.r].fm-1){C.okc=(C.okc||0)+1;C.xi++;xNew();window.scrollTo(0,0);}
        else{xst.bad[xi]=1;C.mist[1]++;xst.fb='아니에요. 동사 뒤에 무엇이 오는지 보세요.';}
      }
      else if((a==='xmu'||a==='xmt')&&xe.t==='pair'){
        var skx=xSkel(xn,xe.r),PX=XPAT[xn.x.rounds[xe.r].fm-1];
        if(a==='xmu'){if(xst.md[xi]==null)xst.mu=xi;}else{if(!xst.mtd[xi])xst.mt=xi;}
        xst.fb=null;
        if(xst.mu!=null&&xst.mt!=null){
          var cx=xn.ch[skx[xst.mu]],tx=PX.tok[xst.mt];
          if(cx.r===tx[1]){xst.md[xst.mu]=xst.mt;xst.mtd[xst.mt]=1;xst.mu=null;xst.mt=null;C.okc=(C.okc||0)+1;if(Object.keys(xst.md).length===skx.length)xst.done=true;}
          else{xMiss(skx[xst.mu],tx[1],xn);xst.fb='짝이 아니에요. 같은 자리끼리 이어 보세요.';xst.mu=null;xst.mt=null;}
        }
      }
    }
  }
