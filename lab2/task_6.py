def sort_by_length_desc(tpl):
    return tuple(sorted(tpl, key=len, reverse=True))

N = int(input("How many strings do you want to input? "))
StrTuple = []
for i in range(N):
    s = input(f"Enter string {i + 1}: ")
    StrTuple.append(s)

StrTuple = tuple(StrTuple)
print(f"Original tuple: {StrTuple}")
SortedTuple = sort_by_length_desc(StrTuple)
print(f"Sorted by descending length: {SortedTuple}")
