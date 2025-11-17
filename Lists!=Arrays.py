def energy_levels():
    energyList = []
    for i in range(0,5):
        energyList.append(input(f"Enter the {i+1} energy reading of the day: "))
    print("\n", energyList)
    print("\n", energyList[0], "\n", energyList[round(len(energyList)/2)], "\n", energyList[round(len(energyList) - 1)])

def username_list():
    usernames = []
    for i in range(0,5):
        usernames.append(input(f"Enter the {i+1} username: "))
    print("\n", usernames)
    print("\n", usernames[0], "\n", usernames[round(len(usernames)/2)], "\n", usernames[round(len(usernames) - 1)])
    
def step_count_values():
    stepCounts = []
    for i in range(0,5):
        stepCounts.append(input(f"Enter the {i+1} energy reading of the day: "))
    print("\n", stepCounts)
    print("\n", stepCounts[0], "\n", stepCounts[round(len(stepCounts)/2)], "\n", stepCounts[round(len(stepCounts) - 1)])

def screen_activity():
    screen_times = [120, 95, 140, 160, 80, 100, 200]
    print(f"The value of the second day {screen_times[2]}.")
    print(f"The average of the first three days is {(screen_times[0] + screen_times[1] + screen_times[2])/3}.")
    screen_times[len(screen_times)-1] = int(input("Enter the replacement for the final value: "))
    print(f"The highest value is {min(screen_times)}.")
    print(f"The lowest value is {max(screen_times)}.")

def mixed_lists():
    listA = [1, 2, 3]
    listB = [1, "2", 3.0]
    #still prints mixed lists without error
    #min max cannot compare diiffernt data types
    #traditional arrays only have one data type
    #lists are useful for data that is recorded as different data types

def notification_numbers():
    notificationsA = [34, 28, 55, 40, 60, 22, 18]
    notificationsB = [65, 3, 34, 87, 13, 76, 12]
    total = 0
    for i in range(0, len(notificationsA)):
        print(f"Number of notifications on day {i + 1}: {notificationsA[i]}.")
        total = total + notificationsA[i]
    average = total / len(notificationsA)
    print(f"\nThe total number of notifications is {total} and the average is {average:.2f}.\n")
    for x in range(0, len(notificationsA)):
        if notificationsA[x] > notificationsB[x]:
            print(f"On day {x + 1}, you had more notifications than user B.")
        elif notificationsA[x] < notificationsB[x]:
            print(f"On day {x + 1}, you had less notofications than user B.")
        else:
            print(f"On day {x + 1}, you had the same amount of notifications as user B.")
    print(f"\nThe day with the highest number of notifications was {notificationsA.index(max(notificationsA))}, with {max(notificationsA)} notifications.")
    print(f"The day with the lowest number of notifications was {notificationsA.index(min(notificationsA))}, with {min(notificationsA)} notifications.")
    notificationsA.append(int(input("Enter the number of notifications today: ")))
    print(f"The new list is: \n {notificationsA}.")

def menu():
    print("1. Enter energy readings. \n2. Enter usernames. \n3. Enter step counts. \n4. Screen activity. \n5. Mixed list activity \n6. Check notifications. \n7. Exit.")
    choice = input("\n>>>> ")
    match choice:
        case "1":
            energy_levels()
        case "2":
            username_list()
        case "3":
            step_count_values()
        case "4":
            screen_activity()
        case "5":
            mixed_lists()
        case "6":
            notification_numbers()
        case "7":
            exit()

menu()