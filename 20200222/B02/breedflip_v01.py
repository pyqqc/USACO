"""
ID: xknxkn
LANG: PYTHON3
TASK: breedflip
"""

#i1nput formating
f=open("breedflip.in",'r')

N=int(f.readline())
print(N)

A=list(f.readline().strip())
B=list(f.readline().strip())
print("A",A)
print("B",B)

def flip(bl,start,blen):
    btemp=bl.copy()
    if start+blen >N:
        print("out of B range")
        return -1
    for i in range(blen):
        name=btemp[start+i]
        if name == 'G':
            btemp[start+i]='H'
        else:
            btemp[start+i]='G'
    return btemp

#function test
print("B",B)
newB=flip(B,2,3)
print("flib B,2,3")
print(newB)
newB=flip(B,5,2)
print("flib B,5,2")
print(newB)
newB=flip(B,6,2)
print("flib B,6,2")
print(newB)
print("B",B)
#main loop
difs=[]
for i in range(N):
    if A[i]!=B[i]:
        difs.append(1)
    else:
        difs.append(0)
print("difs",difs)




bflips=[1,2,3]
#result handling
output=min(bflips)
outstr=str(output)

with open("breedflip.out",'w') as fw:
    outstr+="\n"
    print(outstr)
    fw.write(outstr)