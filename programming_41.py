text = input("Enter text with leading spaces: ")

i = 0
while i < len(text) and text[i] == " ":
    i += 1

result = text[i:]
print("Output:", result)