# https://github.com/marissaasasasasass/Smart-Inventory-Auditor

def load_inventory():
    inventory = {}
    history = []

    try:
        file = open("inventory.txt", "r")

        for line in file:
            line = line.strip()

            if line == "":
                continue

            parts = line.split(",")
            product_id = parts[0]
            product_name = parts[1]
            quantity = int(parts[2])
            inventory[product_id] = [product_name, quantity]

        file.close()

    except FileNotFoundError:
        pass

    return inventory, history


def save_inventory(inventory, history):
    file = open("inventory.txt", "w")

    for product_id in inventory:
        product_name = inventory[product_id][0]
        quantity = inventory[product_id][1]

        file.write(
            product_id + "," +
            product_name + "," +
            str(quantity) + "\n"
        )

    file.close()


def get_valid_input():
    inventory = input("Enter a stock quantity (or 'quit' to exit): ")

    if inventory == "quit":
        return "quit"

    elif inventory.isdigit():
        inventory = int(inventory)

        if inventory > 0:
            return inventory
        else:
            print("Stock quantity must be above 0.")
            return None
    else:
        print(
            "Invalid input. Please enter a valid stock quantity "
            "or 'quit' to exit."
        )
        return None


def process_delivery(inventory, product_id, product_name, quantity):

    for product in inventory:
        if product["product_id"] == product_id:
            product["quantity"] += quantity
            return

    inventory.append({
        "product_id": product_id,
        "product_name": product_name,
        "quantity": quantity
    })

def calculate_tax(amount):
    tax_rate = 0.1
    tax_amount = amount * tax_rate
    return tax_amount


def generate_report(inventory, failed_attempts):
    print("\nFinal inventory:")

    for product_id in inventory:
        product_name = inventory[product_id][0]
        quantity = inventory[product_id][1]

        print(product_id, product_name, quantity)

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

        print(
            f"Current stock for {product_name}: "
            f"{inventory_stock[product_id][1]}"
        )


generate_report(inventory_stock, failed_entries)