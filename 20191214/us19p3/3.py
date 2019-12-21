"""
ID: 
LANG: PYTHON3
TASK: lineup
"""
import itertools

answer="a beside b"

cows=["Bessie","Buttercup","Belinda","Beatrice","Bella","Blue","Betsy","Sue"]

fin = open('lineup.in','r')
N=int(fin.readline().strip())

cowplans=[]
for p in itertools.permutations(cows):
    cowplan=" ".join(p)
    cowplans.append(cowplan.split(" "))
print(cowplans)

rules=[]
for i in range(N):
    rulerawstr=fin.readline().strip().split(" ")
    rules.append([rulerawstr[0],rulerawstr[-1]])

print(rules)

def checkrule(cowplan,rule):
    rlidx=cowplan.index(rule[0])
#    print("rlidx",rlidx)
    if rlidx==0:
        if cowplan[1]==rule[1]:
            return True
        else:
            return False

    if rlidx==7:
        if cowplan[6]==rule[1]:
            return True
        else:
            return False
    
    if cowplan[rlidx-1]==rule[1] or cowplan[rlidx+1]==rule[1]:
        return True
    else:
        return False

def checkrulespass(cowplan):
    global rules
    for rule in rules:
        if checkrule(cowplan,rule)!=True:
            return False
    return True

goodplans=[]
for cowplan in cowplans:
    if checkrulespass(cowplan) == True:
        strcowplan=" ".join(cowplan)
        print(strcowplan)
        goodplans.append(" ".join(cowplan))
goodplans.sort()
print(goodplans[0])


print(answer)
with open('lineup.out','w') as fw:
    fw.write(answer)
    fw.write('\n')