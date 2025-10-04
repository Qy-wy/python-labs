def format_time(seconds):
    minutes = seconds // 60
    seconds -= minutes * 60

    print(f"{minutes} minute(s) and {seconds} second(s)")

time = int(input("Enter the seconds: "))
format_time(time)
