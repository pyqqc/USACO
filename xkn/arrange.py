def perm(lst):
    if len(lst) <= 1:  # 如果当前lst长度为1，停止递归，返回
        return [lst]
    result = []
    for i in range(len(lst)):
        s = lst[:i]+lst[i+1:]  # 每一次拿出一个元素
        p = perm(s)  # 得到剩下元素的全排列
        for x in p:
            result.append(lst[i:i+1] + x)  # 将该元素插到剩下元素全排列的各个列表的前面
    print("r",result)
    print('\n')
    return result

def permall(lst):
    if len(lst) <= 1:  # 如果当前lst长度为1，停止递归，返回
        return [lst]
    result = []
    for i in range(len(lst)):
        p = perm(lst)  # 得到剩下元素的全排列
        for x in p:
            result.append(lst[i:i+1] + x)  # 将该元素插到剩下元素全排列的各个列表的前面
    print("r",result)
    print('\n')
    return result



a=['a','b','c']

p=permall(a)

print(p)