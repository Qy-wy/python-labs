def check_password(password):
    if len(password) < 16:
        return "Too short"
    elif password.isdigit() or password.isalpha():
        return "Too weak"
    else:
        return "Great password"

text = input("Enter the password: ")
print("Result: ", check_password(text))