import time
import matplotlib.pyplot as plt

def measure_time(arr_size):
    
    
    arr = list(range(arr_size))
    target = arr[-1]
    
    
    start_time = time.perf_counter()
    
    end_time = time.perf_counter()
    
    return end_time - start_time


sizes = [10, 50, 100, 200, 500, 1000, 2000]
times = []


for size in sizes:
    exec_time = measure_time(size)
    times.append(exec_time)
    print(f"Размер {size}: {exec_time:.6f} сек")


plt.figure(figsize=(10, 6))
plt.plot(sizes, times, marker='o', linestyle='-')
plt.title('Зависимость времени выполнения линейного поиска от размера списка')
plt.xlabel('Размер списка')
plt.ylabel('Время выполнения (сек)')
plt.grid(True)
plt.show()