import time
import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
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

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def measure_time(sort_func, arr):
    start_time = time.perf_counter()
    sort_func(arr.copy())
    end_time = time.perf_counter()
    return end_time - start_time

# Размеры списков
sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

times_bubble = []
times_selection = []
times_insertion = []

for size in sizes:
    test_arr = [random.randint(1, 1000) for _ in range(size)]
    times_bubble.append(measure_time(bubble_sort, test_arr))
    times_selection.append(measure_time(selection_sort, test_arr))
    times_insertion.append(measure_time(insertion_sort, test_arr))

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(sizes, times_bubble, label='Пузырьковая сортировка', marker='o')
plt.plot(sizes, times_selection, label='Сортировка выбором', marker='s')
plt.plot(sizes, times_insertion, label='Сортировка вставками', marker='^')


plt.title('Сравнение времени выполнения алгоритмов сортировки')
plt.xlabel('Размер списка (количество элементов)')
plt.ylabel('Время выполнения (секунды)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
