from collections import Counter
class Product:
    def __init__(self, product_id, name, category, price, weight, description=""):
        self.id = product_id
        self.name = name
        self.category = category
        self.price = float(price)
        self.weight = float(weight)
        self.description = description

    def __repr__(self):
        return f"{self.name} ({self.category}, {self.price}₽, {self.weight}кг)"


class ProductCatalog:
    def __init__(self):
        self.products = {}
        self.next_id = 1

    def add_product(self, name, category, price, weight, description=""):
        product = Product(self.next_id, name, category, price, weight, description)
        self.products[self.next_id] = product
        print(f"Добавлен товар ID={self.next_id}: '{name}'")
        self.next_id += 1
        return self.next_id - 1

    def get_product(self, product_id):
        return self.products.get(product_id)


class ShoppingCart:
    def __init__(self, catalog):
        self.catalog = catalog
        self.items = []

    def add_item(self, product_id):
        product = self.catalog.get_product(product_id)
        if product:
            self.items.append(product_id)
            print(f"'{product.name}' добавлен в корзину.")
        else:
            print(f"Товар с ID={product_id} не найден.")

    def remove_item(self, product_id):
        if product_id in self.items:
            product = self.catalog.get_product(product_id)
            self.items.remove(product_id)
            print(f"'{product.name}' удалён из корзины.")
        else:
            print(f"ℹТовар с ID={product_id} не в корзине.")

    def get_items(self):
        return [self.catalog.get_product(pid) for pid in self.items if self.catalog.get_product(pid)]

    def bubble_sort(self, items, key_func, reverse=False):
        arr = items[:]
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                cmp = key_func(arr[j]) > key_func(arr[j + 1])
                if not reverse and cmp or reverse and not cmp:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr

    def insertion_sort(self, items, key_func, reverse=False):
        arr = items[:]
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and ((key_func(arr[j]) > key_func(key)) ^ reverse):
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    def quick_sort(self, items, key_func, reverse=False):
        if len(items) <= 1:
            return items
        pivot = items[len(items) // 2]
        left = [x for x in items if (key_func(x) < key_func(pivot)) ^ reverse]
        middle = [x for x in items if key_func(x) == key_func(pivot)]
        right = [x for x in items if (key_func(x) > key_func(pivot)) ^ reverse]
        return self.quick_sort(left, key_func, reverse) + middle + self.quick_sort(right, key_func, reverse)

    def merge_sort(self, items, key_func, reverse=False):
        if len(items) <= 1:
            return items

        mid = len(items) // 2
        left = self.merge_sort(items[:mid], key_func, reverse)
        right = self.merge_sort(items[mid:], key_func, reverse)

        return self._merge(left, right, key_func, reverse)

    def _merge(self, left, right, key_func, reverse):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            left_val = key_func(left[i])
            right_val = key_func(right[j])
            if (left_val <= right_val) ^ reverse:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def sort_items(self, by="price", order="asc", algorithm="quick"):
        
        items = self.get_items()
        if not items:
            print("Корзина пуста — сортировать нечего.")
            return []

        reverse = order == "desc"

        key_funcs = {
            "price": lambda p: p.price,
            "weight": lambda p: p.weight,
            "category": lambda p: p.category.lower()
        }

        if by not in key_funcs:
            print(f"Неизвестный критерий сортировки: {by}")
            return items

        key_func = key_funcs[by]

        algorithms = {
            "bubble": self.bubble_sort,
            "insertion": self.insertion_sort,
            "quick": self.quick_sort,
            "merge": self.merge_sort
        }

        if algorithm not in algorithms:
            print(f"Неизвестный алгоритм: {algorithm}. Используется 'quick'.")
            algorithm = "quick"

        sorted_items = algorithms[algorithm](items, key_func, reverse)
        return sorted_items

  
    def display_cart(self, sorted_items=None):
        items_to_show = sorted_items or self.get_items()

        if not items_to_show:
            print("🛒 Корзина пуста.")
            return

        print("\nСодержимое корзины:")
        print("=" * 80)

        total_cost = sum(p.price for p in items_to_show)
        total_weight = sum(p.weight for p in items_to_show)
        cart_count = Counter(p.name for p in items_to_show)

        for name, count in cart_count.items():
            product = next(p for p in items_to_show if p.name == name)
            print(f"• {name} ×{count}")
            print(f"    Категория: {product.category}")
            print(f"    Цена: {product.price}₽")
            print(f"    Вес: {product.weight}кг")

        print("=" * 80)
        print(f"ИТОГО: {len(cart_count)} наименований, "
              f"на сумму {total_cost:.2f}₽, "
              f"вес: {total_weight:.2f}кг")

# пример:

if __name__ == "__main__":
    catalog = ProductCatalog()
    id1 = catalog.add_product("Ноутбук", "Электроника", 75000, 2.1, "Игровой")
    id2 = catalog.add_product("Смартфон", "Электроника", 45000, 0.18, "Флагман")
    id3 = catalog.add_product("Стул", "Мебель", 9500, 6.5, "Офисный")
    id4 = catalog.add_product("Лампа", "Мебель", 3500, 1.2, "Светодиодная")

    cart = ShoppingCart(catalog)
    cart.add_item(id1)
    cart.add_item(id2)
    cart.add_item(id3)
    cart.add_item(id4)
    cart.add_item(id2)

    print("\nВыберите алгоритм сортировки:")
    print("1. Пузырьковая (bubble)")
    print("2. Вставками (insertion)")
    print("3. Быстрая (quick)")
    print("4. Слиянием (merge)")

    algo = input("Введите название алгоритма (по умолчанию 'quick'): ").strip().lower() or "quick"
    by = input("Сортировать по (price/weight/category): ").strip().lower() or "price"
    order = input("Порядок (asc/desc): ").strip().lower() or "asc"

    sorted_items = cart.sort_items(by=by, order=order, algorithm=algo)
    cart.display_cart(sorted_items)