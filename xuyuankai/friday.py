"""
ID: mythica2
LANG: PYTHON3
TASK: friday
"""
f = open('friday.in','r')
data = f.read()
yearnum = int(data)
print(yearnum)
def leap(year):
    leap = False
    if year%4 == 0 and year%100 != 0:
        leap = True
    if year%400 == 0:
        leap = True
    return leap
def leapcal(year,month):
    m=[31,28,31,30,31,30,31,31,30,31,30,31]
    dim = m[month-1]
    if month == 2 and leap(year):
        dim = 29
    return dim
days = 0
res = [0,0,0,0,0,0,0]
for i in range(yearnum):
    year = 1900+i
    for month in range(1,13):
        daynum = leapcal(year,month)
        for day in range(1,daynum+1):
            days += 1
            week = days%7+1
            if day == 13:
                res[week-1] += 1
print(res)
resstr = str(res[6])
with open('friday.out','w') as fw:
    for i in range(6):
        resstr += ' '+str(res[i])
    resstr += '\n'
    fw.write(resstr)