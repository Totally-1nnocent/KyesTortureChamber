def rectangle_area_calc(): # calcu;ates area of a rectangle
    width = float(input("Enter the width of the rectangle: "))
    length = float(input("Enter the length of the rectangle: "))
    area = width * length # width and length variables already cast into floats
    print(f"The area of the triangle is {area:.2f}.")

def minute_hour_conversion(): # converts minutes into hours and minutes
    input_minutes = int(input("Enter the number of minutes you would like to convert: "))
    calculated_hours = input_minutes // 60 # calculates the number of hours in the inputted minutes
    remainding_minutes = input_minutes % 60 # finds remaining minutes
    print(f"{input_minutes} minutes is {calculated_hours} hour(s) and {remainding_minutes} minute(s).")

def added_tax_calc(): # calculates added tax
    bill = int(input("Enter the bill amount: ")) # cast into int
    vat = bill * 0.2 # finds 20% of the bill
    print(f"The VAT is {vat:.2f}.")

def billing(): # calculates cost 
    name = input("Enter patient's name: ")
    age = int(input("Enter patient's age: "))
    bill_amount = float(input("Enter the bill amount: "))
    taxed_bill = bill_amount * 1.2
    if age < 18:
        print("You are eligible for a 15% discount.")
        bill_total = taxed_bill * 0.85
    else:
        bill_total = taxed_bill
    print(f"The total bill is £{bill_total:.2f}.")
    if bill_total > 1000:
        print(f"\nPossible payment plan for costs more than £1,000 include: \n - Hospital credit scheme \n - Debt management plan \n - Insured cost \n - Workplace healthcare benefit plans")

def login():
    login_details = {"RachelRaves" : "sw0rdd@nce", "DaveLovesDonuts" : "i82much", "WoohooPizzaMan" : "Regr@veSund@es", "rangofan1" : "justonebu11et", "RavageDaCat" : "SoundwavesBestCassette!1"}
    attempting = True
    username_check = True
    while attempting:
        username = input(f"\nEnter your username: ")
        password = input("Enter your password: ")
        for detail in login_details:
            if username != login_details[detail]:
                username_check = False
        
        if username_check:
            if login_details[username] == password:
                print(f"Login successful.\n")
                attempting = False
            else:
                print(f"Password incorrect. Try again.\n")
        else:
            print(f"Username not found. Try again.\n")

def menu(): # navigate between subprograms
    repeat = True
    while repeat:
        print(f"Enter a to area of a rectangle.\nEnter b to convert minutes into hours and minutes.")
        print(f"Enter c to calculate VAT.\nEnter d to calculate cost.")
        print(f"Enter e to log in. \nEnter f to go to the patient menu. \nEnter x to exit the program.\n")
        choice = input("")
        if choice.upper() == "A":
            repeat = False
            rectangle_area_calc()
        elif choice.upper() == "B":
            repeat = False
            minute_hour_conversion()
        elif choice.upper() == "C":
            repeat = False
            added_tax_calc()
        elif choice.upper() == "D":
            repeat = False
            billing()
        elif choice.upper() == "E":
            repeat = False
            login()
        elif choice.upper() == "F":
            repeat = False
            patient_menu()
        elif choice.upper() == "X":
            repeat = False
        else:
            print("That is an invalid input.")

def patient_menu():
    print(f"Welcome to the patient interface.\n")
    navigating = True
    while navigating:
        print("Press 'a' to eneter patient details.\nPress 'e' to calculate your bmi.\nPress 'l' to calculate medicine dosage.\nPress 'x' to exit the program.\n")
        choose_subprogram = input("")
        if choose_subprogram == "a":
            navigating = False
            print(f"\nPlaceholding entering patient detail program.\n") # call on subprogram would go here
        elif choose_subprogram == "e":
            navigating = False
            print(f"\nPlaceholding calculate bmi program.\n") # call on subprogram would go here
        elif choose_subprogram == "l":
            navigating = False
            print(f"\nPlaceholding calculate medicine dosage program.\n") # call on subprogram would go here
        elif choose_subprogram == "x":
            navigating = False
        else:
            print(f"\nThat is an invalid input.\n")
    print("Goodbye.")

menu()