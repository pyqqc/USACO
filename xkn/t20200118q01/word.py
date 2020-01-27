"""
ID: xknxkn
LANG: PYTHON3
TASK: word
"""

f=open("word.in",'r')

MSC=list(map(int,f.readline().strip().split(" ")))
N=MSC[0]
K=MSC[1]
print("N,K",N,K)

words=f.readline().strip().split(" ")

print(words)

outstr=""
chcout=0
for word in words:
    lw=len(word)
    print(word)
    if chcout==0:
        outstr+=word
        chcout+=lw
    else:
        tempp=chcout+lw
        print("tp",tempp)
        if tempp >K:
            outstr+="\n"+word
            chcout=lw
        else:
            outstr+=" "+word
            chcout+=lw

outstr+="\n"
with open("word.out",'w') as fw:
    print(outstr)
    fw.write(outstr)