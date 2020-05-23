"""
ID: xknxkn1
LANG: PYTHON3
TASK: wormhole
"""
from itertools import combinations

f=open("wormhole.in",'r')

N=int(f.readline().strip())

poss=[]
pxs=[]
for i in range(N):
    pos=list(map(int,f.readline().strip().split(" ")))
    poss.append(pos)
    if pos[0] not in pxs:
        pxs.append(pos[0])
#print("N,poss",N,poss)

pxs.sort()
maxx=pxs[-1]

#print("maxx",maxx)
print("pxs",pxs)

# for TEST
a=poss[0]
b=poss[1]
c=poss[2]
d=poss[3]

#pair=[[a,b],[c,d]]
#pair=[[a,d],[b,c]]
#pair=[[a,c],[b,d]]

def connected(lines,line):
    for ln in lines:
        if ln[0] in line or ln[1] in line:
            return True
    return False

def combsk(S,k):
    n=len(S)
    result=[]
    for i in range(n-k+1):
        curS=S[i]
        if k>1:
            newS=S[i+1:]
            Comb=combsk(newS,k-1)
            for item in Comb:
                if not connected(item,curS):
                    item.insert(0,curS)
                result.append(item)
        else:
            result.append([curS])
    return result

holes=poss
lcs=list(combinations(holes,2))
lines=list(map(list,lcs))

K=int(len(holes)/2)
combrs=combsk(lines,K)
combes=[]
for comb in combrs:
    if len(comb)==K:
        combes.append(comb)
#print("-------combrs",combes)
pairs=combes

# True: pair will loop
# False:pair will not loop
def travelsim(startp,pair):
    curp=startp
    cnt=0
    while True:
        cnt+=1
#        print("cnt1 curp",cnt,curp)
#        print("pair",pair)
        for pr in pair:
            if curp in pr:
                pdx=pr.index(curp)
                curp=pr[(pdx+1)%2].copy()
#                print("pass hole")
                break
        cnt+=1
#        print("cnt2 curp",cnt,curp)

        pxi=pxs.index(curp[0])
        if pxi == len(pxs)-1:
            curp[0]+=1
        else:
            curp[0]=pxs[pxi+1]

        cnt+=1
 #       print("cnt3 curp",cnt,curp)
        if curp ==  startp:
 #           print("stuck")
            return True
        if curp[0]>maxx:
 #           print("outside")
            return False

def ifloopair(pair):
    for pos in poss:
        tsr=travelsim(pos,pair)
 #       print("tsr",tsr)
        if tsr==True:
            return True
    return False
result=0

#ifpr=ifloopair(pair)
#print("ifpr",ifpr)
print("pairs,len",pairs,len(pairs))

for pair in pairs:
    print("pair",pair)
    ifpr=ifloopair(pair)
    print("ifpr",ifpr)
    if ifpr == True:
        result+=1

print("result",result)
outstr=str(result)+"\n"
with open("wormhole.out",'w') as fw:
    print(outstr)
    fw.write(outstr)
