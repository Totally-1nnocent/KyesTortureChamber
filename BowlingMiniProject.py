import datetime

weekAvailability = {
    "Monday":{"12:00" : False, "13:00" : False, "14:00" : False, "15:00" : False, "16:00" : True, "17:00" : True, "18:00" : False, "19:00" : False}, 
    "Tuesday":{"12:00" : True, "13:00" : True, "14:00" : True, "15:00" : False, "16:00" : True, "17:00" : True, "18:00" : False, "19:00" : False}, 
    "Wednesday":{"12:00" : False, "13:00" : False, "14:00" : False, "15:00" : False, "16:00" : True, "17:00" : True, "18:00" : False, "19:00" : False}, 
    "Thursday":{"12:00" : False, "13:00" : False, "14:00" : False, "15:00" : False, "16:00" : True, "17:00" : True, "18:00" : False, "19:00" : False}, 
    "Friday":{"12:00" : True, "13:00" : True, "14:00" : True, "15:00" : True, "16:00" : True, "17:00" : True, "18:00" : False, "19:00" : False}, 
    "Saturday":{"12:00" : True, "13:00" : True, "14:00" : True, "15:00" : True, "16:00" : True, "17:00" : True, "18:00" : True, "19:00" : True}
    }#add lanes later?

def booking(weekAvailability): #edit array to check and update avilability
    bookingDay = input("Enter the day of the week you would like to book: ").capitalize()
    flag = True
    checking = True
    timeformat = "%H:%M"
    while flag:
        bookedBlocks = 0
        for item in weekAvailability[bookingDay].values():
            if item: #checks if the day is fully booked
                bookedBlocks = bookedBlocks + 1
        if bookedBlocks == 8:
            print(f"Sorry. We are all booked for {bookingDay}. Try another day.")
            bookingDay = input("Enter the day of the week you would like to book: ") #loops until a day is not fully booked is entered
        else:
            flag = False
    for key in weekAvailability[bookingDay]:
        if weekAvailability[bookingDay][key]:
            timeAvailable = "Booked"
        else:
            timeAvailable = "Available"
        print(f"{key} : {timeAvailable}")
    while checking:
        bookingTime = input("Enter the time you would like to book beginning from (hh:mm): ")
        try:
            datetime.datetime.strptime(bookingTime, timeformat)
            checking = False
        except ValueError:
            bookingTime = input("Enter the time you would like to book beginning from (hh:mm): ")
    bookingLength = int(input("Enter how long you would like your booking to last in hours (min 1 hr): "))
    flag = True
    while flag:
        if bookingLength < 0 or bookingLength > 8: #checks hours is less than an hour or longer than a day
            print("Sorry, this is an invalid amount of time. Try again.")
            bookingLength = int(input("Enter how long you would like your booking to last in hours (min 1 hr): "))
        else:
            flag = False
    for i in range(0,bookingLength):
        time = f"1{int(bookingTime[1])+i}:00"
        weekAvailability[bookingDay][time] = True
    for key in weekAvailability[bookingDay]:
        if weekAvailability[bookingDay][key]:
            timeAvailable = "Booked"
        else:
            timeAvailable = "Available"
        print(f"{key} : {timeAvailable}")
    return weekAvailability

#def proccess_orders(): #c


#def calculate_prices(): #input orders and booking in order to calculate price


#def reciept(): #display calculated prices

booking(weekAvailability)