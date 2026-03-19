numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        print("Invalid input. Program stopped.")
        break
if numbers:
    highest = numbers[0]

    for num in numbers:
        if num > highest:
            highest = num

    print("Highest number is:", highest)
else:
    print("No valid numbers were entered.")