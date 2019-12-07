"""
ID: xknxkn1
LANG: PYTHON3
TASK: beads
"""

f=open("beads.in",'r')

blen=int(f.readline())
print(blen)
beads=f.readline()
print(beads)

bcolors=[]

def cutbeads(cutpoint):
    global beads
    cutedbeads=[]
    for i in range(blen):
        pos=(i+cutpoint)%blen
        c=beads[pos]
        cutedbeads.append(c)
    print("cutedbeads:",cutedbeads)
    print("\n")
    return cutedbeads

def firsthcolor(ibeads):
    for b in ibeads:
        if b !="w":
            return b
        else:
            continue
    return "w"

def firsttcolor(ibeads):
    for i in range(1,len(ibeads)):
        if ibeads[-i] !="w":
            return ibeads[-i]
        else:        
            continue
    return "w"

def paintbeads(cbeads):
    hc=firsthcolor(cbeads)
    tc=firsttcolor(cbeads)
    for i in range(len(cbeads)):
        if cbeads[i]=="w":
            cbeads[i]=hc
        elif cbeads[i] !=hc:
            break

    for i in range(1,len(cbeads)):
        if cbeads[-i]=="w":
            cbeads[-i]=tc
        elif cbeads[-i] !=tc:
            break

    return cbeads


def countbeadscolor(cb):
    cblen=len(cb)
    headc=1
    tailc=0
    hcolor=cb[0]
    tcolor=cb[-1]
    for i in range(1,cblen):
        if hcolor == cb[i]:
            headc+=1
        else:
            break
    for i in range(1,cblen):
        if tcolor == cb[-i]:
            tailc+=1
        else:
            break
    if headc == cblen:
        return cblen
    count=headc+tailc
    print("hc tc count",headc,tailc,count)
    return count

#bp 0 means in front of first beads
#cb stands for cutted beads
#pb stands for pinted beads
for bp in range(blen):
    cb=cutbeads(bp)
    pb=paintbeads(cb)
    print("painted beads:",pb)
    num=countbeadscolor(pb)
    bcolors.append(num)
print(bcolors)
maxbeads=max(bcolors)
outstr=str(maxbeads)

with open("beads.out",'w') as fw:
    outstr+="\n"
    print(outstr)
    fw.write(outstr)
