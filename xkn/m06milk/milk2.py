"""
ID: xknxkn1
LANG: PYTHON3
TASK: milk2
"""
#i1nput formating
f=open("milk2.in",'r')

N=int(f.readline())
print(N)

timesds=[]
for i in range(N):
    tl=f.readline()
    tse=list(map(int,tl.split(" ")))
    print(tse)
    timesds.append(tse)

timesds.sort()
print(timesds)

#global veriables
#functionsm
def mergeMilktime(mktimes,milksch):
    if mktimes==[]:
        mktimes.append(milksch)
    else:
        N=len(mktimes)
        #mktimes.sort()
        for i in range(N):
            mktime=mktimes[i]
            start=milksch[0]
            end=milksch[1]
 #           print("start end",start,end)
 #           print("milktime segment",mktime[0],mktime[1])
 #           print("mktimes",mktimes)
            if start <mktime[0] and end <mktime[0]:
 #               print("left out,append")
                mktimes.append(milksch)
            elif start >mktime[1] and end >mktime[1]:
                if i == N-1:
 #                   print("right of last seg,append")
                    mktimes.append(milksch)
                else:
                    continue
            elif start <mktime[0] and end >mktime[0] and end <mktime[1]:
                mktime[0]=start
            elif start <mktime[0] and end >mktime[0] and end >mktime[1]:
                mktime[0]=start
                mktime[1]=end
            elif start >mktime[0] and end <mktime[1]:
                pass
            elif start >mktime[0] and end >mktime[1]:
                mktime[1]=end

#main process
mktime1s=[]
for milksche in timesds:
    mktime1s.sort()
    mergeMilktime(mktime1s,milksche)
#print("mktimes",mktime1s)
mktresult=mktime1s

mktlens=[]
nmktlens=[]
for i in range(len(mktresult)):
    mktrst=mktresult[i]
    mktlens.append(mktrst[1]-mktrst[0])
    if i < len(mktresult)-1:
        nextmktrst=mktresult[i+1]
        nmktlens.append(nextmktrst[0]-mktrst[1])
print("mktlens",mktlens)
print("nmktlens",nmktlens)


#result handling
lct=max(mktlens)
if nmktlens == []:
    lit=0
else:
    lit=max(nmktlens)

outstr=str(lct)+" "+str(lit)

#912_184

with open("milk2.out",'w') as fw:
    outstr+="\n"
    print(outstr)
    fw.write(outstr)