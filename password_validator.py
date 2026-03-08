password = input("Enter the password: ")

if len(password) >= 8:
    if password != password.lower() and password != password.upper():
        if any(char.isdigit() for char in password):
            print("Password is strong")
        else:
            print("Password must contain a number")
    else:
        print("Password must contain uppercase and lowercase letters")
else:
    print("Password must be at least 8 characters long")
