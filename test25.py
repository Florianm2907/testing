import random
arr = []
for i in range(100000):
    arr.append(i)
random.shuffle(arr)
def issorted(arr):
    sorted = True
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            sorted = False
    return sorted
def stalinsort(arr):
    sorted = False
    h = 0
    geloescht = 0
    while not sorted:
        while arr[h] > arr[h+1]:
            arr.pop(h)
            geloescht += 1
        if h == len(arr)-2:
            sorted = issorted(arr)
            h = 0
        else: h+=1
    return(arr)
print(stalinsort(arr))