from collections import deque
import datetime


tasks = [
    ("Отправить отчёт", 3),
    ("Проверить почту", 2),
    ("Запустить бэкап", 5),
    ("Обновить документацию", 4),
    ("Собрать статистику", 3)
]


queue = deque(tasks)


current_time = datetime.datetime.now()
print(" Моделирование обработки задач в очереди\n")
print(f"Стартовое время: {current_time.strftime('%H:%M:%S')}")
print("-" * 50)


for i in range(len(queue)):
    task_name, duration = queue.popleft()  
    
    start_time = current_time
    end_time = current_time + datetime.timedelta(seconds=duration)
    
    print(f" {i+1}. {task_name}")
    print(f"Начало: {start_time.strftime('%H:%M:%S')}")
    print(f"Окончание: {end_time.strftime('%H:%M:%S')} (+{duration} сек)")
    print()
    
    
    current_time = end_time

print("Все задачи обработаны.")
