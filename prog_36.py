fullname = input("Enter your full name: ")
reverse_case = ""
for ch in fullname:
    if ch.islower():
        reverse_case += ch.upper()
    elif ch.isupper():
        reverse_case += ch.lower()
    else:
        reverse_case += ch 