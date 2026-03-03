def binary_search(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid -1)
    else:
        return binary_search(arr, target, mid +1, right)
    
arr = [1, 3, 5, 7, 9, 11, 13, 15]
print (binary_search(arr, 7))
print (binary_search(arr, 4))
print (binary_search(arr, 2))
print (binary_search(arr, 15))