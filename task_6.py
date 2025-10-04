def count_amount_of_substance():
    print("Enter the pressure in pascals")
    pressure = float(input())

    print("Enter the temperature in Kelvin")
    temperature = float(input())

    print("Enter the volume in m^3")
    volume = float(input())

    R = 8.31

    if temperature <=0 :
        print("The temperature must be more than 0 K")
        return

    amount_of_substance = pressure * volume / (temperature * R)
    print("The amount of substance is", amount_of_substance)

count_amount_of_substance()