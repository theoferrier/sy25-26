grade = 0
weight = int(input("Enter the weight of the potato in grams: "))
if weight < 100:
    grade = "small"
elif weight <= 200:
    grade = "medium"
else:
    grade = "large"
print(f"You have a {grade} potato.")              