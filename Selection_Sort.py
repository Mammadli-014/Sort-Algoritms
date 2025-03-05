class Selection_Sort:
    def __init__(self,lst):
        self.lst=lst
    def sort(self):
        n=len(self.lst)
        for i in range(n):
            min_index=i
            for j in range(i+1,n):
                if self.lst[min_index]>self.lst[j]:
                    min_index=j
            self.lst[i],self.lst[min_index]=self.lst[min_index],self.lst[i]
        return self.lst