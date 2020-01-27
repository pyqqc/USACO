"""
ID: xknxkn1
LANG: PYTHON3
TASK: palsquare
"""

f=open("palsquare.in",'r')

B=int(f.readline().strip())
print(B)

def getBaseB(number):
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

outstr=""
for i in range(300):
    nBs=getBaseB((i+1)**2)
    if ifpal(nBs):
        outstr+=getBaseB(i+1)+" "+nBs+"\n"

with open("palsquare.out",'w') as fw:
    print(outstr)
    fw.write(outstr)

