# https://github.com/marissaasasasasass/Smart-Inventory-Auditor

# 1. Initialize the inventory to zero in the start 
inventory_stock = 0
failed_entries = 0

def get_valid_input():
    inventory = input("Enter a stock quantity (or 'quit' to exit): ")

    if inventory == "quit":
        return "quit"

    elif inventory.startswith("-") and inventory[1:].isdigit():
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