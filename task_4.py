from collections import Counter

class Product:
    def __init__(self, product_id, name, category, price, weight, description=""):
        self.id = product_id
        self.name = name
        self.category = category
        self.price = float(price)
        self.weight = float(weight)
        self.description = description


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
            print(f"🛒 '{product.name}' добавлен в корзину.")
        else:
            print(f"Товар с ID={product_id} не найден.")

    def remove_item(self, product_id):
        if product_id in self.items:
            product = self.catalog.get_product(product_id)
            self.items.remove(product_id)
            print(f"🗑 '{product.name}' удалён из корзины.")
        else:
            print(f"Товар с ID={product_id} не в корзине.")

    def get_items(self):
        
        return [self.catalog.get_product(pid) for pid in self.items if self.catalog.get_product(pid)]

    def calculate_subtotal(self):
        
        return sum(p.price for p in self.get_items())

    def apply_discount(self, discount_type, value):
       
        subtotal = self.calculate_subtotal()
        if discount_type == "percent":
            if not 0 <= value <= 100:
                raise ValueError("Процент скидки должен быть от 0 до 100")
            discount_amount = subtotal * (value / 100)
        elif discount_type == "fixed":
            discount_amount = min(value, subtotal)
        else:
            raise ValueError("Тип скидки: 'percent' или 'fixed'")
        
        return subtotal - discount_amount

    def add_tax(self, amount, tax_rate=20):
        
        tax_amount = amount * (tax_rate / 100)
        return amount + tax_amount


    def calculate_total(self, discount_type=None, discount_value=0, tax_rate=20):
       
        subtotal = self.calculate_subtotal()

        if discount_type and discount_value > 0:
            discounted = self.apply_discount(discount_type, discount_value)
        else:
            discounted = subtotal

        total = self.add_tax(discounted, tax_rate)

        return {
            "subtotal": round(subtotal, 2),
            "discount_type": discount_type,
            "discount_value": discount_value,
            "discounted": round(discounted, 2),
            "tax_rate": tax_rate,
            "tax_amount": round(total - discounted, 2),
            "total": round(total, 2)
        }


    def display_receipt(self, discount_type=None, discount_value=0, tax_rate=20):
        if not self.items:
            print("Корзина пуста.")
            return

        cart_count = Counter(p.name for p in self.get_items())
        print("\nЧЕК")
        print("=" * 50)
        for name, count in cart_count.items():
            product = next(p for p in self.get_items() if p.name == name)
            print(f"{name} ×{count} — {product.price}₽")

        result = self.calculate_total(discount_type, discount_value, tax_rate)

        print("=" * 50)
        print(f"Сумма: {result['subtotal']}₽")
        if discount_value > 0:
            disc_str = f"{discount_value}%" if discount_type == "percent" else f"{discount_value}₽"
            print(f"Скидка ({disc_str}):     -{round(result['subtotal'] - result['discounted'], 2)}₽")
        print(f"Налог ({result['tax_rate']}%):     +{result['tax_amount']}₽")
        print("-" * 50)
        print(f"ИТОГО: {result['total']}₽")


# пример: 
if __name__ == "__main__":
    catalog = ProductCatalog()
    id1 = catalog.add_product("Ноутбук", "Электроника", 75000, 2.1)
    id2 = catalog.add_product("Смартфон", "Электроника", 45000, 0.18)
    id3 = catalog.add_product("Стул", "Мебель", 9500, 6.5)

    cart = ShoppingCart(catalog)
    cart.add_item(id1)
    cart.add_item(id2)
    cart.add_item(id2)

    print("\nБез скидок")
    cart.display_receipt(tax_rate=20)

    
    print("\nС 10% скидкой")
    cart.display_receipt(discount_type="percent", discount_value=10, tax_rate=20)
    print("\nС фиксированной скидкой 5000₽")
    cart.display_receipt(discount_type="fixed", discount_value=5000, tax_rate=20)