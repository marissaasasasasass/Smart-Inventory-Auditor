# https://github.com/marissaasasasasass/Smart-Inventory-Auditor

def load_inventory():
    try:
        file = open("inventory.txt", "r")

        lines = file.readlines()
        file.close()

        # First line stores the final inventory total
        inventory = int(lines[0].strip())

        # Second line onwards store previous transactions
        history = []

        for line in lines[1:]:
            history.append(int(line.strip()))

        return inventory, history

    except FileNotFoundError:
        # Start with empty inventory and empty history
        return 0, []

def save_inventory(inventory, history):
    file = open("inventory.txt", "w")

    # Save final inventory
    file.write(str(inventory) + "\n")

    # Save every transaction
    for transaction in history:
        file.write(str(transaction) + "\n")

    file.close()


def get_valid_input():
    inventory = input("Enter a stock quantity (or 'quit' to exit): ")

    if inventory == "quit":
        return "quit"

    elif inventory.isdigit() and int(inventory) <= 0:
        print("Stock quantity must be above 0.")
        return None

    elif inventory.isdigit():
        inventory = int(inventory)

        if inventory > 0:
            return inventory
        else:
            print("Stock quantity must be above 0.")
            return None

    else:
        print("Invalid input. Please enter a valid stock quantity or 'quit' to exit.")
        return None

def process_delivery(current_total, new_value):
    delivery_total = current_total + new_value
    return delivery_total

def calculate_tax(amount):
    tax_rate = 0.1  # 10% tax rate
    tax_amount = amount * tax_rate
    return tax_amount

def generate_report(total_units, failed_attempts):
    print(f"Final inventory: {total_units}")
    print(f"Total failed entries: {failed_attempts}")

# ----------------------------------------
# Main Program
# ----------------------------------------   

# Run infinite loop until user decides to quit or inventory exceeds 500
inventory_stock, transaction_history = load_inventory()
failed_entries = 0
deliveries_processed = 0

while True:
    product_id = input("Enter product ID: ")
    user_input = get_valid_input()

    # User wants to quit
    if user_input == "quit":
        break

    # Invalid input
    elif user_input is None:
        failed_entries += 1
        continue

    # Valid delivery
    else:
        # Store transaction in history
        transaction_history.append(user_input)

        inventory_stock = process_delivery(inventory_stock, user_input)

        tax = calculate_tax(user_input)

        deliveries_processed += 1

        print(f"Delivery processed: {user_input} units")
        print(f"Tax for this delivery: {tax}")
        print(f"Current inventory: {inventory_stock}")

        if inventory_stock > 500:
            print(
                "Warning: Inventory exceeds maximum capacity of 500 units."
            )
            break


generate_report(inventory_stock, failed_entries)

print("Transaction history:", transaction_history)