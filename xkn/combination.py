from itertools import combinations

def connected(lines,line):
    for ln in lines:
        if ln[0] in line or ln[1] in line:
            return True
    return False

def combsk(S,k):
    n=len(S)
    result=[]
    for i in range(n-k+1):
        curS=S[i]
        if k>1:
            newS=S[i+1:]
            Comb=combsk(newS,k-1)
            for item in Comb:
                if not connected(item,curS):
                    item.insert(0,curS)
                result.append(item)
        else:
            result.append([curS])
    return result

holes=[1,2,3,4]
lcs=list(combinations(holes,2))
lines=list(map(list,lcs))
print("lines",lines)

K=int(len(holes)/2)
combrs=combsk(lines,K)
combes=[]
for comb in combrs:
    if len(comb)==K:
        combes.append(comb)
print("-------combrs",combes)

# divid and conquer
