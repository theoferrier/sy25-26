from calendar import c


E3 = ["E3","Skoda Octavia WRC",230,("221/300"),7500,5.3,2000,4]
D3 =["D3", "Seat Toledo Marathon", 220, ("195,330"), 8400, 5.2, 2100, 5]

cars = [E3,D3]

def print_car(c):
    print("_________________________________")
    print(f"| {c[0]} | {c[1]}        |")
    print("|-------------------------------|")
    print("|                               |")
    print("|            __________         |")
    print("|           //   ||\   \        |")
    print("|    ______//____||_\   \__     |")
    print("|   | __               __  \    |")
    print("|   |/  \_____________/  \_|    |")
    print("|    \__/             \__/      |")
    print("|_______________________________|")
    print("|  Top Speed:  | 0 to 100 kM/h: |")
    print(f"|     {c[2]}      |      {c[5]}       |")
    print("|--------------|----------------|")
    print("|Horsepower in |                |")
    print("|    kW/hp:    |  Engine cc's:  |")
    print(f"|   {c[3]}    |      {c[6]}      |")
    print("|--------------|----------------|")
    print("|     RPM:     |   Cylinders:   |")
    print(f"|     {c[4]}     |       {c[7]}        |")
    print("|______________|________________|")


i = 1
for c in cars:
    print(i, c[1])
    i = i + 1
    print(" ")

choice = int(input("Select a car to view details by the number in front: "))
if choice == 1:
    print_car(E3)
elif choice == 2:
    print_car(D3)