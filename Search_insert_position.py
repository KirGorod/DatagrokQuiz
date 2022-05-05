def findIndex(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        elif arr[i] > target:
            return i
    return len(arr)

arr = [1,3,5,6,7]
print(findIndex(arr, 4))

