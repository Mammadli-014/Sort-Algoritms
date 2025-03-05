import random
# insertion sort2
lst = random.sample(range(-2000000, 2000000), 100000)
for i in range(1, len(lst)):
    currentElement = lst[i]
    k = i - 1
    while k >= 0 and lst[k] > currentElement:
        lst[k + 1] = lst[k]
        k -= 1

    lst[k + 1] = currentElement
