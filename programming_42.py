text = input("Enter text: ")
prefix = input("Enter prefix to remove: ")

if text[:len(prefix)] == prefix:
    result = text[len(prefix):]
else:
    result = texts
