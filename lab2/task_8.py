def remove_duplicates(lst):
    unique_items = []
    for item in lst:
        if lst.count(item) == 1:
            unique_items.append(item)
    return unique_items

N = int(input("How many numbers do you want to input? "))
Lst = []
for i in range(N):
    num = int(input(f"Enter the number {i + 1}: "))
    Lst.append(num)

print(f"The original list is: {Lst}")
filtered_list = remove_duplicates(Lst)
print(f"List after removing duplicates: {filtered_list}")