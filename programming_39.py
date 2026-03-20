fullname = input("Enter your full name: ")
pascal_case = "".join(word.capitalize() for word in fullname.split())
print("Output:", pascal_case)
