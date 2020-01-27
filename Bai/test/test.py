"""
ID:Yanlin Bai
LANG:PYTHON3
TASK:test
"""
f=open("test.in","r")
data=f.read()
print(data)
DS=data.split(" ")
print(DS)
print(DS[0])
print(DS[1])
x=DS[0]
y=DS[1]
sum=int(x)+int(y)
print(sum)
f2=open("test.out","w")
ss=str(sum)
f2.write(ss+"\n")
f2.close()

