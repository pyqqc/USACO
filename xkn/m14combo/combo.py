"""
ID: xknxkn1
LANG: PYTHON3
TASK: combo
"""

f=open("combo.in",'r')

N=int(f.readline().strip())
jcomb=list(map(int,f.readline().strip().split(" ")))
mcomb=list(map(int,f.readline().strip().split(" ")))
print("N,jcomb,mcomb",N,jcomb,mcomb)

combs=[]

digiall=["0"]*N
for j in jcomb:
    digiall[j-1]="1"
for m in mcomb:
    digiall[m-1]="1"
print(digiall)
digia=digiall.copy()

for i in range(N):
    if digiall[i]=="1":
        digia[i]="1"
        if N >=2:
            digia[i-1]="1"
        if N>=3:
            digia[i-2]="1"
        if N>=2:
            digia[(i+1)%N]="1"
        if N>=3:
           digia[(i+2)%N]="1"
print(digia)

jmrange=[]
for i in range(N):
    if digia[i]=="1":
        jmrange.append(i+1)

print(jmrange)

for i in jmrange:
    for j in jmrange:
        for k in jmrange:
            combs.append([i,j,k])

print(len(combs))

def distance(a,b):
    x=a-1
    y=b-1
    dis=abs(y-x)
    if dis<=N/2:
        return dis
    else:
        return N-dis

print(distance(1,2))
print(distance(2,1))
print(distance(48,50))
print(distance(50,48))
print(distance(1,50))
print(distance(2,50))
print(distance(3,50))
print(distance(49,1))
print(distance(48,1))
print(distance(47,1))


goodcomb=[]
print(combs[0:10])

for comb in combs:
    jmc=0
    mmc=0
    for i in range(3):
        key=comb[i]
        if distance(key,jcomb[i])<=2:
            jmc+=1
#           print("kg")
        if distance(key,mcomb[i])<=2:
            mmc+=1

    if jmc >=3 or mmc>=3:
#        print("good")
        goodcomb.append(comb)


print("goodcomb",goodcomb)
result=len(goodcomb)
outstr=str(result)+"\n"
with open("combo.out",'w') as fw:
    print(outstr)
    fw.write(outstr)
