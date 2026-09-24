def load_inventory():
    try:
        file = open("inventory.txt", "r")

        lines = file.readlines()
        file.close()

        total = int(lines[0].strip())

        history = []

        for line in lines[1:]:
            history.append(int(line.strip()))

        return total, history

    except FileNotFoundError:
        # No inventory.txt yet
        return 0, []


def save_inventory(total, history):
    file = open("inventory.txt", "w")

    # Save total inventory
    file.write(str(total) + "\n")

    # Save transaction history
    for amount in history:
        file.write(str(amount) + "\n")

    file.close()


def get_valid_input():
    while True:
        stock = input("Enter stock quantity (Quit to stop): ")

        if stock.upper() == "QUIT":
            return "quit"

        try:
            stock = int(stock)

            if stock < 0:
                print("Negative numbers are not accepted")
            else:
                return stock

        except ValueError:
            print("Invalid input, try again")


def process_delivery(current_total, new_value):
    return current_total + new_value


def calculate_tax(amount):
    return amount * 0.10


def generate_report(total_units, failed_attempts):
    print("\nFinal Report")
    print("Total Inventory:", total_units)
    print("Failed/Rejected Entries:", failed_attempts)


# ---------------- MAIN PROGRAM ----------------

inventory, history = load_inventory()

failed_attempts = 0

print("Current Inventory:", inventory)

while True:

    stock = get_valid_input()

    if stock == "quit":
        break

    inventory = process_delivery(inventory, stock)

    # Add valid transaction to history list
    history.append(stock)

    tax = calculate_tax(stock)

    print("Delivery added:", stock)
    print("Tax:", tax)
    print("Current Inventory:", inventory)


# Save everything when user quits
save_inventory(inventory, history)

generate_report(inventory, failed_attempts)

print("\nTransaction History:", history)
print("Inventory successfully saved to inventory.txt")