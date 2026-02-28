import random
import time
import matplotlib.pyplot as plt

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

def linear_search(arr, target):
    
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1



sizes = [100, 500, 1000, 2000, 5000, 10000]
binary_times = []
linear_times = []

print("🔍 Запуск сравнения времени поиска...")

for size in sizes:
    
    arr = sorted([random.randint(1, size * 10) for _ in range(size)])
    target = arr[size // 2]  

    # Замер времени для бинарного поиска
    start = time.perf_counter()
    binary_search(arr, target)
    binary_times.append(time.perf_counter() - start)

    # Замер времени для линейного поиска
    start = time.perf_counter()
    linear_search(arr, target)
    linear_times.append(time.perf_counter() - start)

    print(f"Размер {size}: линейный={linear_times[-1]:.6f} с, бинарный={binary_times[-1]:.6f} с")

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(sizes, binary_times, label="Бинарный поиск (O(log n))", marker="o")
plt.plot(sizes, linear_times, label="Линейный поиск (O(n))", marker="s")
plt.xlabel("Размер списка (n)")
plt.ylabel("Время выполнения (секунды)")
plt.title("Сравнение времени поиска: бинарный vs линейный")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
