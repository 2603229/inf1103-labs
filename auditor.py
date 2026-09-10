inventory = 0
n = 1
storage = 0
error = 0


while n ==1:
    if storage < 500:
        stock = input("Enter stock quantity (Quit to stop): ").upper()
        if stock == "QUIT":
            print("Total Units Processed:", str(storage))
            print("Number of Failed/Rejected Entries:", str(error))
            n = 0
        elif stock.isdigit():
            stock = int(stock)
            storage = storage + stock
        else:
            print("Error, try again")
            error = error + 1

    else:
        storage = storage - stock
        print("Total inventory exeeds 500 units")
        print("Only processed", str(storage), "units")
        n = 0

