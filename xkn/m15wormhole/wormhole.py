"""
ID: xknxkn1
LANG: PYTHON3
TASK: wormhole
"""
from itertools import combinations,product
import sys

f=open("wormhole.in",'r')

N=int(f.readline().strip())

poss=[]
pxs=[]
posyss=[]
for i in range(N):
    pos=list(map(int,f.readline().strip().split(" ")))
    poss.append(pos)
    if pos[0] not in pxs:
        pxs.append(pos[0])
poss.sort()

#pxs所有点的x值从小到大排列
pxs.sort()
maxx=pxs[-1]
#print("maxx",maxx)
#print("pxs",pxs)

#有相同y值的点统一放在posds
posds=[]
for pos in poss:
    posyss.append([pos])
for pos in poss:
    for posys in posyss:
        posy=posys[-1]
        if posy[1]==pos[1]:
            posys.append(pos)
for i in range(N):
    posys=posyss[i]
    if len(posys)>2:
        posds.append(poss[i])
#print("posds",posds)
PDN=len(posds)

#没有相同y值的点放在posrs
posrs=poss.copy()
for posd in posds:
    posrs.remove(posd)
#print("posrs",posrs)
PRN=len(posrs)
#a=poss[0]
#b=poss[1]
#c=poss[2]
#d=poss[3]
#pair=[[a,b],[c,d]]
#pair=[[a,d],[b,c]]
#pair=[[a,c],[b,d]]

#所有相同y轴的点先连线
lineys=list(combinations(posds,2))
#print("lineys",lineys,len(lineys))

# True: pair will loop.   pair is a group of line
# False:pair will not loop
def travelsim(startp,pair):
    curp=startp.copy()
#    print("cnt0,startp")
    cnt=0
    while True:
        cnt+=1
#        print("cnt1 curp",cnt,curp)
#        print("pair",pair)
        for pr in pair:
            if curp in pr:
                pdx=pr.index(curp)
                curp=pr[(pdx+1)%2].copy()
#                print("pass hole")
                break
        cnt+=1
#        print("cnt2 curp",cnt,curp)

        pxi=pxs.index(curp[0])
        if pxi == len(pxs)-1:
            curp[0]+=1
        else:
            curp[0]=pxs[pxi+1]

        cnt+=1
#        print("cnt3 curp",cnt,curp)
        if curp ==  startp:
#            print("stuck")
            return True
        if curp[0]>maxx:
#            print("outside")
            return False

# 
def ifloopair(pair):
    pc=pair.copy()
    for pos in poss:
        tsr=travelsim(pos,pc)
        if tsr==True:
            return True
    return False

#remove dot on lines
def removeylines(lines,dots):
    dres=dots.copy()
    rmdots=[]
    for line in lines:
        if line[0] not in rmdots:
            rmdots.append(line[0])
        if line[1] not in rmdots:
            rmdots.append(line[1])

    for rmdot in rmdots:
        if rmdot in dres:
            dres.remove(rmdot)
    return dres

# if lines1  lines2  the same 
def linessame(lines1,lines2):
    dlines1=[]
    dlines2=[]
#    print("lines1",lines1)
    for line1 in lines1:
        if line1[0] not in poss or line1[1] not in poss:
            return False
        lind0=poss.index(line1[0])
        lind1=poss.index(line1[1])
        linds=[lind0,lind1]
        linds.sort()
        dlines1.append(linds)
    dlines1.sort()
#    print("dlines1",dlines1)
    for line2 in lines2:
        lind0=poss.index(line2[0])
        lind1=poss.index(line2[1])
        linds=[lind0,lind1]
        linds.sort()
        dlines2.append(linds)
    dlines2.sort()
#    print("dlines2",dlines2)
    return dlines1 == dlines2

# pick up two dots from  dots left, pairs is the result of last pick up.  dots eft calculated form pairs which have lines outside
def combdots(dots,pairs):
    if pairs==[]:
        linec=list(combinations(dots,2))
#        print("linec,len",linec,len(linec))
        for line in linec:
            pairs.append([line])
        pairrsts=pairs
    else:
        pairrsts=[]
        for pair in pairs:
            #get the left dots
            ldots=removeylines(pair,dots)
#            print("ldots,n",ldots,len(ldots))
            linec=list(combinations(ldots,2))
            for line in linec:
                pair.append(line)
                pairrsts.append(pair)
#    print("pairrsts.len",pairrsts,len(pairrsts))
    return pairrsts

def combdotsK(dots,k):
    pairs=[]
    for i in range(k):
        pairs=combdots(dots,pairs)
    prsts=[]
    for pair in pairs:
        lsame=0
        for prst in prsts:
            if linessame(pair,prst)==True:
                lsame+=1
        if lsame == 0:
            prsts.append(pair)
#    print("prst len",prsts,len(prsts))
    return prsts

#TEST code
def test():
    lines=[[[0,0],[0,1]]]
#    print("poss",poss)
    posres=removeylines(lines,poss)
#    print("poss",poss)
#    print("posres",posres)

    lines1=[[[0, 0], [1, 0]], [[0, 1], [1, 1]]]
    lines2=[[[0, 1], [1, 1]], [[0, 0], [1, 0]]]
    linessame(lines1,lines2)

    dots=[[0,0],[0,1],[1,0],[1,1]]
    combdotsK(dots,1)
    combdotsK(dots,2)
    sys.exit(0)

def mainfuc():
    # main
    #K为y集合的直线数目
    K=int(PDN/2)
#    print("K",K)
    #从y集合选1个元素。2个元素，直至所有点都有不相交的线
    cmblineykres=[]
    print("posds,K",posds,K)
    for k in range(1,K+1):
        cmblineyk=combdotsK(posds,k)
#        print("--------------cmblineyk k",cmblineyk,k)
        #找牛loop的
        for cmblk in cmblineyk:
#            print("try cmblk",cmblk)
            if ifloopair(cmblk):
#                print("----------find one",cmblk)
                cmblineykres.append(cmblk)
    #cmblinekres 保存y集合所有stuck的线的组合1条，2条，3条.....
#    print("------------cmblineykres",cmblineykres)    
    return cmblineykres=[]

#main 
fms=mainfuc()
#double check if it is real loop
result=0
fmrs=[]
for fm in fms:
    if ifloopair(fm)==True:
        fmrs.append(fm)
        result+=1
print("fmrs",fmrs)
#print("result",result)
outstr=str(result)+"\n"
with open("wormhole.out",'w') as fw:
    print(outstr)
    fw.write(outstr)