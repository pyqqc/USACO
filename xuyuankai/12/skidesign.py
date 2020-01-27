"""
ID: mythica2
LANG: PYTHON3
TASK: crypt1
"""
sin = open('skidesign.in','r').read().strip().split('\n')
print(sin)
tt = int(sin[0])
hills = list(map(int,sin[1:]))
hills.sort()
print(tt,hills)
h = 0
mod = []
money = []
ttmoney = 0
for b in range(100):
    h = b+1
    for a in range(tt):
        if hills[a] < h:
            mod.append((h - hills[a])**2)
        if h <= hills[a] and hills[a] <= h+17:
            mod.append(0)
        if hills[a] > h+17:
            mod.append((hills[a] - h-17)**2)
    for c in range(len(mod)):
        ttmoney += mod[c]
    money.append(ttmoney)
    mod = []
    ttmoney = 0
res = min(money)
print(money)
print(res)
with open('skidesign.out','w') as sw:
    sw.write(str(res)+'\n')

