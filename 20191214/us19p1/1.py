"""
ID: 
LANG: PYTHON3
TASK: gymnastics
"""
ccn=0

fin = open('gymnastics.in','r')
kn=fin.readline().strip().split(" ")
K=int(kn[0])
N=int(kn[1])

print("K,N",K,N)

trains=[]

for k in range(K):
    row=fin.readline().strip().split(" ")
    trains.append(list(map(int,row)))
print(trains)

def getVpairs(testid):
    global trains
    cowrankrec=trains[testid]
    vp=[]
    for i in range(N):
        for j in range(i+1,N):
            crpair=[cowrankrec[j],cowrankrec[i]]
            vp.append(crpair)
    return vp

def contra(a,b):
    if a[0]==b[1] and a[1]==b[0]:
        return 1
    elif a[0]==b[0] and a[1]==b[1]:
        return 2
    else:
        return 0
 
vps=[]
for k in range(K):
    vp=getVpairs(k)
    for vpe in vp:
        vps.append(vpe)

print(vps)

goodcts=[]

for v in range(len(vps)):
    for m in range(len(vps)):
        val=contra(vps[v],vps[m])
        if val==1:
            goodct=[]
            break
        else:
            goodct=vps[v]
    if goodct !=[]:
        if goodct not in goodcts:
            goodcts.append(goodct)

print(goodcts)
ccn=len(goodcts)
print(ccn)

with open('gymnastics.out','w') as fw:
    fw.write(str(ccn))
    fw.write('\n')