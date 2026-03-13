odd_count = 0

print("Enter 10 numbers:")

for i in range(10):
    num = int(input(f"Number {i + 1}: "))
    if num % 2 != 0:
        odd_count += 1
print("Number of odd numbers:", odd_count)