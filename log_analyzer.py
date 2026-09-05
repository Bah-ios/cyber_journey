counts = {}
with open("sample.log", 'r') as file:
    count = 0
    for line in file:
        if "Failed password" in line:
            count +=1
            details = line.split(" ")
            key = (details[8],details[10])
            if key in counts:
                counts[key] += 1
            else:
                counts[key] = 1
    for user_info,attempt in counts.items():
        print("{} from {}: {} attempts".format(user_info[0],user_info[1], attempt))
        
    print("Failed login attempts: {}".format(count))
    if count >= 3:
        print("ALERT: possible brute-force attempt detected")
    else:
        print("Activity within normal range")
