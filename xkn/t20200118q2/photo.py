"""
ID: xknxkn
LANG: PYTHON3
TASK: photo

"""

f=open("photo.in",'r')

MSC=list(map(int,f.readline().strip().split(" ")))
N=MSC[0]
print("N",N)

words=f.readline().strip().split(" ")
data=list(map(int,words))
print(data)

ps=[]
for i in range(1,data[0]):
    tryi=data[0]-i
    ps.append(tryi)
    print("try",tryi)
    for j in range(1,len(data)+1):
        tgt=data[j-1]
        rst=tgt-ps[j-1]
        if rst<=0:
            print("wrong",rst)
            ps=[]
            break
        else:
            ps.append(rst)
        print(ps)
    if len(ps)==N:
        break
      
result=list(map(str,ps))
outstr=" ".join(result)

outstr+="\n"
with open("photo.out",'w') as fw:
    print(outstr)
    fw.write(outstr)