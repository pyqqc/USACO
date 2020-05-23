"""
ID: sheep430
LANG: PYTHON3
TASK: triangles
"""
#N = 0
#3 <= N <= 100
#
f=open("triangles.in",'r')

N=int(f.readline())

poss = []
for i in range(N):
    pl = f.readline().strip()
    #print(pl)
    pos = list(map(int,pl.split(" ")))
    #print(pos)
    poss.append(pos)

poss.sort()
#print(poss)
#print(poss)

#poss[0]/poss[-1]
'''poss0 = poss[0]
poss1 = poss[-1]
x1 = poss0[0]
y1 = poss0[1]
x2 = poss1[0]
y2 = poss1[1]

xvalue = x2 - x1
yvalue = y2 - y1'''
'''
xlist = []
ylist = []
for n in range(N):
	possn = poss[n]
	x = possn[0]
	y = possn[1]
	xlist.append(x)
	ylist.append(y)
print(xlist)
print(ylist)
'''
s = 0
for i in range(N):
            for j in range(i+1,N):
                for k in range(j+1,N):
                	#if poss[i][0] == poss[j][0] and poss[j][1] == poss[k][1]:
                	x=(poss[i][0]*poss[j][1]+poss[j][0]*poss[k][1]+poss[k][0]*poss[i][1]-poss[i][0]*poss[k][1]-poss[j][0]*poss[i][1]-poss[k][0]*poss[j][1])
                	s=max(s,abs(x))
#print(s)
'''
x1 = 0
x2 = 0
x3 = 0
y1 = 0
y2 = 0
y3 = 0
baseline = 0
hyperline = 0
for n,m,l in range(N,N,N):
	x1 = xlist[n]
	y1 = ylist[n]
	x2 = xlist[m]
	y2 = ylist[m]
	x3 = xlist[l]
	y3 = ylist[l]
	if x1 == x2:
		if y2 == y3:
			baseline = x3 - x2
			hyperline = y1 - y2
			print(baseline)'''




outstr = str(s)

with open("triangles.out",'w') as fw:
	outstr += "\n"
	print(outstr)
	fw.write(outstr)