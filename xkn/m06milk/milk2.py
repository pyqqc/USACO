"""
ID: xknxkn1
LANG: PYTHON3
TASK: milk2
"""

#input formating
f=open("milk2.in",'r')

N=int(f.readline())
print(N)

timesds=[]
for i in range(N):
    tl=f.readline()
    tse=list(map(int,tl.split(" ")))
    print(tse)
    timesds.append(tse)
print(timesds)


#functions
#TBD





#main loop





#result handling
lct=900
lit=300

outstr=str(lct)+" "+str(lit)

with open("milk2.out",'w') as fw:
    outstr+="\n"
    print(outstr)
    fw.write(outstr)
