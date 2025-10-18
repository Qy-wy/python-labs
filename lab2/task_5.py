def find_min_in_list(lst):
    min_item = lst[0]
    for item in lst:
        if item < min_item:
            min_item = item
    return min_item

N = int(input("How many numbers do you want to input? "))
Lst = []
for i in range(N):
    num = int(input(f"Enter the number {i + 1}: "))
    Lst.append(num)
print(f"The list is: {Lst}")
print(f"Min element is: {find_min_in_list(Lst)}, index of min element is: {Lst.index(find_min_in_list(Lst))}")