"""
ID: xknxkn1
LANG: PYTHON3
TASK: friday
"""

f=open("friday.in",'r')

data=f.read()
print(data)
nyear=int(data)
print(nyear)

def dayinmonth(year,month):
    return 31

daystoday=0

for i in range(nyear):
    year=i+1900
    print(year)

    for j in range(1,13):
        nday=dayinmonth(year,j)
        daystr="Month"+str(j)+":"
        for k in range(1,nday+1):
            daystoday+=1
            week=daystoday%7+1
            daystr+=str(k)+"W"+str(week)+" "
        print(daystr)

outstr=""

with open("friday.out",'w') as fw:
    for i in range(7):
        outstr+=str(weeks[i])+" "
    print(outstr)
    fw.write(outstr)



