"""
ID: sheep430
LANG: PYTHON3
TASK: triangles
"""

#i1nput formating
f=open("swap.in",'r')

L1=list(map(int,f.readline().strip().split(" ")))
N=L1[0]
K=L1[1]
#print("N,K",N,K)
L2=list(map(int,f.readline().strip().split(" ")))
L3=list(map(int,f.readline().strip().split(" ")))
A1=L2[0] - 1#need to -1
A2=L2[1] - 1
B1=L3[0] - 1
B2=L3[1] - 1

cow = []
for cowcount in range(1,101):
	cow.append(cowcount)

cowcopy = cow[:]
print(cowcopy)
c = 0
while True:
	print("before A reverse,A2,A1",A2,A1,cow)
	for i in range(A2-A1-1):
		cow[A1+i],cow[A2-i] = cow[A2-i],cow[A1+i]
	print("after A reverse",cow)
	for ii in range(0,(B2-B1-1)):
		cow[B1+ii],cow[B2-ii] = cow[B2-ii],cow[B1+ii]
		c +=1
	if cow == cowcopy:
		break
print(c)




kk = K%c

while (kk > 0):
	for i in range(A2-A1-1):
		cow[A1+i],cow[A2-i] = cow[A2-i],cow[A1+i]
	for ii in range(0,(B2-B1-1)):
		cow[B1+ii],cow[B2-ii] = cow[B2-ii],cow[B1+ii]
	kk-= 1
print(cow)


with open("swap.out",'w') as fw:
	for n in range(N):
		outstr = str(cow[n])
		outstr += "\n"
		#print(outstr)
		fw.write(outstr)



