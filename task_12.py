def count_phone_bill():
    t_minutes = 60
    t_sms = 30
    t_mb = 1024
    t_price = 24.99

    extra_minutes_price = 0.89
    extra_sms_price = 0.59
    extra_mb_price = 0.79
    tax_rate = 0.02

    minutes = int(input("Enter number of minutes used: "))
    sms = int(input("Enter number of sms: "))
    mb = int(input("Enter number of mb: "))

    extra_minutes = minutes - t_minutes
    extra_sms = sms - t_sms
    extra_mb = mb - t_mb
    extra_price = 0.0

    if extra_minutes > 0:
        print(f"Extra minutes ({extra_minutes} min): {extra_minutes * extra_minutes_price:.2f} RUB")
        extra_price += extra_minutes * extra_minutes_price
    if extra_sms > 0:
        print(f"Extra SMS ({extra_sms} messages): {extra_sms * extra_sms_price:.2f} RUB")
        extra_price += extra_sms * extra_sms_price
    if extra_mb > 0:
        print(f"Extra data ({extra_mb} MB): {extra_mb * extra_mb_price:.2f} RUB")
        extra_price += extra_mb * extra_mb_price

    tax = (extra_price + t_price) * tax_rate
    print(f"Tax (2%): {tax:.2f} RUB")

    total_price = t_price + extra_price + tax
    print(f"Total amount: {total_price:.2f} RUB")

count_phone_bill()