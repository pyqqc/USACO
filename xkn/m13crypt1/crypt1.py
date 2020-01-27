"""
ID: xknxkn1
LANG: PYTHON3
TASK: crypt1
"""

f=open("crypt1.in",'r')

N=int(f.readline().strip())
dsetstr=f.readline().strip().split(" ")
dset=list(map(int,dsetstr))
dset.sort()
dsetstr=list(map(str,dset))
print("N,dsetstr,dset",N,dsetstr,dset)


allgood=[]
line1=[0,0,0,0]
line2=[0,0]
line3=[0,0,0,0]
line4=[0,0,0,0]
line5=[0,0,0,0]

def charinset(charstr,charset):
    chars=list(charstr)
    for char in chars:
        if char not in charset:
            return False
    return True

def goodmultple(line1,line2):
    global allgood
    l1str="".join(list(map(str,line1)))
    l2str="".join(list(map(str,line2)))
#    print(l1str+"x"+l2str)
    l1int=int(l1str)
    l2int=int(l2str)
    l3int=l1int*line2[1]
    l3str=str(l3int)
    if len(l3str)>3:
#        print("l3>3")
        return 3
    if charinset(l3str,dsetstr)==False:
        return 1
    l4int=l1int*line2[0]
    l4str=str(l4int)
    if len(l4str)>3:
#        print("l4>3")
        return 4
    if charinset(l4str,dsetstr)==False:
        return 1
    l5int=l1int*l2int
    l5str=str(l5int)
 
 #   print(l5str)
    if len(l5str)>4:
 #       print("len5>5")
        return 5
    if charinset(l5str,dsetstr)==False:
        return 1

 #   print("good")
#   print("\n"+" "+l1str+"\n"+"   "+l2str+"\n"+"-----"+"\n"+" "+l3str+"   "+"\n"+""+l4str+"\n"+"....."+"\n"+l5str)
    allgood.append(l1str+" "+l2str)
    return 0

line1=[2,2,2]
line2=[2,2]

line1s=[]
for i in range(N):
    for j in range(N):
        for k in range(N):
                line1[0]=dset[i]
                line1[1]=dset[j]
                line1[2]=dset[k]
#                print(line1)
                line1s.append(line1.copy())

line2s=[]
for i in range(N):
    for j in range(N):
        line2[0]=dset[i]
        line2[1]=dset[j]
#        print(line2)
        line2s.append(line2.copy())

#print("line1s",line1s)
#print("line2s",line2s)


def searchall():
    ress=[]
    for i in range(len(line1s)):
        for j in range(len(line2s)):
            line1=line1s[i]
            line2=line2s[j]
            res=goodmultple(line1,line2)
            if res == 0:
                ress.append([line1,line2])
            elif res == 1:
                continue
    return ress

ress=searchall()
result=len(ress)
#print(ress)
outstr=str(result)+"\n"
with open("crypt1.out",'w') as fw:
    print(outstr)
    fw.write(outstr)
