def simple_hash(s, table_size):
    
    if not isinstance(s, str):
        raise TypeError("Ключ должен быть строкой")
    hash_value = sum(ord(char) for char in s)
    return hash_value % table_size

class StringHashTable:
    def __init__(self, size=8):
        self.size = size
        self.table = [[] for _ in range(self.size)] 
    def add(self, key, value):
        
        index = simple_hash(key, self.size)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  
                return

        bucket.append((key, value))

    def get(self, key):
        
        index = simple_hash(key, self.size)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(key)

    def __repr__(self):
        items = []
        for bucket in self.table:
            for k, v in bucket:
                items.append(f"{repr(k)}: {repr(v)}")
        return "{" + ", ".join(items) + "}"

    def display(self):
        
        print(f"Хеш-таблица (размер = {self.size}):")
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"[{i}] {bucket}")
            else:
                print(f"[{i}] пусто")


#пример:

 #создаем таблицу

ht = StringHashTable(size=5)


ht.add("name", "Andrey")
ht.add("age", 25)
ht.add("city", "Moscow")
ht.add("job", "Malasia")


ht.display()


print("\n Поиск:")
print(f"name → {ht.get('name')}")
print(f"city → {ht.get('city')}")


ht.add("age", 26)
print(f"age → {ht.get('age')}")


try:
    print(ht.get("unknown"))
except KeyError as e:
    print(f" Ключ {e} не найден")