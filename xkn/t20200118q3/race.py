"""
ID: xknxkn
LANG: PYTHON3
TASK: race

"""

f=open("race.in",'r')

MSC=list(map(int,f.readline().strip().split(" ")))
K=MSC[0]
N=MSC[1]
print("K",K)
print("N",N)

NS=[2]

for i in range(N):
    speed=int(f.readline().strip())
    NS.append(speed)
print(NS)


outstr=""
for speedlimit in NS:
    speeds=[1]
    poss=[]
    pos=0
    fin=False
    while fin == False:
        pos+=speeds[-1]
        poss.append(pos)
        print(poss)
        if pos >=K:
            print("finished")
            fin=True
            break
        avespeed=sum(speeds)/len(speeds)
        print("ave",avespeed)
        delta=avespeed-speedlimit
        print("delta",delta)
        if  0.5 > delta >= 0:
            speed=speeds[-1]+1
        elif 0.6 > delta >0.5:
            speed=speeds[-1]-1
        elif delta ==0.5:
            speed=speeds[-1]
        elif 0 > delta >-0.5:
            speed=speeds[-1]
        elif -0.5>delta > -1:
            speed=speeds[-1]+1
        else:
            speed=speeds[-1]

        print("next speed",speed)
        speeds.append(speed)
        print("speeds",speeds)

    avespeed=int(sum(speeds)/len(speeds))
    result=len(speeds)
    print("poss",poss)
    print("speeds",speeds)
    print("avespeed",avespeed)
    print("result",result)
    outstr+=str(result)+"\n"

outstr+="\n"
with open("race.out",'w') as fw:
    print(outstr)
    fw.write(outstr)