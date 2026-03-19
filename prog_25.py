numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        print("Invalid input. Program stopped.")
        break

numbers.sort()

print("Numbers from lowest to highest:")
print(numbers)