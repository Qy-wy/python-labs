def print_sum_of_squares(n):
    sum = 0
    for i in range(1,n+1):
        sum += i*i
    print(f"the sum of squares from  to {n}: {sum}")

N = int(input("Enter the N: "))
print_sum_of_squares(N)