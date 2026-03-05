import random
import time
import matplotlib.pyplot as plt


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def bubble_sort(arr):
    arr = arr[:]
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


sizes = [10, 100, 500, 1000, 2000]
merge_times = []
bubble_times = []

print("Запуск сравнения сортировок...")

for size in sizes:
    
    arr = [random.randint(1, 1000) for _ in range(size)]
    
    # Замер merge sort
    start = time.perf_counter()
    merge_sort(arr)
    merge_time = time.perf_counter() - start
    merge_times.append(merge_time)
    
    # Замер bubble sort
    start = time.perf_counter()
    bubble_sort(arr)
    bubble_time = time.perf_counter() - start
    bubble_times.append(bubble_time)

    print(f"Размер {size}: Merge={merge_time:.6f} с | Bubble={bubble_time:.6f} с")

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(sizes, merge_times, label="Слиянием (O(n log n))", marker="o")
plt.plot(sizes, bubble_times, label="Пузырьком (O(n²))", marker="s")
plt.xlabel("Размер списка (n)")
plt.ylabel("Время выполнения (секунды)")
plt.title("Сравнение времени сортировки: слиянием vs пузырьком")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("sorting_comparison.png", dpi=150)
plt.show()

print("График сохранён и отображён.")