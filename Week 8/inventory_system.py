# https://github.com/marissaasasasasass/Smart-Inventory-Auditor


import json


# -----------------------------
# Product Class
# -----------------------------

class Product:

    def __init__(self, product_id, product_name, price, quantity):

        if price < 0 or quantity < 0:
            raise ValueError("Price and stock quantity cannot be negative.")

        self.__product_id = product_id
        self.__name = product_name
        self.__price = price
        self.__stock = quantity

    def update_stock(self, quantity):

        if quantity >= 0:
            self.__stock = quantity
            print("Stock updated successfully.")

        else:
            print("Stock quantity cannot be negative.")

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


# -----------------------------
# Inventory Class
# -----------------------------

class Inventory:

    def __init__(self):
        self.__products = []

    def add_product(self, product, show_message=True):

        for item in self.__products:

            if item.get_product_id() == product.get_product_id():

                if show_message:
                    print("Product already exists.")

                return

        self.__products.append(product)

        if show_message:
            print("Product added successfully.")

    def search_product(self, product_id):

        for product in self.__products:

            if product.get_product_id() == product_id:
                return product

        return None

    def display_all(self):

        print("------------------------------")

        if len(self.__products) == 0:
            print("Inventory is empty.")

        else:
            for product in self.__products:
                product.display_information()

        print("------------------------------")

    def get_products(self):
        return self.__products.copy()


# -----------------------------
# File Handling
# -----------------------------

def load_inventory():

    inventory = Inventory()

    try:
        with open("inventory.json", "r") as file:
            data = json.load(file)

        for item in data:

            product = Product(
                item["product_id"],
                item["product_name"],
                item["price"],
                item["quantity"]
            )

            inventory.add_product(product, False)

    except FileNotFoundError:
        print("No existing inventory file found. Starting with empty inventory.")

    except json.JSONDecodeError:
        print("Invalid inventory.json file. Starting with empty inventory.")

    return inventory


def save_inventory(inventory):

    data = []

    for product in inventory.get_products():

        data.append({
            "product_id": product.get_product_id(),
            "product_name": product.get_name(),
            "price": product.get_price(),
            "quantity": product.get_stock()
        })

    with open("inventory.json", "w") as file:
        json.dump(data, file, indent=4)


# -----------------------------
# Display Menu
# -----------------------------

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

print("========================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("========================================")

inventory_stock = load_inventory()

while True:

    display_menu()

    option = input("Enter option: ")

    # Option 1: Display All Products
    if option == "1":

        print("\nCurrent Inventory")
        inventory_stock.display_all()

    # Option 2: Add Product
    elif option == "2":

        print("\nAdd New Product")

        product_id = input("Product ID: ")
        product_name = input("Product Name: ")

        try:
            price = float(input("Price: "))
            quantity = int(input("Stock Quantity: "))

            product = Product(
                product_id,
                product_name,
                price,
                quantity
            )

            inventory_stock.add_product(product)

        except ValueError:
            print("Invalid input. Price and stock quantity must be valid non-negative numbers.")

    # Option 3: Update Stock
    elif option == "3":

        print("\nUpdate Stock")

        product_id = input("Enter Product ID: ")

        product = inventory_stock.search_product(product_id)

        if product is not None:

            print("\nProduct Found:")
            print("Name:", product.get_name())
            print("Current Stock:", product.get_stock())

            try:
                quantity = int(input("\nNew Stock Quantity: "))

                product.update_stock(quantity)

            except ValueError:
                print("Invalid input. Please enter a valid whole number.")

        else:
            print("Product not found.")

    # Option 4: Search Product
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

    # Option 5: Save Inventory
    elif option == "5":

        print("\nSaving inventory...")

        save_inventory(inventory_stock)

        print("Inventory saved successfully to inventory.json.")

    # Option 6: Exit
    elif option == "6":

        print("\nSaving inventory before exit...")

        save_inventory(inventory_stock)

        print("Inventory saved successfully.")
        print("\nThank you for using Inventory Management System.")
        print("Program terminated.")

        break

    else:
        print("Invalid option. Please enter 1 to 6.")
