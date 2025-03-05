#selection Sort
lst = [10,20,1,35,40,15]

for i in range(n):
    min_index=i
    for j in range(i+1,n):
        if lst[min_index]>lst[j]:
            min_index=j
    lst[i],lst[min_index]=lst[min_index],lst[i]
print(lst)