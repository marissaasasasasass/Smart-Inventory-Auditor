inventory_stock = 0

while True: #Runs in a continous loop (2)
    inventory = input("Enter a stock quantity (or 'quit' to exit): ")

    if inventory.isdigit() and int(inventory) > 0: #Accept positive stock values as integers (3)
        inventory = int(inventory)

    if inventory == 'quit':
        break