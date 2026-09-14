# 1. Initialize the inventory to zero in the start 
inventory_stock = 0

while True: #Runs in a continous loop (2)
    inventory = input("Enter a stock quantity (or 'quit' to exit): ")

    if inventory.isdigit() and int(inventory) > 0: #Accept positive stock values as integers (3)
        inventory = int(inventory)

    elif inventory == "quit":
        break

    elif inventory.isdigit() and int(inventory) <= 0: #Enforce Business Rule (5)
        print("Stock quantity must be above 0.")
        continue

    else:
        print("Invalid input. Please enter a valid stock quantity or 'quit' to exit.")
        continue