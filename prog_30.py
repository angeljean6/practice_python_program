numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        print("Invalid input. Program stopped.")
        break
if numbers:
    total = 0

    for num in numbers:
        total += num

    average = total / len(numbers)

    print("Average is:", average)
else:
    print("No valid numbers were entered.")