"""
ID: mythica2
LANG: PYTHON3
TASK: namenum
"""
ndict = open('dict.txt','r')
innum = open('namenum.in','r').readline().strip()
nlist = []
nnum = ''
numlist = []
ilist = []
for i in range(4617):
    nlist.append(ndict.readline().strip())
for a in range(4617):
    for b in range(len(nlist[a])):
        if nlist[a][b] == 'A' or nlist[a][b] == 'B' or nlist[a][b] == 'C':
            nnum += '2'
        if nlist[a][b] == 'D' or nlist[a][b] == 'E' or nlist[a][b] == 'F':
            nnum += '3'
        if nlist[a][b] == 'G' or nlist[a][b] == 'H' or nlist[a][b] == 'I':
            nnum += '4'
        if nlist[a][b] == 'J' or nlist[a][b] == 'K' or nlist[a][b] == 'L':
            nnum += '5'
        if nlist[a][b] == 'M' or nlist[a][b] == 'N' or nlist[a][b] == 'O':
            nnum += '6'
        if nlist[a][b] == 'P' or nlist[a][b] == 'R' or nlist[a][b] == 'S':
            nnum += '7'
        if nlist[a][b] == 'T' or nlist[a][b] == 'U' or nlist[a][b] == 'V':
            nnum += '8'
        if nlist[a][b] == 'W' or nlist[a][b] == 'X' or nlist[a][b] == 'Y':
            nnum += '9'
        if nlist[a][b] == 'Q' or nlist[a][b] == 'Z':
            nnum = ''
    numlist.append(nnum)
    nnum = ''
with open('namenum.out','w') as nw:
    try:
        for d in range(len(numlist)):
            if innum == numlist[d]:
                ilist.append(d)
        if ilist == []:
            nw.write('NONE'+'\n')
        else:
            for c in range(len(ilist)):
                nw.write(nlist[ilist[c]]+'\n')
    except:
        nw.write('NONE'+'\n')
        pass
