import random
import time

x = lambda a: [a] if isinstance(a, int) else a
def merge(A, B):
    A, B = x(A), x(B)
    c = []
    indexA = 0
    indexB = 0
    while indexA != len(A) and indexB != len(B):
        if A[indexA] < B[indexB]:
            c.append(A[indexA])
            indexA += 1
        else:
            c.append(B[indexB])
            indexB += 1
    for indexA in range(indexA, len(A)):
        c.append(A[indexA])
    for indexB in range(indexB, len(B)):
        c.append(B[indexB])
    return c

def mergeSort(list):
    if len(list)>1:
        mid=len(list) // 2
        a=mergeSort(list[:mid])
        b=mergeSort(list[mid:])
        return merge(a,b)
    else:return list

def merging2(lst):
    sublist = []
    for i in range(0, len(lst) - 1, 2):
        sublist.append(merge(lst[i], lst[i + 1]))
    if len(lst) % 2 == 1: sublist.append(lst[-1])
    if len(sublist) == 1:
        return sublist[0]
    return merging2(sublist)

start_time = time.time()
list = random.sample(range(-200,200),100)
sorted_list = mergeSort(list)

end_time = time.time()
elapsed_time = (end_time - start_time) * 1000
print(f"Prosedure Time: {elapsed_time:.3f} ms")
