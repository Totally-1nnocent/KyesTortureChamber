#oxygen = int(input("Enter the oxygen level: "))
#if oxygen < 95:
    #print("The oxygen is less than 95.")

#glucose = float(input("Enter the oxygen level: "))
#if glucose > 7.0:
    #print("The glucose is more than 7.")

#heartRate = int(input("Enter the oxygen level: "))
#if heartRate == 70:
    #print("The heart rate is 70.")

def vital_signs_monitor():
    def temp_checker():
        temperature = int(input("Enter the patients temperature: "))
        if temperature > 37.5:
            print("The patient is overheating.")
    def oxygen_checker():
        oxygen = int(input("Enter the patients oxygen: "))
        if oxygen < 92:
            print("The patient's oxygen is low.")
    def heart_rate_checker():
        heartRate = int(input("Enter the patients patients heart rate: "))
        if heartRate >= 60 and heartRate <= 100:
            print("The patient's heart rate is normal.")
    def monitor_menu():
        navigating = True
        print("\n1) Check temperature.\n2) Check oxygen.\n3) Check heart rate.\n4) Exit.")
        choice = input("")
        while navigating:
            match choice:
                case "1":
                    navigating = False
                    temp_checker()
                case "2":
                    navigating = False
                    oxygen_checker()
                case "3":
                    navigating = False
                    heart_rate_checker()
                case "4":
                    navigating = False
                    exit()
                case else:
                    print("£")
    monitor_menu()

vital_signs_monitor()