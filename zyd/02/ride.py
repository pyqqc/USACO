"""
ID: sheep431
LANG: PYTHON3
TASK: ride
"""
Plist = open("ride.in","r")
Glist = open("ride.out","w")

line1 = Plist.readline()
line2 = Plist.readline()
print(line1)
print(line2)
p = 1
for c in line1[0:len(line1)-1]:
	#print(c)
	#print(ord(c))
	pp = ord(c)-ord("A") + 1
	print(pp)
	p = p * pp


line1p = p % 47
print(line1p)

p = 1
for c in line2[0:len(line2)-1]:
	#print(c)
	#print(ord(c))
	pp = ord(c)-ord("A") + 1
	print(pp)
	p = p * pp


line2p = p % 47
print(line2p)

if line1p == line2p:
	Glist.write("GO\n")
else:
	Glist.write("STAY\n")
Glist.close()




