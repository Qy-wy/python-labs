def delete_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ""
    for char in string:
        if char not in vowels:
            result += char
    print("Result: ", result)

text = input("Enter the string: ")
delete_vowels(text)