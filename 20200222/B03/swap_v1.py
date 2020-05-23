"""
ID: xknxkn
LANG: PYTHON3
TASK: swap
"""

#i1nput formating
f=open("swap.in",'r')

L1=list(map(int,f.readline().strip().split(" ")))
N=L1[0]
K=L1[1]
#print("N,K",N,K)
L2=list(map(int,f.readline().strip().split(" ")))
L3=list(map(int,f.readline().strip().split(" ")))
A1=L2[0]
A2=L2[1]
B1=L3[0]
B2=L3[1]
#print("A1,A2,B1,B2",A1,A2,B1,B2)
ASLEN=int((A2-A1+1)/2)
BSLEN=int((B2-B1+1)/2)
AI1=A1-1
AI2=A2-1
BI1=B1-1
BI2=B2-1

cows=list(map(str,range(1,N+1)))
#print(cows)

for k in range(K):
    for i in range(ASLEN):
        head=AI1+i
        tail=AI2-i
        temp=cows[head]
        cows[head]=cows[tail]
        cows[tail]=temp
    for i in range(BSLEN):
        head=BI1+i
        tail=BI2-i
        temp=cows[head]
        cows[head]=cows[tail]
        cows[tail]=temp

outstr=""
with open("swap.out",'w') as fw:
    for i in range(N):
        fw.write(cows[i]+"\n")
    fw.write("\n")