"""
ID: xknxkn
LANG: PYTHON3
TASK: breedflip
"""

#i1nput formating
f=open("breedflip.in",'r')

N=int(f.readline())
print(N)

A=f.readline().strip()
B=f.readline().strip()
print("A",A)
print("B",B)

difs=""
for i in range(N):
    if A[i]!=B[i]:
        difs+='1'
    else:
        difs+='0'
print("difs",difs)
dcs=difs.split("0")
print("dcs",dcs)
flipnum=0
for dc in dcs:
    if dc !='':
        flipnum+=1
outstr=str(flipnum)

with open("breedflip.out",'w') as fw:
    outstr+="\n"
    print(outstr)
    fw.write(outstr)
