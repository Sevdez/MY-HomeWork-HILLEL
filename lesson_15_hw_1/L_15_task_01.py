import pickle


class Product:

    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity


# Shop's default store
my_products = [
    Product("Milk", 100, 250),
    Product("Bread", 28, 70),
    Product("Eggs", 100, 500),
    Product("Cider", 50, 500),
    Product("Pizza", 99, 50)
]


class Store:

    def __init__(self):
        self.products = []
        self.total_income = 0
        self.income_by_product = {}

    def save_store(self, shop_data):
        self.products = shop_data.products
        self.total_income = shop_data.total_income
        self.income_by_product = shop_data.income_by_product

        save_data = [self.products, self.total_income, self.income_by_product]
        with open('store.obj', 'wb') as f:
            pickle.dump(save_data, f)

    def load_store(self):
        with open('store.obj', 'rb') as f:
            store_data = pickle.load(f)
            self.products = store_data[0]
            self.total_income = store_data[1]
            self.income_by_product = store_data[2]

    def get_store(self):
        return [self.products, self.total_income, self.income_by_product]


my_store = Store()


class Shop:

    def __init__(self, products):
        self.products = products
        self.total_income = 0
        self.income_by_product = {}

    def display_products(self):
        available_products = list(map(
            lambda product: f'{product.quantity} items of {product.title}. Price: {product.price} \n',
            self.products
        ))

        str_available_products = "".join(available_products)

        print(f'\n'
              f'Available products:\n'
              f'\n'
              f'{str_available_products}\n')

    def buy_product(self):
        title_input = input('Which product do you want to buy? \n')

        required_product = [product for product in self.products if product.title == title_input][0]

        def get_quantity():
            print(f'There are {required_product.quantity} of {required_product.title} in shop.\n ')
            quantity_input = input(
                f' \n'
                f'How many you want to buy?'
            )

            if quantity_input > str(required_product.quantity):
                print('Sorry, the Shop doesn\'t have this amount of product')
                return get_quantity()
            else:
                return quantity_input

        required_quantity = get_quantity()

        for product in self.products:
            if product.title == title_input:
                profit = product.price * int(required_quantity)
                product.quantity -= int(required_quantity)
                self.total_income += profit
                if title_input in self.income_by_product:
                    self.income_by_product[title_input] += profit
                else:
                    self.income_by_product[title_input] = profit

    def get_income_by_product(self):
        return self.income_by_product

    def get_total_income(self):
        return self.total_income

    def set_store(self, store):
        self.products = store[0]
        self.total_income = store[1]
        self.income_by_product = store[2]


my_shop = Shop(my_products)
