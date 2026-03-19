numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        print("Invalid input. Program stopped.")
        break
if numbers:
    lowest = min(numbers)
    print("Lowest number is:", lowest)
else:
    print("No valid numbers were entered.")