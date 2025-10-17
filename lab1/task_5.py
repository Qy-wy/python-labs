def magic_number(number):
    if number % 7 == 0:
        print("Magic number!")
    else:
        digit_sum = 0
        for digit in str(abs(number)):
            digit_sum += int(digit)
        print("Digit sum: ", digit_sum)

num = int(input("Enter the number: "))
magic_number(num)