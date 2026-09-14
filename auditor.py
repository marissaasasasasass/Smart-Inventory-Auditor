# 1. Initialize the inventory to zero in the start 
inventory_stock = 0

while True: #Runs in a continous loop (2)
    inventory = input("Enter a stock quantity (or 'quit' to exit): ")

    if inventory == "quit":
        break