numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        print("Invalid input. Program stopped.")
        break
if numbers:
    most_duplicate = numbers[0]
    highest_count = numbers.count(numbers[0])

    for num in numbers:
        count = numbers.count(num)
        if count > highest_count:
            highest_count = count
            most_duplicate = num
    print("Number with most duplicates:", most_duplicate)
    print("Number of occurrences:", highest_count)
else:
    print("No valid numbers were entered.")