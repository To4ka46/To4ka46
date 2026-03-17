class Product:
    def __init__(self, product_id, name, category, price, weight, description=""):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = float(price)
        self.weight = float(weight)
        self.description = description

    def __repr__(self):
        return (f"Product(ID={self.product_id}, "
                f"Название='{self.name}', "
                f"Категория='{self.category}', "
                f"Цена={self.price}₽, "
                f"Вес={self.weight}кг, "
                f"Описание='{self.description}')")


class ProductCatalog:
    def __init__(self):
        self.products = []
        self.next_id = 1

    def add_product(self, name, category, price, weight, description=""):
    
        product = Product(
            product_id=self.next_id,
            name=name,
            category=category,
            price=price,
            weight=weight,
            description=description
        )
        self.products.append(product)
        print(f"Товар '{name}' добавлен с ID={self.next_id}")
        self.next_id += 1

    def find_product(self, product_id=None, name=None):
        
        for product in self.products:
            if product_id and product.product_id == product_id:
                return product
            if name and product.name.lower() == name.lower():
                return product
        return None

    def edit_product(self, product_id, **kwargs):
        
        product = self.find_product(product_id=product_id)
        if not product:
            print(f"Товар с ID={product_id} не найден.")
            return

        valid_fields = ['name', 'category', 'price', 'weight', 'description']
        for key, value in kwargs.items():
            if key in valid_fields:
                if key in ['price', 'weight']:
                    value = float(value)
                setattr(product, key, value)
            else:
                print(f"Поле '{key}' не может быть изменено.")

        print(f"Товар '{product.name}' (ID={product_id}) обновлён.")

    def delete_product(self, product_id):
        
        product = self.find_product(product_id=product_id)
        if product:
            self.products.remove(product)
            print(f"Товар '{product.name}' (ID={product_id}) удалён.")
        else:
            print(f"Товар с ID={product_id} не найден.")

    def display_all(self):
        
        if not self.products:
            print("Каталог пуст.")
            return

        print("\ Каталог товаров:")
        print("-" * 80)
        for product in self.products:
            print(product)
        print("-" * 80)

    def filter_by_category(self, category):
        
        filtered = [p for p in self.products if p.category.lower() == category.lower()]
        if not filtered:
            print(f" Нет товаров в категории '{category}'.")
            return []
        print(f"\nТовары в категории '{category}':")
        for product in filtered:
            print(f"  • {product.name} — {product.price}₽, вес: {product.weight}кг")
        return filtered


if __name__ == "__main__":
    catalog = ProductCatalog()

    catalog.add_product("Ноутбук", "Электроника", 75000, 2.1, "Мощный ноутбук для работы и игр")
    catalog.add_product("Смартфон", "Электроника", 35000, 0.2, "Флагманский смартфон 2025")
    catalog.add_product("Стул", "Мебель", 8000, 5.0, "Эргономичный офисный стул")
    catalog.add_product("Лампа", "Мебель", 3500, 1.2, "Светодиодная настольная лампа")

    
    catalog.display_all()

  
    catalog.edit_product(1, price=69999, description="Обновлённая модель")


    laptop = catalog.find_product(name="ноутбук")
    print(f"\n Найден товар: {laptop}")

    catalog.filter_by_category("Электроника")

    catalog.delete_product(4)
    catalog.display_all()
