"""
ID: xknxkn1
LANG: PYTHON3
TASK: milk
"""

f=open("milk.in",'r')

NS=list(map(int,f.readline().strip().split(" ")))
N=NS[0]
M=NS[1]
print("N,M",N,M)

milkpnu=[]
for m in range(M):
    pnu=list(map(int,f.readline().strip().split(" ")))
    milkpnu.append(pnu)

print("milkpnu",milkpnu)
milkpnu.sort()
print("milkpnusort",milkpnu)

res=N
cost=0

for mpnu in milkpnu:
    mu=mpnu[1]
    price=mpnu[0]
    for m in range(mu):
        res-=1
        cost+=price
        if res==0:
            break
    if res==0:
        break
result=cost

outstr=str(result)+"\n"
with open("milk.out",'w') as fw:
    print(outstr)
    fw.write(outstr)