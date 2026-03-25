from re import A


choice = input("What would you like to do. (view all, view specific, update record, exit): ")
print(" ")
while True:
    if choice == "view all":
        print("-----------------------------------------------------------------------------")
        print("All Records:")
        with open("records.txt", "r") as f:
            for line in f:
                print(line.strip())
        print(" ")
        choice = input("What would you like to do. (edit, view specific, view all, exit): ")
    elif choice == "view specific":
        event = input("Enter the event name (all lowercase and add boys/girls at the end for whatever gender you want): ")
        with open(records, "r") as f:
            show = False
            for line in f:
                if line.strip() == f"event: {event}":
                    show = True
                elif line.startswith("event: ") and show:
                    break
                if show:
                    print(line.strip())
    elif choice == "update record":
        event = input("Enter the event name (all lowercase and add boys/girls at the end for whatever gender you want): ")
        with open("records.txt", "r") as f:
            lines = f.readlines()
        show = False
        for line in lines:
            if line.strip() == f"event: {event}":
                show = True
            elif line.startswith("event: ") and show:
                break
            if show:
                print(line.strip())
        confirm = input("Are you sure you want to update this record? (yes/no):")
        if confirm == "yes":
            new_name = input("Enter new athlete name: ")  
            new_grade = input("Enter new grade: ")  
            new_result = input("Enter new result: ")  
            for i in range(len(lines)):
                if lines [i].strip() == f"event: {event}":
                    lines[i+1] = f"name: {new_name}\n"
                    lines[i+2] = f"grade: {new_grade}\n"
                    lines[i+3] = f"result: {new_result}\n"
                    break

            with open("records.txt", "w") as f:
                f.writelines(lines)
            print("Record updated successfully.")
            another = input("Do you want to update another record? (yes/no): ")
            if another == "yes":
                choice = "update record"
            elif another == "no":
                choice = input("What would you like to do. (view all, view specific, update record, exit): ")
        else:
            print("Update cancelled.")
            print(" ")
            update_different = input("Do you want to update a different record? (yes/no): ")
            print(" ")
            if update_different == "yes":
                choice = "update record"
            elif update_different == "no":
                choice = input("What would you like to do. (view all, view specific, update record, exit): ")
    elif choice == "exit":
        print("Thanks for using our program!")
        break