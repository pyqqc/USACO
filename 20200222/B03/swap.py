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
print("N,K",N,K)
L2=list(map(int,f.readline().strip().split(" ")))
L3=list(map(int,f.readline().strip().split(" ")))
A1=L2[0]
A2=L2[1]
B1=L3[0]
B2=L3[1]
print("A1,A2,B1,B2",A1,A2,B1,B2)

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
    reverse(A1,A2)
#    print("A1,A2",A1,A2,cows)
    reverse(B1,B2)
#    print("B2,B2",B1,B2,cows)
    repeat+=1
    print("i",i,cows)
    if cowsin==cows:
        repeatfound=1
        print("repeat",repeat)
        break

print("cows",cows)
if repeatfound==1:
    KM=K%repeat
    for i in range(KM):
        reverse(A1,A2)
        reverse(B1,B2)
print("result cows",cows)

outstr=""
with open("swap.out",'w') as fw:
    for i in range(N):
        outstr+=cows[i]
        outstr+="\n"
    print(outstr)
    fw.write(outstr)