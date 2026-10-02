import json
import os

FILE_NAME = "inventory.json"


# ==========================================
# LOAD INVENTORY
# ==========================================
def load_inventory():
    if os.path.exists(FILE_NAME):
        print("inventory.json found.")

        try:
            with open(FILE_NAME, "r") as file:
                inventory = json.load(file)

            print("Inventory loaded successfully.")
            return inventory

        except json.JSONDecodeError:
            print("Error reading inventory.json.")
            return []

    else:
        print("inventory.json not found.")
        print("Starting with default inventory.")

        # At least 3 products
        inventory = [
            {
                "id": "P001",
                "name": "Laptop",
                "price": 1200.00,
                "stock": 15
            },
            {
                "id": "P002",
                "name": "Mouse",
                "price": 25.50,
                "stock": 40
            },
            {
                "id": "P003",
                "name": "Keyboard",
                "price": 45.00,
                "stock": 25
            }
        ]

        return inventory


# ==========================================
# SAVE INVENTORY
# ==========================================
def save_inventory(inventory):
    with open(FILE_NAME, "w") as file:
        json.dump(inventory, file, indent=4)

    print("Inventory saved successfully to inventory.json.")


# ==========================================
# DISPLAY ALL PRODUCTS
# ==========================================
def display_all(inventory):
    print("\nCurrent Inventory")
    print("------------------------------------------------")

    if len(inventory) == 0:
        print("No products in inventory.")

    else:
        for product in inventory:
            print(
                f"ID: {product['id']} | "
                f"Name: {product['name']} | "
                f"Price: ${product['price']:.2f} | "
                f"Stock: {product['stock']}"
            )

    print("------------------------------------------------")


# ==========================================
# ADD PRODUCT
# ==========================================
def add_product(inventory):
    print("\nAdd New Product")

    product_id = input("Product ID: ").upper()

    # Check if product ID already exists
    for product in inventory:
        if product["id"] == product_id:
            print("Product ID already exists.")
            return

    name = input("Product Name: ")

    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))

        if price < 0 or stock < 0:
            print("Price and stock cannot be negative.")
            return

    except ValueError:
        print("Invalid input. Price and stock must be numbers.")
        return

    new_product = {
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock
    }

    inventory.append(new_product)

    print("Product added successfully!")


# ==========================================
# UPDATE STOCK
# ==========================================
def update_stock(inventory):
    print("\nUpdate Stock")

    product_id = input("Enter Product ID: ").upper()

    for product in inventory:

        if product["id"] == product_id:
            print("Product Found:")
            print(f"Name: {product['name']}")
            print(f"Current Stock: {product['stock']}")

            try:
                new_stock = int(input("New Stock Quantity: "))

                if new_stock < 0:
                    print("Stock cannot be negative.")
                    return

                product["stock"] = new_stock

                print("Stock updated successfully!")
                return

            except ValueError:
                print("Invalid stock quantity.")
                return

    print("Product not found.")


# ==========================================
# SEARCH PRODUCT
# ==========================================
def search_product(inventory):
    print("\nSearch Product")

    product_id = input("Enter Product ID: ").upper()

    for product in inventory:

        if product["id"] == product_id:

            print("Product Found")
            print("------------------------------------------------")
            print(f"ID: {product['id']}")
            print(f"Name: {product['name']}")
            print(f"Price: ${product['price']:.2f}")
            print(f"Stock: {product['stock']}")
            print("------------------------------------------------")

            return

    print("Product not found.")


# ==========================================
# DISPLAY MENU
# ==========================================
def display_menu():
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


# ==========================================
# MAIN PROGRAM
# ==========================================
def main():

    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    inventory = load_inventory()

    while True:

        display_menu()

        option = input("Enter option: ")

        if option == "1":
            display_all(inventory)

        elif option == "2":
            add_product(inventory)

        elif option == "3":
            update_stock(inventory)

        elif option == "4":
            search_product(inventory)

        elif option == "5":
            print("Saving inventory...")
            save_inventory(inventory)

        elif option == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory)

            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break

        else:
            print("Invalid option. Please enter 1-6.")


# ==========================================
# START PROGRAM
# ==========================================
if __name__ == "__main__":
    main()