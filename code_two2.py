import random



random_list = [random.randint(1, 1000) for _ in range(100)]
print("Список:", random_list)


search_values = [random_list[0], random_list[50], 9999]  

def linear_search(random_list, value):

 for value in search_values:
    index = linear_search(random_list, value)
    if index != -1:
        print(f"Элемент {value} найден на позиции {index}")
    else:
        print(f"Элемент {value} не найден")