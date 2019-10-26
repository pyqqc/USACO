"""
ID: mythica2
LANG: PYTHON3
TASK: beads
"""
f = open('beads.in','r')
data = f.read()
dataln = data.split('\n')
b = dataln[1]
b += b
print(b)
m = 1
n = 2
mn = 1
nn = 1
pos = []
for i in range(1,len(b)-1):
    print('\n')
    if b[i] != 'w':
        while True:
            if i-m >= 0:
                if b[i-m] == b[i] or b[i-m] == 'w':
                    m += 1
                    mn += 1
                else:
                    break
            else:
                break
    else:
        while True:
            if i-m-1>=0:
                if b[i-1] == b[i-m-1] or b[i-m-1] == 'w':
                    m += 1
                    mn += 1
                else:
                    break
            else:
                break
    if b[i+1] != 'w':
        while True:
            if i+n >= len(b)-1:
                break
            elif b[i+1] == b[i+n] or b[i+n] == 'w':
                print(b[1+n])
                n += 1
                nn += 1
            else:
                break
    else:
        while True:
            if i+n+1 >= len(b)-1:
                break
            elif b[i+2] == b[i+n+1] or b[i+n+1] == 'w':
                if n<= len(b)-i-2:
                    n += 1
                    nn += 1
                else:
                    break
            else:
                break
    finalnum = mn+nn
    m = 1
    n = 2
    mn = 1
    nn = 1
    pos.append(finalnum)
    finalnum = 0
print(pos)
finalres = max(pos)
if finalres >= int(dataln[0]):
    finalres = int(finalres/2)
with open('beads.out','w') as fw:
    fw.write(str(int(finalres)))
    fw.write('\n')