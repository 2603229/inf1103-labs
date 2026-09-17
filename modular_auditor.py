def get_valid_input():
    stock = input("Enter stock quantity (Quit to stop): ")

    if stock.upper() == "QUIT":
        return "quit"

    if stock.isdigit():
        return int(stock)

    return None


def process_delivery(current_total, new_value):
    current_total = current_total + new_value
    return current_total


def calculate_tax(amount):
    tax = amount * 0.10
    return tax


def generate_report(total_units, failed_attempts):
    print("\n--- FINAL REPORT ---")
    print("Total Deliveries Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)


# Main program
inventory = 0
deliveries = 0
failed_attempts = 0

while True:

    stock = get_valid_input()

    if stock == "quit":
        break

    elif stock is None:
        print("Invalid input. Please enter a positive number.")
        failed_attempts += 1

    else:
        inventory = process_delivery(inventory, stock)
        tax = calculate_tax(stock)

        deliveries += 1

        print("Delivery accepted:", stock)
        print("Tax for this delivery:", tax)
        print("Current inventory:", inventory)


generate_report(deliveries, failed_attempts)