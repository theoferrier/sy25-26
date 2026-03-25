
stock_count = int(input("How many items are in stock? "))

if stock_count == 0:
    print("Out of stock")
elif stock_count <= 5:
    print("Low stock reorder soon")
else:
    print("In stock")

sum = 0
for i in range(0, 51, 2):
    sum = sum + i
print("The sum of all even numbers from 0 to 50 is:", sum)