def is_palindrome(string):
    new_string = string.replace(" ", "").lower()

    length = len(new_string)

    for i in range(length//2):
        if new_string[i] != new_string[-i-1]:
            return False

    return True

text = input("Enter the string: ")
if is_palindrome(text):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")