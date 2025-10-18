def count_a_in_string(string):
    count = 0
    for char in string:
        if char == "a":
            count += 1
    return count

s = input("Enter the string: ")
print(f"The quantity of a: {count_a_in_string(s)}")