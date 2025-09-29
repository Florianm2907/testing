import random

arr = []
for i in range(100000):
    arr.append(i)
random.shuffle(arr)
# print(arr)

def issorted(arr):
    sorted = True
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            sorted = False
    return sorted
def stalinsort(arr):
    sorted = False
    j = 0
    geloescht = 0
    while not sorted:
        # print("Stelle " + str(j))
        # print(len(arr))
        if arr[j] > arr[j+1]:
            # print("Element " + str(arr[j]) + " wurde gelöscht, weil es größer als " + str(arr[j+1]) + " ist.")
            arr.pop(j)
            geloescht += 1
            # print("Gelöschte Elemente: " + str(geloescht))
        
        j+=1
        if j+2 > len(arr):
            if(issorted(arr)):
                sorted = True
            j = 0
        # print(arr)
        # print(issorted(arr))
    return arr
print(stalinsort(arr))
print("Länge: " + str(len(arr)))