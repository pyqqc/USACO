"""
ID: sheep100
LANG: PYTHON3
TASK: triangles
"""
#N = 0
#3 <= N <= 100

f = open("triangles.in",'r')

xvalue = 0
N = int(f.readline().strip())
#NS = list(map(int,f.readline().strip()))


poss = []
for n in range(N):
	NS = list(map(int,f.readline().strip()))
	poss.append(NS)

poss.sort()
print(poss)
#poss[0]/poss[-1]
poss0 = poss[0]
poss1 = poss[-1]
x1 = poss0[0]
y1 = poss0[1]
x2 = poss1[0]
y2 = poss1[1]

xvalue = x2 - x1
yvalue = y2 - y1
area = xvalue*yvalue/2
outputarea = area *2
outstr = str(outputarea)

with open("triangles.out",'w') as fw:
	outstr += "\n"
	print(outstr)
	fw.write(outstr)

