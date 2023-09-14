class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def total_price(self):
        total = 0
        for product in self.products:
            total += product.price * product.quantity
        return total

class Supermarket:
    def __init__(self):
        self.products = [Product("Apple", 1.00, 10),
                         Product("Banana", 0.50, 20),
                         Product("Orange", 1.50, 15),
                         Product("Mango", 2.50, 5),
                         Product("Pineapple", 3.00, 3)]

    def list_products(self):
        print("Product List:")
        for i, product in enumerate(self.products):
            print(i+1, "-", product.name, "- $", product.price, "- Quantity:", product.quantity)

    def buy_products(self):
        cart = Cart()
        self.list_products()
        while True:
            choice = input("Enter product number to add to cart (0 to finish): ")
            if choice == "0":
                break
            elif not choice.isdigit() or int(choice) < 1 or int(choice) > len(self.products):
                print("Invalid choice. Please try again.")
            else:
                product = self.products[int(choice)-1]
                quantity = int(input("Enter quantity to buy: "))
                if quantity > product.quantity:
                    print("Insufficient quantity. Please try again.")
                else:
                    product.quantity -= quantity
                    cart.add_product(Product(product.name, product.price, quantity))
                    print("Added", quantity, product.name, "to cart.")
        total = cart.total_price()
        print("Your total is: $", total)

market = Supermarket()
market.buy_products()