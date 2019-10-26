"""
ID: mythica2
LANG: PYTHON3
TASK: milk2
"""
fin = open('milk2.in', 'r')
fout = open('milk2.out', 'w')
num = int(fin.readline().strip())
list_ = []
for i in range(10000000):
    list_.append(0)
for i in range(num):
    start, end = map(int, fin.readline().split())
    print(start, end)
    list_[start:end] = [1]*(end - start)
max_continuous = []; max_idle = []
continuous = 1; idle = 0; value = 0
started = False
for v in list_:
    if v == value and value == 0 and started == True:
        idle += 1
    if v == value and value == 1:
        continuous += 1
    else:
        if v == 1:
            value = 1
            started = True
            max_idle.append(idle)
            idle = 1
        if v == 0:
            value = 0
            max_continuous.append(continuous)
            continuous = 1
fout.write(str(max(max_continuous)) + ' ' + str(max(max_idle)) + '\n')
print(str(max(max_continuous)) + ' ' + str(max(max_idle)) + '\n')
fout.close()
