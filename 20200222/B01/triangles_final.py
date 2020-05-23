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
        maxy=max(col)
        miny=min(col)
        maxx=max(row)
        minx=min(row)
        print("xrange yrange",(minx,maxx),(miny,maxy))
        py=maxy-y
        ny=y-miny
        px=maxx-x
        nx=x-minx
        area4=[py*px,py*nx,nx*ny,ny*px]
        print("area4",area4)
        areabig=max(area4)
        print("areabig",areabig)
        areas.append(areabig)
print("areas",areas)

#result handling
output=max(areas)
outstr=str(output)

with open("triangles.out",'w') as fw:
    outstr+="\n"
    print(outstr)
    fw.write(outstr)