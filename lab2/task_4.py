def print_odd_num(N):
    for i in range(N+1):
        if i%2 != 0:
            print(i)

n = int(input("Enter a number: "))
print_odd_num(n)
