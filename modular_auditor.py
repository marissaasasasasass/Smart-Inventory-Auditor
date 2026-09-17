# https://github.com/marissaasasasasass/Smart-Inventory-Auditor

# 1. Initialize the inventory to zero in the start 
inventory_stock = 0
failed_entries = 0
delivery_count = 0

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

# Run infinite loop until user decides to quit or inventory exceeds 500
inventory_stock = 0
failed_entries = 0
deliveries_processed = 0

while True:
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
        inventory_stock = process_delivery(inventory_stock, user_input)

        tax = calculate_tax(user_input)

        deliveries_processed += 1

        print(f"Delivery processed: {user_input} units")
        print(f"Tax for this delivery: {tax}")
        print(f"Current inventory: {inventory_stock}")

        if inventory_stock > 500:
            print("Warning: Inventory exceeds maximum capacity of 500 units.")
            break

# This only happens after the loop ends
generate_report(inventory_stock, failed_entries)