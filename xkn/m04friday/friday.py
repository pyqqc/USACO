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

def isleapyear(year):
    isleapyear=False
    if year % 4 == 0 and year %100 != 0 :
        isleapyear=True
    if year % 400 == 0:
        isleapyear=True
    return isleapyear

def dayinmonth(year,month):
    dm=[31,28,31,30,31,30,31,31,30,31,30,31]
    dim=dm[month-1]
    if month == 2 and isleapyear(year):
        dim=29
    return dim

daystoday=0

week_13_num=[0,0,0,0,0,0,0]
for i in range(nyear):
    year=i+1900
    print(year)
    for month in range(1,13):
        nday=dayinmonth(year,month)
        daystr="Month"+str(month)+":"
        for day in range(1,nday+1):
            daystoday+=1
            week=daystoday%7+1
            daystr+=str(day)+"W"+str(week)+" "
            if day == 13:
                week_13_num[week-1]+=1
        print(daystr)




outstr=str(week_13_num[6])

with open("friday.out",'w') as fw:
    for i in range(6):
        outstr+=" "+str(week_13_num[i])
    outstr+="\n"
    print(outstr)
    fw.write(outstr)