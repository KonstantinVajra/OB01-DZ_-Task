class Store:
    def __init__(self, name, address):
        self.name = name  # название магазина
        self.address = address  # адрес магазина
        self.items = {}  # пустой словарь для товаров

    def add_item(self, item_name, price):
        """Метод для добавления товара в ассортимент."""
        self.items[item_name] = price

    def remove_item(self, item_name):
        """Метод для удаления товара из ассортимента."""
        if item_name in self.items:
            del self.items[item_name]
        else:
            print(f"Товар {item_name} не найден в ассортименте.")

    def get_price(self, item_name):
        """Метод для получения цены товара по названию."""
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        """Метод для обновления цены товара."""
        if item_name in self.items:
            self.items[item_name] = new_price
        else:
            print(f"Товар {item_name} не найден для обновления цены.")

# Пример использования:
store = Store("My Store", "123 Main St")
store.add_item("apples", 0.5)
store.add_item("bananas", 0.75)

print(store.get_price("apples"))  # 0.5
store.update_price("apples", 0.6)
print(store.get_price("apples"))  # 0.6

store.remove_item("bananas")
print(store.get_price("bananas"))  # None

# Пример использования-2
store2 = Store("Factoria43", "Primera Avenida 232")
store2.add_item("burger",1)
store2.add_item("cerveza", 1.5)

print(store2.get_price("cerveza"))
store2.update_price("cerveza", 1.3)
print(store2.get_price("cerveza"))

print(store2.get_price("pan"))
store2.update_price("pan", 1.3)

store3 = Store("Bodega", "calle 32")
store3.add_item("")
