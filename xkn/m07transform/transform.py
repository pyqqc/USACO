"""
ID: xknxkn1
LANG: PYTHON3
TASK: transform
"""
#i1nput formating
f=open("transform.in",'r')

N=int(f.readline())
print(N)

SqIn=[]
for i in range(N):
    line=f.readline().strip()
    ll=list(line)
    SqIn.append(ll)
print(SqIn)

SqOut=[]
for i in range(N):
    line=f.readline().strip()
    ll=list(line)
    SqOut.append(ll)
print(SqOut)

def samesqrt(SqrIn,SqrOut):
    if SqIn == SqOut:
        print("same")
        return 7
    else:
        return 0

def rotation90(SqrIn,SqrOut):
    temp=[["."]*N for row in range(N)]
    for i in range(N):
        for j in range(N):
            temp[j][N-i-1]=SqrIn[i][j]
    if temp == SqrOut:
        return 1
    else:
        return 0
       
def rotation180(SqrIn,SqrOut):
    temp=[["."]*N for row in range(N)]
    temp1=[["."]*N for row in range(N)]
    for i in range(N):
        for j in range(N):
            temp1[j][N-i-1]=SqrIn[i][j]
    for i in range(N):
        for j in range(N):
            temp[j][N-i-1]=temp1[i][j]
    if temp == SqrOut:
        return 2
    else:
        return 0

def rotation270(SqrIn,SqrOut):
    temp=[["."]*N for row in range(N)]
    temp1=[["."]*N for row in range(N)]
    temp2=[["."]*N for row in range(N)]
    for i in range(N):
        for j in range(N):
            temp2[j][N-i-1]=SqrIn[i][j]
    for i in range(N):
        for j in range(N):
            temp1[j][N-i-1]=temp2[i][j]
    for i in range(N):
        for j in range(N):
            temp[j][N-i-1]=temp1[i][j]

    if temp == SqrOut:
        return 3
    else:
        return 0

def reflection(SqrIn,SqrOut):
    temp=[["."]*N for row in range(N)]
    for i in range(N):
        for j in range(N):
            temp[i][N-j-1]=SqrIn[i][j]
    if temp == SqrOut:
        return 4
    else:
        return 0

def combination(SqrIn,SqrOut):
    temp=[["."]*N for row in range(N)]
    for i in range(N):
        for j in range(N):
            temp[i][N-j-1]=SqrIn[i][j]
    
    temp1=[["."]*N for row in range(N)]
    for i in range(N):
        for j in range(N):
            temp1[j][N-i-1]=temp[i][j]
    if temp1 == SqrOut:
        return 5
    
    temp2=[["."]*N for row in range(N)]
    for i in range(N):
        for j in range(N):
            temp2[j][N-i-1]=temp1[i][j]
    if temp2 == SqrOut:
        return 5

    temp3=[["."]*N for row in range(N)]
    for i in range(N):
        for j in range(N):
            temp3[j][N-i-1]=temp2[i][j]
    if temp3 == SqrOut:
        return 5
    return 0

def nochange(SqrIn,SqrOut):
    if SqrIn == SqrOut:
        return 6
    else:
        return 0

def whichtransform(SqrIn,SqrOut):
    result=rotation90(SqIn,SqOut)
    if result!=0:
        return result
    result=rotation180(SqIn,SqOut)
    if result!=0:
        return result
    result=rotation270(SqIn,SqOut)
    if result!=0:
        return result
    result=reflection(SqIn,SqOut)
    if result!=0:
        return result
    result=combination(SqIn,SqOut)
    if result!=0:
        return result
    result=nochange(SqIn,SqOut)
    if result!=0:
        return result
    return 7

result=whichtransform(SqIn,SqOut)
print(result)

outstr=str(result)

with open("transform.out",'w') as fw:
    outstr+="\n"
    print(outstr)
    fw.write(outstr)