"""
ID: mythica2
LANG: PYTHON3
TASK: crypt1
"""
cin = open('crypt1.in','r').read().strip()
total = int(cin.split('\n')[0])
numlist = []
num1 = ''
num1l = []
num2 = []
num2l = []
p1 = 0
p2 = 0
p3 = 0
p1l = []
p2l = []
p3l = []
res = 0
r = 0
for a in range(len(cin.split('\n')[1].split(' '))):
    numlist.append(cin.split('\n')[1].split(' ')[a])
print(total)
print(numlist)
for b in range(len(numlist)):
    for c in range(len(numlist)):
        for d in range(len(numlist)):
            num1 += numlist[b]
            num1 += numlist[c]
            num1 += numlist[d]
            num1l.append(int(num1))
            num1 = ''
print(num1l)
for e in range(len(numlist)):
    for f in range(len(numlist)):
        num2.append(int(numlist[e]))
        num2.append(int(numlist[f]))
        num2l.append(num2)
        num2 = []
print(num2l)
for g in range(len(num1l)):
    for h in range(len(num2l)):
        p1 = str(num1l[g]*num2l[h][1])
        p2 = str(num1l[g]*num2l[h][0])
        p3 = str(int(p1)+(int(p2)*10))
        p1l.append(p1)
        p2l.append(p2)
        p3l.append(p3)
print(p1l)
print(p2l)
print(len(p3l[0]))
for i in range(len(p1l)):
    for j in range(len(p1l[i])):
        print(i,j)
        if (p1l[i][j] in numlist) == True and len(p1l[i]) == 3:
            r += 1
    for k in range(len(p2l[i])):
        print(i,k)
        if (p2l[i][k] in numlist) == True and len(p2l[i]) == 3:
            r += 1
    for l in range(len(p3l[i])):
        print(i,l)
        if (p3l[i][l] in numlist) == True and len(p3l[i]) == 4:
            r += 1
    if r == 10:
        res += 1
    r = 0
print(res)
with open('crypt1.out','w') as cw:
    cw.write(str(res))
    cw.write('\n')
