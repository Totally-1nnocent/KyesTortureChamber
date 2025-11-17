def calorie_burn():
    workoutTime = int(input("\nEnter the number of minutes you have worked out for: "))
    caloriesPerMin = float(input("Enter the calories you burned per minute during your workout: "))
    calorieBurn = workoutTime * caloriesPerMin
    print(f"\nYou have burned {calorieBurn:.2f} calories.")
    menu()

def step_conversion():
    steps = int(input("\nEnter the number of steps you have walked today: "))
    distance = steps / 1300
    print(f"\n{steps} steps in km is {distance:.2f}km.")
    menu()

def medication_timing():
    minutes = int(input("\nEnter the number of minutes until the next dose: "))
    hours = minutes // 60
    excessMinutes = minutes % 60
    print(f"\n{minutes} minutes is {hours} hours and {excessMinutes} minutes.")
    menu()

def medicine_pack_usage():
    packs = int(input("\nEnter the number of packs do you have for distribution: "))
    tabletsPerPack = int(input("Enter the number of tablets in each pack: "))
    totalTablets = packs * tabletsPerPack
    usedTablets = int(input("Enter the number of tablets distributed: "))
    remainingTablets = totalTablets - usedTablets
    remainingPacks = remainingTablets // tabletsPerPack
    leftoverTablets = remainingTablets % tabletsPerPack
    print(f"\nYou will have {remainingPacks} packs and {leftoverTablets} tablets left after distribution.")
    menu()

def heart_recovery():
    timer = 0
    heartRate = int(input("\nEnter your current heartrate: "))
    restingRate = int(input("Enter your resting heart rate: "))
    print("")
    while heartRate > restingRate:
        timer = timer + 1 
        heartRate = heartRate * (0.9 ** 5)
        print(f"After {timer} minutes, your heart rate will be {heartRate:.2f}.")
    print(f"\nAfter {timer} minutes, your heart rate will return to normal.")
    menu()

def menu():
    navigating = True
    print("\n1) Calculate calories burnt. \n2) Convert steps to km. \n3) Calculate timing for medication in hours and minutes.\n4) Calculate remaing packs of medicine after distribution.\n5) Calculate time until heart rate returns to normal.\n6) Exit the program.")
    choice = input("\n>> ")
    while navigating:
        match choice:
            case "1":
                navigating = False
                calorie_burn()
            case "2":
                navigating = False
                step_conversion()
            case "3":
                navigating = False
                medication_timing()
            case "4":
                navigating = False
                medicine_pack_usage()
            case "5":
                navigating = False
                heart_recovery()
            case "6":
                navigating = False
                print("Goodbye.")
                exit()
        print("That is not a valid input.")

menu()