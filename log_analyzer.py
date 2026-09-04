with open("sample.log", 'r') as file:
    count = 0
    for line in file:
        if "Failed password" in line:
            count +=1
    print("Failed login attempts: {}".format(count))
    if count >= 3:
        print("ALERT: possible brute-force attempt detected")
    else:
        print("Activity within normal range")