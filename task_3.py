import random
import time
import matplotlib.pyplot as plt

def linear_search(arr, target):
    """Линейный поиск: возвращает индекс или -1."""
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1


sizes = [10, 100, 1000, 5000, 10000, 20000, 50000, 100000]
times = []

print("🚀 Запуск измерения времени линейного поиска...")

for size in sizes:
    
    arr = [random.randint(1, size) for _ in range(size)]
    
    
    target = -1

    
    start_time = time.perf_counter()
    linear_search(arr, target)
    end_time = time.perf_counter()

    elapsed = end_time - start_time
    times.append(elapsed)

    print(f"Размер {size:>6}: время {elapsed:.6f} сек")


plt.figure(figsize=(10, 6))
plt.plot(sizes, times, marker='o', linestyle='-', color='blue', label='Линейный поиск')
plt.title('Зависимость времени выполнения линейного поиска от размера списка')
plt.xlabel('Размер списка (n)')
plt.ylabel('Время выполнения (секунды)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()


plt.savefig("linear_search_time.png", dpi=150)
plt.show()

print("✅ График сохранён как 'linear_search_time.png' и отображён.")
