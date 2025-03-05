#Buble sort2
class Buble_Sort:
    def __init__(self,lst):
        self.lst=lst

    def sort(self):
        needNextPass=True
        while 1 < len(self.lst) and needNextPass:
            needNextPass = False
            for i in range(len(self.lst) - 1):
                if self.lst[i] > self.lst[i + 1]:
                    self.lst[i],self.lst[i+1]=self.lst[i+1],self.lst[i]
                    needNextPass = True
        return self.lst
a=Buble_Sort([-6,10,-15,1])
print(a.sort())