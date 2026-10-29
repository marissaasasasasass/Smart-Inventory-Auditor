# https://github.com/marissaasasasasass/Smart-Inventory-Auditor

import json

class Product:

    def __init__(self, product_id, product_name, price, quantity):
        self.__product_id = product_id
        self.__name = product_name
        self.__price = price
        self.__stock = quantity

    def update_stock(self, quantity):
        self.__stock = quantity
        print("Stock updated successfully.")

    def display_information(self):
        print(
            f"ID: {self.__product_id} | "
            f"Name: {self.__name} | "
            f"Price: ${self.__price:.2f} | "
            f"Stock: {self.__stock}"
        )

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock    

class Inventory:

    def __init__(self):
        self.__products = []

    def add_product(self, product):

        for item in self.__products:
            if item.get_product_id() == product.get_product_id():
                print("Product already exists.")
                return

        self.__products.append(product)
        print("Product added successfully.")

    def search_product(self, product_id):

        for product in self.__products:
            if product.get_product_id() == product_id:
                return product

        return None

    def display_all(self):

        print("------------------------------")

        for product in self.__products:
            product.display_information()

        print("------------------------------")

    def get_products(self):
        return self.__products

def load_inventory():

    inventory = Inventory()
    history = []

    try:
        file = open("inventory.json", "r")
        data = json.load(file)
        file.close()

        for item in data:

            product = Product(
                item["product_id"],
                item["product_name"],
                item["price"],
                item["quantity"]
            )

            inventory.add_product(product)

    except FileNotFoundError:
        pass

    return inventory, history

def save_inventory(inventory, history):

    data = []

    for product in inventory.get_products():

        data.append({
            "product_id": product.get_product_id(),
            "product_name": product.get_name(),
            "price": product.get_price(),
            "quantity": product.get_stock()
        })

    file = open("inventory.json", "w")

    json.dump(data, file, indent=4)

    file.close()

def display_menu():
    print("\n---------- MENU ----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("--------------------------")


# -----------------------------
# Main Program
# -----------------------------


# -----------------------------
# Main Program
# -----------------------------

print("========================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("========================================")

inventory_stock, transaction_history = load_inventory()

while True:

    display_menu()

    option = input("Enter option: ")

    if option == "1":
        print("\nCurrent Inventory")
        inventory_stock.display_all()

    elif option == "2":
        print("\nAdd New Product")

        product_id = input("Product ID: ")
        product_name = input("Product Name: ")
        price = float(input("Price: "))
        quantity = int(input("Stock Quantity: "))

        product = Product(
            product_id,
            product_name,
            price,
            quantity
        )

        inventory_stock.add_product(product)

    elif option == "3":
        print("\nUpdate Stock")

        product_id = input("Enter Product ID: ")

        product = inventory_stock.search_product(product_id)

        if product is not None:
            print("\nProduct Found:")
            print("Name:", product.get_name())
            print("Current Stock:", product.get_stock())

            quantity = int(input("\nNew Stock Quantity: "))

            product.update_stock(quantity)

        else:
            print("Product not found.")

    elif option == "4":
        print("\nSearch Product")

        product_id = input("Enter Product ID: ")

        product = inventory_stock.search_product(product_id)

        if product is not None:
            print("\nProduct Found")
            print("------------------------------")
            product.display_information()
            print("------------------------------")

        else:
            print("\nProduct not found.")

    elif option == "5":
        print("\nSaving inventory...")

        save_inventory(inventory_stock, transaction_history)

        print("Inventory saved successfully to inventory.json.")

    elif option == "6":
        print("\nSaving inventory before exit...")

        save_inventory(inventory_stock, transaction_history)

        print("Inventory saved successfully.")
        print("\nThank you for using Inventory Management System.")
        print("Program terminated.")
        break

    else:
        print("Invalid option. Please enter 1 to 6.")
