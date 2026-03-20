fullname = input("Enter full name: ")
snake_case = "_".join(word.lower() for word in fullname.split())

print("Output:", snake_case)