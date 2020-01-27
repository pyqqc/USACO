"""
ID: xknxkn1
LANG: PYTHON3
TASK: barn1
"""

f=open("barn1.in",'r')

MSC=list(map(int,f.readline().strip().split(" ")))
M=MSC[0]
S=MSC[1]
C=MSC[2]
print("M,S,C",M,S,C)

stalls=["0"]*S
print(stalls)

for i in range(C):
    sn=int(f.readline().strip())
    print("sn",sn)
    stalls[sn-1]="1"
print(stalls)

barn="".join(stalls)
print("barn",barn)

def getMaxZero(onezeros):
    print("onezeros",onezeros)
    ozs=onezeros.split("1")
    print("ozs",ozs)
    ozlens=list(map(len,ozs))
    print("ozlens",ozlens)
    moz=max(ozlens)
    return moz

def nextbarn(barns,m):
    print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbarns,m",barns,m)
    if m==1:
        barn=barns[0]
        first=barn.find("1")
        last=barn.rfind("1")
        barn=barn[first:last+1]
        barns[0]=barn
    else:
        mzs=[]
        for barn in barns:
            print("barn",barn)
            mz=getMaxZero(barn)
            mzs.append(mz)
        print("mzs",mzs)
        mmzs=max(mzs)
        if mmzs==0:
            print("no more zero")
            return barns,-1
        mzsi=mzs.index(mmzs)
        barncut=barns[mzsi]
        print("barncut",barncut)
        bcs=barncut.split("0"*mmzs)
        bcs=[("0"*mmzs).join(bcs[0:-1]),bcs[-1]]
        print("bcs",bcs)
        barns.pop(mzsi)
        for bc in bcs:
            barns.append(bc)
        print("nextbarns",barns)
    return barns,1

barns=[]
barns.append(barn)

for m in range(1,M+1):
    barns,result=nextbarn(barns,m)
    if result==-1:
        break


barnlens=list(map(len,barns))
print("barnlens",barnlens)

result=sum(barnlens)
outstr=str(result)+"\n"
with open("barn1.out",'w') as fw:
    print(outstr)
    fw.write(outstr)