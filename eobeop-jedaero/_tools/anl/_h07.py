import json,sys
REF={"1":([["I","s"],["sleep","v"]],""),"2":([["I","s"],["am","v"],["happy","c"]],"I = happy"),"3":([["I","s"],["like","v"],["apples","o"]],"I ≠ apples"),"4":([["I","s"],["give","v"],["him","io"],["a book","do"]],"him ≠ a book"),"5":([["I","s"],["make","v"],["him","o"],["happy","oc"]],"him = happy")}
def it(en,key,f,me,merel,easy,notes):
    r,rr=REF[f]
    return {"en":en,"key":key,"form":f+"형식","ref":r,"refrel":rr,"me":me,"merel":merel,"easy":easy,"notes":notes}
def save(name,items):
    json.dump(items,open('/home/claude/via/eobeop-jedaero/_tools/anl/'+name+'.json','w'),ensure_ascii=False)
