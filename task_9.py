def check_IP(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        if int(part) < 0 or int(part) > 255:
            return False

    return True

IP = input("Enter the IP: ")
if check_IP(IP):
    print("Your input is correct IP")
else:
    print("Your input is not the IP")
