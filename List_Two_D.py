import random

#1) Question
def create2DList(numberOfRows, numberOfColumns):
    arr = []
    for i in range(numberOfRows):
        arr.append([])
        for j in range(numberOfColumns):
            arr[i].append(random.randint(0, 100))
    return arr

#2) Question
def sort2DList (arr, columnIndex):
    return sorted(arr, key=lambda x: x[columnIndex])

arr = create2DList (3, 3)
print(sort2DList(arr, 2))