records = "records.txt"

choice = input("What would you like to do. (add, view specific, view all, exit): ")

while choice != "exit":
    if choice == "view all".upper():
        with open(records, "r") as f:
            for line in f:
                print(line.strip())