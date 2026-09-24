# Load existing orders from inventory.txt
def load_inventory():
    orders = []

    try:
        with open("inventory.txt", "r") as file:
            for line in file:
                line = line.strip()

                if line == "":
                    continue

                parts = line.split(",")

                if len(parts) == 3:
                    try:
                        order_id = int(parts[0].strip())
                        product_name = parts[1].strip()
                        quantity = int(parts[2].strip())

                        orders.append([order_id, product_name, quantity])

                    except ValueError:
                        continue

    except FileNotFoundError:
        # Start with empty inventory if file does not exist
        orders = []

    return orders


# Save all orders to inventory.txt
def save_inventory(orders):
    with open("inventory.txt", "w") as file:
        for order in orders:
            file.write(
                str(order[0]) + "," +
                order[1] + "," +
                str(order[2]) + "\n"
            )


# Generate next order ID
def get_next_order_id(orders):
    if len(orders) == 0:
        return 1001

    highest_id = orders[0][0]

    for order in orders:
        if order[0] > highest_id:
            highest_id = order[0]

    return highest_id + 1


# Get valid quantity
def get_quantity():
    while True:
        quantity = input("Enter Quantity: ")

        if quantity.upper() == "QUIT":
            return "quit"

        try:
            quantity = int(quantity)

            if quantity > 0:
                return quantity
            else:
                print("Quantity must be greater than 0.")

        except ValueError:
            print("Invalid quantity. Please enter a number.")


# Display all orders
def display_inventory(orders):
    print()
    print("Current Orders:")
    print()

    if len(orders) == 0:
        print("No current orders.")

    else:
        for order in orders:
            print(
                str(order[0]) + ", " +
                order[1] + ", " +
                str(order[2])
            )


# =====================================
# MAIN PROGRAM
# =====================================

orders = load_inventory()

# Display inventory when program starts
display_inventory(orders)

print()


# Keep running until user types quit
while True:

    product_name = input("Enter Product Name (or quit to stop): ")

    # Quit program
    if product_name.upper() == "QUIT":
        break

    # Check for empty product name
    if product_name.strip() == "":
        print("Product name cannot be empty.")
        print()
        continue

    # Get quantity
    quantity = get_quantity()

    # Quit if user types quit for quantity
    if quantity == "quit":
        break

    # Generate next order ID
    order_id = get_next_order_id(orders)

    # Create new order
    new_order = [order_id, product_name, quantity]

    # Add to inventory
    orders.append(new_order)

    print()
    print("New Order Added:")
    print(
        str(order_id) + "," +
        product_name + "," +
        str(quantity)
    )

    print()


# =====================================
# WHEN USER TYPES QUIT
# =====================================

# Save inventory
save_inventory(orders)

print()
print("Order successfully saved to inventory.txt")

# Show entire final inventory
print()
print("Final Inventory:")
print()

if len(orders) == 0:
    print("No orders.")

else:
    for order in orders:
        print(
            str(order[0]) + ", " +
            order[1] + ", " +
            str(order[2])
        )