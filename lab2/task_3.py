def make_devisors_dict(n):
    d = {}
    for i in range(1, n+1):
        counter = 0
        for j in range(1, i+1):
            if i%j == 0:
                counter += 1
        d[i] = counter
    return d

N = int(input("Enter N: "))
print(make_devisors_dict(N))