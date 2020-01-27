"""
ID: xknxkn1
LANG: PYTHON3
TASK: dualpal
"""

f=open("dualpal.in",'r')

NS=list(map(int,f.readline().strip().split(" ")))
N=NS[0]
S=NS[1]
print("N,S",N,S)

def getBaseB(number,B):
    nB=[]
    res=number
    while res != 0:
        rem=res%B
        res=res//B
        nB.append(rem)
    nB.reverse()
#
#    print(nB)
    nBs=""
    for num in nB:
        if num <10:
            nBs+=str(num)
        else:
            numord=(num-10)+ord('A')
            nBs+=chr(numord)
    return nBs

def ifpal(nBs):
    nBsl=list(nBs)
    temp=nBsl.copy()
    nBsl.reverse()
    if temp == nBsl:
        return True
    else:
        return False

n=0
outlist=[]
for s in range(S+1,100000):
    palN=0
    print("s is",s)
    for b in range(2,10+1):
        print("try base",b)
        nbs=getBaseB(s,b)
        if ifpal(nbs) == True:
            palN+=1
            print("nbs,s,b",nbs,s,b)
        if palN >=2:
            outlist.append(s)
            n+=1
            break
    print(n)
    if n>=N:
        break

outlist.sort()
print(outlist)

outstr="\n".join(list(map(str,outlist)))+"\n"

with open("dualpal.out",'w') as fw:
    print(outstr)
    fw.write(outstr)