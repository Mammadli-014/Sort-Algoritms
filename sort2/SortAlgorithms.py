import random

lst = [10,20,1,35,40,15]
n=len(lst)

#Buble sort2
needNextPass=True
while 1 < len(lst) and needNextPass:
    needNextPass = False
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            lst[i],lst[i+1]=lst[i+1],lst[i]
            needNextPass = True

#selection Sort
lst = [10,20,1,35,40,15]

for i in range(n):
    min_index=i
    for j in range(i+1,n):
        if lst[min_index]>lst[j]:
            min_index=j
    lst[i],lst[min_index]=lst[min_index],lst[i]
print(lst)

# insertion sort2
lst = random.sample(range(-2000000, 2000000), 100000)
for i in range(1, len(lst)):
    currentElement = lst[i]
    k = i - 1
    while k >= 0 and lst[k] > currentElement:
        lst[k + 1] = lst[k]
        k -= 1

    lst[k + 1] = currentElement
