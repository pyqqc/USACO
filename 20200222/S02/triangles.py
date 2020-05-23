"""
ID: xknxkn
LANG: PYTHON3
TASK: triangles
"""

#i1nput formating
f=open("triangles.in",'r')

N=int(f.readline())
print(N)

poss=[]
for i in range(N):
    pl=f.readline().strip()
    print(pl)
    pos=list(map(int,pl.split(" ")))
    print(pos)
    poss.append(pos)

poss.sort()
print(poss)
coldic={}
rowdic={}
for i in range(N):
    pos=poss[i]
    x=pos[0]
    y=pos[1]
    if x not in coldic:
        coldic[x]=[]
    if y not in rowdic:
        rowdic[y]=[]
    coldic[x].append(y)
    rowdic[y].append(x)
    coldic[x].sort()
    rowdic[y].sort()
print("coldic",coldic)
print("rowdic",rowdic)

def absp(line,p):
    res=[]
    for pos in line:
        res.append(abs(pos-p))
    return res

#test
tl=[1,3,5,7,9,100,-1,-5]
rl=absp(tl,5)
print("rl",rl)

#main process
areas=[]


for i in range(N):
    #find corner,cpos is current pos
    cpos=poss[i]
    x=cpos[0]
    y=cpos[1]
    print("i current pos is",i,(x,y))
    col=coldic[x]
    row=rowdic[y]
    if len(col)>1 and len(row)>1:
        print("cpos is a cross point,col,row",cpos,col,row)
        colabs=absp(col,y)
        rowabs=absp(row,x)
        area4sum=sum(colabs)*sum(rowabs)
        areas.append(area4sum)
print("areas",areas)

#result handling
output=sum(areas)
outstr=str(output)

with open("triangles.out",'w') as fw:
    outstr+="\n"
    print(outstr)
    fw.write(outstr)