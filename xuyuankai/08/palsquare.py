"""
ID: mythica2
LANG: PYTHON3
TASK: palsquare
"""
pin = open('palsquare.in','r')
B = int(pin.read())
sqlist = []
blist = []
nlist = []
nback = []
bback = []
flist = []
tlist = []
reslist = []
res = []
klist = []
res1 = []
res2 = []
res3 = []
res4 = []
res5 = []
res6 = []
resback = []
x = 0
y = B
z = 0
fstr = ''
for a in range(1,301):
    sqlist.append(a**2)
for c in range(300):
    x = sqlist[c]
    while True:
        if x < y:
            z = x
            nlist.append(z)
            break
        z = x%y
        nlist.append(z)
        x = int(x/y)
    for d in range(len(nlist)):
        nback.append(nlist[-d-1])
    blist.append(nback)
    bback.append(nlist)
    nlist = []
    nback = []
for e in range(300):
    if blist[e] == bback[e]:
        flist.append(blist[e])
        klist.append(e)
for f in range(len(flist)):
    for g in range(len(flist[f])):
        if flist[f][g] < 10:
            tlist.append(str(flist[f][g]))
        if flist[f][g] == 10:
            tlist.append('A')
        if flist[f][g] == 11:
            tlist.append('B')
        if flist[f][g] == 12:
            tlist.append('C')
        if flist[f][g] == 13:
            tlist.append('D')
        if flist[f][g] == 14:
            tlist.append('E')
        if flist[f][g] == 15:
            tlist.append('F')
        if flist[f][g] == 16:
            tlist.append('G')
        if flist[f][g] == 17:
            tlist.append('H')
        if flist[f][g] == 18:
            tlist.append('I')
        if flist[f][g] == 19:
            tlist.append('J')
    reslist.append(tlist)
    tlist = []
for h in range(len(reslist)):
    for i in range(len(reslist[h])):
        fstr += reslist[h][i]
    res.append(fstr)
    fstr = ''
for j in range(len(klist)):
    res2.append(str(klist[j]+1))
for l in range(len(res2)):
    x = int(res2[l])
    z = 0
    while True:
        if x < y:
            z = x
            res1.append(z)
            break
        z = x%y
        res1.append(z)
        x = int(x/y)
    for q in range(len(res1)):
        resback.append(res1[-q-1])
    res3.append(resback)
    resback = []
    res1 = []
print(res3)
for m in range(len(res3)):
    for n in range(len(res3[m])):
        if res3[m][n] < 10:
            res4.append(str(res3[m][n]))
        if res3[m][n] == 10:
            res4.append('A')
        if res3[m][n] == 11:
            res4.append('B')
        if res3[m][n] == 12:
            res4.append('C')
        if res3[m][n] == 13:
            res4.append('D')
        if res3[m][n] == 14:
            res4.append('E')
        if res3[m][n] == 15:
            res4.append('F')
        if res3[m][n] == 16:
            res4.append('G')
        if res3[m][n] == 17:
            res4.append('H')
        if res3[m][n] == 18:
            res4.append('I')
        if res3[m][n] == 19:
            res4.append('J')
    res5.append(res4)
    res4 = []
for o in range(len(res5)):
    for p in range(len(res5[o])):
        fstr += res5[o][p]
    res6.append(fstr)
    fstr = ''
with open('palsquare.out','w') as pw:
    for k in range(len(res)):
        pw.write(res6[k]+' '+res[k]+'\n')
