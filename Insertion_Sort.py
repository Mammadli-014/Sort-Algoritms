import random
class Insertion_Sort:
    def __init__(self,lst):
        self.lst=lst

    def sort(self):
        for i in range(1, len(self.lst)):
            currentElement = self.lst[i]
            k = i - 1
            while k >= 0 and self.lst[k] > currentElement:
                self.lst[k + 1] = self.lst[k]
                k -= 1
            self.lst[k + 1] = currentElement
        return self.lst