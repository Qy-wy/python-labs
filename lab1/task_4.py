def money_exchange(amount):
    denominations = [100, 50, 20, 10, 5, 2, 1]
    result = {}
    for denomination in denominations:
         count = amount // denomination
         amount %= denomination
         result[denomination] = count
    print("Amount: ", amount)
    for denomination in denominations:
         if denomination <= 5 :
             print(f"{denomination}: {result[denomination]} coins")
         else :
             print(f"{denomination}: {result[denomination]} banknotes")

number = int(input("Enter the amount: "))
money_exchange(number)

