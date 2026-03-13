total = 0
print("enter 10 numbers:")

for i in range(10):
    num = float(input(f"Number {i + 1}: "))
    total += num

print("The sum of the 10 numbers is:", total)