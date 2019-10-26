"""
ID: mythica2
LANG: PYTHON3
TASK: transform
"""
fin = open('transform.in', 'r')
fout = open('transform.out', 'w')
size = int(fin.readline().strip())
arr1 = []
for i in range(size):
    row = fin.readline().strip()
    list_ = []
    for ln in row: list_.append(ln)
    arr1.append(list_)
print(arr1)
arr2 = []
for i in range(size):
    row = fin.readline().strip()
    list_ = []
    for ln in row: list_.append(ln)
    arr2.append(list_)
print(arr2)
def rotate_90(arr, size):
    new_arr = []
    for i in range(size):
        list_ = []
        for j in range(size):
            list_.append(arr[j][i])
        new_arr.append(list_[::-1])
    return new_arr
def mirror(arr, size):
    new_arr = []
    for i in range(size):
        new_arr.append(arr[i][::-1])
    return new_arr
def test_transformations(arr1, arr2, size):
    counter = 0
    for i in range(3):
        arr1 = rotate_90(arr1, size)
        counter += 1
        if arr1 == arr2: return counter
    arr1 = mirror(rotate_90(arr1, size), size)
    if arr1 == arr2: return 4
    for i in range(3):
        arr1 = rotate_90(arr1, size)
        if arr1 == arr2: return 5
    arr1 = mirror(rotate_90(arr1, size), size)
    if arr1 == arr2: return 6
    return 7
fout.write(str(test_transformations(arr1, arr2, size)) + '\n')
fout.close()
