import json,sys
R={"1":([["I","s"],["sleep","v"]],""),"2":([["I","s"],["am","v"],["happy","c"]],"I = happy"),"3":([["I","s"],["like","v"],["apples","o"]],"I ≠ apples"),"4":([["I","s"],["give","v"],["him","io"],["a book","do"]],"him ≠ a book"),"5":([["I","s"],["make","v"],["him","o"],["happy","oc"]],"him = happy")}
def mk(en,key,f,me,merel,easy,notes):
    ref,rr=R[f[0]]
    return {"en":en,"key":key,"form":f,"ref":ref,"refrel":rr,"me":me,"merel":merel,"easy":easy,"notes":notes}
def save(name,items):
    for it in items:
        assert "".join(c[0] for c in it["me"]).replace(" ","")==it["en"].replace("[[","").replace("]]","").replace(" ",""),(name,it["en"])
    json.dump(items,open(name+".json","w",encoding="utf-8"),ensure_ascii=False)
