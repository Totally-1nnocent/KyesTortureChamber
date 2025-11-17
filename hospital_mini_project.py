def lab_results(): # converts mmol/L to mg/dL and vice versa
    type = input("What kind of test have you conducted? ")
    val = int(input("Enter the numerical outcome of the test: "))
    unit = input("Which unit is this in? (mg/dL / mmol/L) ")
    if type.upper() != "GLUCOSE" and type.upper() != "CHOLESTERAL": # not case sensitive
        print("This test type is not on the system currently.")
    elif unit.upper() != "MG/DL" and unit.upper() != "MMOL/L": # not case sensitive
        print("This is not a valid unit.")
    else:
        if unit.upper() == "MG/DL":
            converted = val / 18
            print(f"{val} {unit} in mmol/L is {converted}")
        else:
            converted = val * 18
            print(f"{val} {unit} in mg/dL is {converted}")

def average_temp(): # calculates averages of inputted values
    MAXTEMP = 50 # a constant
    temperatures = []
    read1 = float(input("Enter the patients first temperature: "))
    if read1 < 30 or read1 > 45:
        print("This is not a valid temperature.")
        average_temp()
    read2 = float(input("Enter the patients second temperature: "))
    if read2 < 30 or read2 > 45:
        print("This is not a valid temperature.")
        average_temp()
    read3 = float(input("Enter the patients third temperature: "))
    if read3 < 30 or read3 > 45:
        print("This is not a valid temperature.")
        average_temp()
    temperatures.append(read1)
    temperatures.append(read2)
    temperatures.append(read3)
    totalTemp = 0
    for x in range(len(temperatures)):
        totalTemp = totalTemp + temperatures[x]
    average = totalTemp / len(temperatures)
    print(f"The patients average temperature is {average:.2f}.")
    if average > MAXTEMP:
        difference = average - MAXTEMP
        print(f"The patient's average temperature is above the temperature threshold by {difference:.2f}.")

def heart_rate(): # calculates if a patient's resting heart rate is too high or too low
    check = ""
    while check.upper() != "N":
        name = input("Enter the patients name: ")
        age = int(input("Enter the patient's age: "))
        restRate = int(input("Enter the patients resting heart rate: "))
        maxRate = 220 - age
        if restRate >= (maxRate - 30):
            rateType = "high"
        elif restRate < 130:
            rateType = "low"
        else:
            rateType = "medium"
        print(f"{name}'s maximum heart rate is {maxRate}, and their resting heart rate is {rateType}.")
        check = input("Would you like to contiue entering names? (y/n) ")

def hydration_station(): # calculates if a patient has had enough water and if not how much more they need
    water = int(input("Enter the patient's daily water intake in L: "))
    DAILYGOAL = 1.5
    if water >= DAILYGOAL:
        print("The patient has met their daily water intake goal.")
    else:
        diff = DAILYGOAL - water
        print(f"The patient has not yet met their daily water intake goal, they require {diff}L more to meet it.")

def billing(): # Calulates cost of hospital trip
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

def patient_records(total_patients): # navigate functions in patient record
    choicemade = True
    while choicemade:
        print("\nEnter a if you would like to add a new patient to the system.\nEnter b to view the number of patients.\nEnter c to reset the number of patients.\nEnter d to return to the main menu.\n")
        patientRecordNav = input("")
        if patientRecordNav.upper() == "A":
            choicemade = False
            total_patients = add_patient(total_patients)
        elif patientRecordNav.upper() == "B":
            choicemade = False
            view_total(total_patients)
        elif patientRecordNav.upper() == "C":
            total_patients = choicemade = False
            reset_patients(total_patients)
        elif patientRecordNav.upper() == "D":
            total_patients = choicemade = False
            menu()
        else:
            print("That is an invalid input.")

def add_patient(total_patients):
    total_patients += 1
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    print(f"\nPatient added: {name} \n")
    patient_records(total_patients)
    return total_patients

def view_total(total_patients):
    print(f"\nTotal patients: {total_patients}\n")
    patient_records(total_patients)

def reset_patients(total_patients):
    total_patients = 0
    print(f"\nTotal patients is now {total_patients}\n")
    patient_records(total_patients)
    return total_patients

def patient_menu():
    print(f"Welcome to the patient interface.\n")
    navigating = True
    while navigating:
        print("Enter a to enter patient details.\nEnter b to calculate your bmi.\nEnter c to calculate medicine dosage.\nEnter d to return to the main menu. \nEnter x to exit the program.\n")
        choose_subprogram = input("")
        if choose_subprogram.upper() == "A":
            navigating = False
            print(f"\nPlaceholding entering patient detail program.\n") # call on subprogram would go here
        elif choose_subprogram.upper() == "B":
            navigating = False
            print(f"\nPlaceholding calculate bmi program.\n") # call on subprogram would go here
        elif choose_subprogram.upper() == "C":
            navigating = False
            print(f"\nPlaceholding calculate medicine dosage program.\n") # call on subprogram would go here
        elif choose_subprogram.upper() == "D":
            navigating = False
            menu()
        elif choose_subprogram.upper() == "X":
            navigating = False
        else:
            print(f"\nThat is an invalid input.\n")
    print("Goodbye.")

def menu(): # navigate between subprograms
    repeat = True
    print("Welcome to my mini hospital project.\n")
    while repeat:
        print("Enter a to covert lab results.\nEnter b to covert calculate average temperature.")
        print("Enter c to check heart rate.\nEnter d to check hydration.")
        print("Enter e to calculate the cost of a hospital trip.\nEnter f to access patient records.\nEnter g to go to the patient menu.\nEnter x to exit the program.\n")
        choice = input("")
        if choice.upper() == "A":
           lab_results()
        elif choice.upper() == "B":
         average_temp()
        elif choice.upper() == "C":
          heart_rate()
        elif choice.upper() == "D":
          hydration_station()
        elif choice.upper() == "E":
            billing()
        elif choice.upper() == "F":
            patient_records(0)
        elif choice.upper() == "G":
            patient_menu()
        elif choice.upper() == "X":
            repeat = False
        else:
            print("That is an invalid input.")

menu()