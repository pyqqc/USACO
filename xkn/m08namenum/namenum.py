"""
ID: xknxkn1
LANG: PYTHON3
TASK: namenum
"""
import itertools as it
f=open("namenum.in",'r')
fdic=open("dict.txt")

data=fdic.read()
names=data.split("\n")
print("names",len(names))
print(names[:10])

Num=f.readline().strip()
print(Num)

pkey={'A':2,'B':2,'C':2,'D':3,'E':3,'F':3,'G':4,'H':4,'I':4,'J':5,'K':5,'L':5,'M':6,'N':6,'O':6,'P':7,'R':7,'S':7,'T':8,'U':8,'V':8,'W':9,'X':9,'Y':9,'Z':0,'Q':0}

namenums=[]
namevalids=[]
for i in range(len(names)):
    name=names[i]
    namenum=""
    for c in name:
        namenum+=str(pkey[c])
    namenums.append(namenum)
    if namenum==Num:
        namevalids.append(name)

namevalids.sort()

if namevalids==[]:
    namevalids=["NONE"]

outstr=""

with open("namenum.out",'w') as fw:
    for nv in namevalids:
        outstr+=nv
        outstr+="\n"
    print(outstr)
    fw.write(outstr)

