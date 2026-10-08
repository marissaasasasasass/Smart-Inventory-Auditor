# https://github.com/marissaasasasasass/Smart-Inventory-Auditor

import json

def load_inventory():
    inventory = []
    history = []

    try:
        file = open("inventory.json", "r")
        inventory = json.load(file)
        file.close()

    except FileNotFoundError:
        pass

    return inventory, history


def save_inventory(inventory, history):
    file = open("inventory.json", "w")

    json.dump(inventory, file, indent=4)

    file.close()


def get_valid_input():
    quantity = input("Enter a stock quantity (or 'quit' to exit): ")

    if quantity == "quit":
        return "quit"

    elif quantity.isdigit():
        quantity = int(quantity)

        if quantity > 0:
            return quantity
        else:
            print("Stock quantity must be above 0.")
            return None

    else:
        print(
            "Invalid input. Please enter a valid stock quantity "
            "or 'quit' to exit."
        )
        return None


# NEW FUNCTION 1
def add_product(inventory, product_id, product_name, price, quantity):

    for product in inventory:
        if product["product_id"] == product_id:
            print("Product already exists.")
            return

    inventory.append({
        "product_id": product_id,
        "product_name": product_name,
        "price": price,
        "quantity": quantity
    })

    print("Product added successfully.")


# NEW FUNCTION 2
def update_stock(inventory, product_id, quantity):

    for product in inventory:
        if product["product_id"] == product_id:
            product["quantity"] = quantity
            print("Stock updated successfully.")
            return

    print("Product not found.")

# NEW FUNCTION 3
def search_product(inventory, product_id):
    for product in inventory:
        if product["product_id"] == product_id:
            return product
    return None


# NEW FUNCTION 4
def display_all(inventory):

    print("------------------------------")
    for product in inventory:
        print(
            f"ID: {product['product_id']} | "
            f"Name: {product['product_name']} | "
            f"Price: ${product['price']:.2f} | "
            f"Stock: {product['quantity']}"
        )
    print("------------------------------")


def process_delivery(inventory, product_id, product_name, quantity):
    product = search_product(inventory, product_id)

    if product is not None:
        update_stock(inventory, product_id, quantity)

    else:
        add_product(inventory, product_id, product_name, quantity)


def calculate_tax(amount):
    tax_rate = 0.1
    tax_amount = amount * tax_rate
    return tax_amount


def generate_report(inventory, failed_attempts):
    print("\nFinal inventory:")
    display_all(inventory)
    print(f"Total failed entries: {failed_attempts}")

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
        display_all(inventory_stock)

    elif option == "2":
        print("\nAdd New Product")

        product_id = input("Product ID: ")
        product_name = input("Product Name: ")
        price = float(input("Price: "))
        quantity = int(input("Stock Quantity: "))

        add_product(
            inventory_stock,
            product_id,
            product_name,
            price,
            quantity
        )

    elif option == "3":
        print("\nUpdate Stock")

        product_id = input("Enter Product ID: ")

        product = search_product(inventory_stock, product_id)

        if product is not None:
            print("\nProduct Found:")
            print("Name:", product["product_name"])
            print("Current Stock:", product["quantity"])

            quantity = int(input("\nNew Stock Quantity: "))

            update_stock(inventory_stock, product_id, quantity)

        else:
            print("Product not found.")

    elif option == "4":
        print("\nSearch Product")

        product_id = input("Enter Product ID: ")

        product = search_product(inventory_stock, product_id)

        if product is not None:
            print("\nProduct Found")
            print("------------------------------")
            print("ID:", product["product_id"])
            print("Name:", product["product_name"])
            print(f"Price: ${product['price']:.2f}")
            print("Stock:", product["quantity"])
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
