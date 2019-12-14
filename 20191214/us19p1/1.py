"""
ID: 
LANG: PYTHON3
TASK: gymnastics
"""
ccn=0

fin = open('gymnastics.in','r')
kn=fin.readline().strip().split(" ")
K=int(kn[0])
N=int(kn[1])

print("K,N",K,N)

trains=[]

for k in range(K):
    row=fin.readline().strip().split(" ")
    trains.append(list(map(int,row)))
print(trains)


with open('gymnastics.out','w') as fw:
    fw.write(str(ccn))
    fw.write('\n')