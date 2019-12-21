"""
ID: 
LANG: PYTHON3
TASK: whereami
"""
answer=0

fin = open('whereami.in','r')
N=int(fin.readline().strip())
print(N)
colorstr=fin.readline().strip()
print(colorstr)

for tlen in range(1,N):
    print("tlen=",tlen)
    for tstart in range(0,N-tlen+1):
        template=colorstr[tstart:tlen+tstart]
        print(template)
        csspl=colorstr.split(template)
        csspll=len(csspl)
        print(csspll)
        if csspll >2:
            answer=0
            break
        else:
            answer=tlen
    if answer !=0:
        break

print("answer is ",answer)

with open('whereami.out','w') as fw:
    fw.write(str(answer))
    fw.write('\n')
