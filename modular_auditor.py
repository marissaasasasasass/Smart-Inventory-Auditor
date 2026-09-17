# https://github.com/marissaasasasasass/Smart-Inventory-Auditor

# 1. Initialize the inventory to zero in the start 
inventory_stock = 0
entries = 0

def get_valid_input():
    while True:
        inventory = input("Enter a stock quantity (or 'quit' to exit): ")

        if inventory.isdigit() and int(inventory) > 0: #Accept positive stock values as integers (3)
            return int(inventory)

        elif inventory == "quit": #Unless the user types 'quit' (2)
            return "quit"

        elif inventory.isdigit() and int(inventory) <= 0: #Enforce Business Rule (5)
            print("Stock quantity must be above 0.")
            continue

        else: #Handle Invalid Input (4)
            print("Invalid input. Please enter a valid stock quantity or 'quit' to exit.")
            continue