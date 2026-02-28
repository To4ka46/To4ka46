import random

def binary_search(arr, target):
   
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


random_list = sorted([random.randint(1, 1000) for _ in range(100)])


targets = [random_list[0], random_list[50], random_list[-1], 9999] 

print("Отсортированный список (первые 10 элементов):", random_list[:10])
print("-" * 50)  

for target in targets:
    index = binary_search(random_list, target)
    if index != -1:
        print(f"Элемент {target} найден на позиции {index}")
    else:
        print(f"Элемент {target} не найден")
