class Product:
    def __init__(self, product_id, name, category, price, weight, description=""):
        self.id = product_id
        self.name = name
        self.category = category
        self.price = float(price)
        self.weight = float(weight)
        self.description = description

    def __repr__(self):
        return f"Product({self.id}, '{self.name}', {self.category}, {self.price}₽, {self.weight}кг)"


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

    def display_all(self):
        if not self.products:
            print("Каталог пуст.")
            return
        print("\nКаталог товаров:")
        for product in self.products.values():
            print(f"ID={product.id} | {product}")


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
            print(f"Товар с ID={product_id} не находится в корзине.")

    def display_cart(self):
        if not self.items:
            print("Корзина пуста.")
            return

        print("\nСодержимое корзины:")
        print("=" * 80)

        
        from collections import Counter
        cart_items = Counter(self.items)

        total_cost = 0
        total_weight = 0

        for product_id, count in cart_items.items():
            product = self.catalog.get_product(product_id)
            if not product:
                continue

            item_total = product.price * count
            item_weight = product.weight * count

            total_cost += item_total
            total_weight += item_weight

            print(f"Товар: {product.name}")
            print(f"Категория: {product.category}")
            print(f"Цена: {product.price}₽ × {count} шт = {item_total:.2f}₽")
            print(f"Вес: {product.weight}кг × {count} шт = {item_weight:.2f}кг")
            if product.description:
                print(f"    Описание: {product.description}")
            print()

        print("=" * 80)
        print(f"ИТОГО: {len(cart_items)} наименований, "
              f"на сумму {total_cost:.2f}₽, "
              f"общий вес: {total_weight:.2f}кг")


if __name__ == "__main__":

 catalog = ProductCatalog()

id1 = catalog.add_product("Ноутбук", "Электроника", 75000, 2.1, "Игровой ноутбук")
id2 = catalog.add_product("Смартфон", "Электроника", 45000, 0.18, "С камерой 200 МП")
id3 = catalog.add_product("Офисный стул", "Мебель", 9500, 6.5, "С регулировкой высоты")


catalog.display_all()


cart = ShoppingCart(catalog)

cart.add_item(id1)
cart.add_item(id2)
cart.add_item(id2)
cart.add_item(id3)


cart.display_cart()

cart.remove_item(id2)

cart.display_cart()
