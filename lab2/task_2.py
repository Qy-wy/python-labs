def get_list():
    string = input("Enter the strings devided by coma: ")
    return string.split(",")

def get_string_A():
    parts = get_list()
    for part in parts:
        if part[0]=="A":
            print(part)

get_string_A()