def find_intersection(set1, set2):
    return set1.intersection(set2)

N1 = int(input("How many elements in the first set? "))
Set1 = set()
for i in range(N1):
    el = input(f"Enter element {i + 1} for the first set: ")
    Set1.add(el)

N2 = int(input("How many elements in the second set? "))
Set2 = set()
for i in range(N2):
    el = input(f"Enter element {i + 1} for the second set: ")
    Set2.add(el)

print(f"First set: {Set1}")
print(f"Second set: {Set2}")
print(f"Intersection: {find_intersection(Set1, Set2)}")