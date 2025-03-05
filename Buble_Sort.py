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
