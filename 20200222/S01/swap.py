"""
ID: xknxkn
LANG: PYTHON3
TASK: swap
"""
import time
starttime = time.clock()

#i1nput formating
f=open("swap.in",'r')

L1=list(map(int,f.readline().strip().split(" ")))
N=L1[0]
M=L1[1]
K=L1[2]
print("N,K",N,M,K)

LRs=[]
for i in range(M):
    L=list(map(int,f.readline().strip().split(" ")))
    LRs.append(L)
print("LRs",LRs)

#simulation 
cows=list(map(str,range(1,N+1)))
#print(cows)

def reverse(start,end):
    global cows
    slen=end-start+1
    swaplen=int(slen/2)
    for i in range(swaplen):
        temp=cows[i+start-1]
        cows[i+start-1]=cows[end-1-i]
        cows[end-1-i]=temp

cowsin=cows.copy()
repeat=0
repeatfound=0
for i in range(K):
    for j in range(M):
        LR=LRs[j]
        reverse(LR[0],LR[1])
    repeat+=1
    print("i",i,cows)
    if cowsin==cows:
        repeatfound=1
        print("repeat",repeat)
        break

print("cows",cows)
if repeatfound==1:
    KM=K%repeat
    for j in range(M):
        LR=LRs[j]
        reverse(LR[0],LR[1])
print("result cows",cows)

outstr=""
with open("swap.out",'w') as fw:
    for i in range(N):
        outstr+=cows[i]
        outstr+="\n"
    print(outstr)
    fw.write(outstr)

endtime = time.clock()

print("time used", endtime-starttime)
