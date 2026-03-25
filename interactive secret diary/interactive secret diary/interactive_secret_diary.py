import datetime

v1 = 'my_diary.tx'
while True:
    print("1. Write, 2. Read, 3. Clear, 4. Exit")
    v2 = input("Select(1-4): ")

    if v2 == '1':  
        v5 = input('Entry: ')  
        v4 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
        with open(v1, 'a') as v3:  
            v3.write(f"[{v4}] {v5}\n")  

    elif v2 == '2':
        try:
            with open(v1, 'r') as v3:  
                v7 = v3.readlines()  
            for v8 in v7:
                print(v8.strip())
        except FileNotFoundError:
            print("Diary file not found.")

    elif v2 == '3':  
        open(v1, 'w').close()  
        print("Diary cleared.")

    elif v2 == '4':  
        break

    else:  
        print("Invalid selection. Please choose 1-4.")