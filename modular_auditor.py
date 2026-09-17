# https://github.com/marissaasasasasass/Smart-Inventory-Auditor

# 1. Initialize the inventory to zero in the start 
inventory_stock = 0
entries = 0

def get_valid_input():
    while True:
        inventory = input("Enter a stock quantity (or 'quit' to exit): ")

        if inventory.isdigit() and int(inventory) > 0: #Accept positive stock values as integers (3)
            inventory_stock += inventory #Keep a running total of the inventory (6)

            if inventory_stock >= 500: #Trigger Overstock Alert (7)
                print("Warning: Inventory exceeds maximum capacity of 500 units.")
                return int(inventory_stock)
                break

        elif inventory == "quit": #Unless the user types 'quit' (2)
            return "quit"

        elif inventory.isdigit() and int(inventory) <= 0: #Enforce Business Rule (5)
            print("Stock quantity must be above 0.")
            continue

        else: #Handle Invalid Input (4)
            print("Invalid input. Please enter a valid stock quantity or 'quit' to exit.")
            continue

def process_delivery(current_total, new_value):
    delivery_total = current_total + new_value
    return delivery_total