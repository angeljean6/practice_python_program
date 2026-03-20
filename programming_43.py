text = input("Enter a string: ")

result = ""

for ch in text:
    ascii_val = ord(ch)

# If uppercase A-Z, convert to lowercase
    if 65 <= ascii_val <= 90:
        result += chr(ascii_val + 32)
    else:
        result += ch