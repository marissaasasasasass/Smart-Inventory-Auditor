# 1. Initialize the inventory to zero in the start 
inventory_stock = 0
entries = 0

while True: #Runs in a continous loop (2)
    inventory = input("Enter a stock quantity (or 'quit' to exit): ")

    if inventory.isdigit() and int(inventory) > 0: #Accept positive stock values as integers (3)
        inventory = int(inventory)
        entries += 1
        inventory_stock += inventory #Keep a running total of the inventory (6)

        if inventory_stock >= 500: #Trigger Overstock Alert (7)
            print("Warning: Inventory exceeds maximum capacity of 500 units.")
            break

        else:
            print(f"Current inventory: {inventory_stock}")

    elif inventory == "quit": #Unless the user types 'quit' (2)
        #Reporting (8)
        print (f"Final inventory: {inventory_stock}")
        print (f"Total entries: {entries}")
        break

    elif inventory.isdigit() and int(inventory) <= 0: #Enforce Business Rule (5)
        print("Stock quantity must be above 0.")
        continue

    else: #Handle Invalid Input (4)
        print("Invalid input. Please enter a valid stock quantity or 'quit' to exit.")
        continue