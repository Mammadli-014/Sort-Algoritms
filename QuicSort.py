class Quick_Sort:
    def __init__(self, lst):
        self.lst = lst

    def partition(self, first, last):
        pivot = self.lst[first]  # Choose the first element as the pivot
        low = first + 1  # Index for forward search
        high = last  # Index for backward search

        while high > low:
            # Search forward from left
            while low <= high and self.lst[low] <= pivot:
                low += 1

            # Search backward from right
            while low <= high and self.lst[high] > pivot:
                high -= 1

            # Swap two elements in the list
            if high > low:
                self.lst[high], self.lst[low] = self.lst[low], self.lst[high]  # Doğru swap

        while high > first and self.lst[high] >= pivot:
            high -= 1

        # Swap pivot with lst[high]
        if pivot > self.lst[high]:
            self.lst[first] = self.lst[high]
            self.lst[high] = pivot
            return high
        else:
            return first

    def quickSortHelper(self, first, last):
        if last > first:
            pivotIndex = self.partition(first, last)
            self.quickSortHelper(first, pivotIndex - 1)
            self.quickSortHelper(pivotIndex + 1, last)

    def quickSort(self):
        self.quickSortHelper( 0, len(self.lst) - 1)

    def sort(self):
        self.quickSortHelper(0, len(self.lst) - 1)
        return self.lst  # Sıralı listeyi döndürüyoruz