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
def add_product(inventory, product_id, product_name, quantity):

    for product in inventory:
        if product["product_id"] == product_id:
            print("Product already exists.")
            return

    inventory.append({
        "product_id": product_id,
        "product_name": product_name,
        "quantity": quantity
    })

    print("Product added successfully.")


# NEW FUNCTION 2
def update_stock(inventory, product_id, quantity):

    for product in inventory:
        if product["product_id"] == product_id:
            product["quantity"] += quantity
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

    print("\nCurrent Inventory:")

    for product in inventory:
        print(
            product["product_id"],
            product["product_name"],
            product["quantity"]
        )


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


# -----------------------------
# Main Program
# -----------------------------

inventory_stock, transaction_history = load_inventory()

failed_entries = 0

while True:

    product_id = input("Enter product ID (or 'quit' to exit): ")

    if product_id == "quit":
        save_inventory(inventory_stock, transaction_history)
        break

    product_name = input("Enter product name: ")

    user_input = get_valid_input()

    if user_input == "quit":
        save_inventory(inventory_stock, transaction_history)
        break

    elif user_input is None:
        failed_entries += 1
        continue

    else:
        process_delivery(
            inventory_stock,
            product_id,
            product_name,
            user_input
        )

        transaction_history.append(user_input)

        print(f"Delivery processed: {user_input} units")

        product = search_product(inventory_stock, product_id)

        print(
            f"Current stock for {product_name}: "
            f"{product['quantity']}"
        )


generate_report(inventory_stock, failed_entries)
