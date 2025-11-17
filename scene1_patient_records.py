patients = {"Rachel" : [36, 170, "07/12"], "Eva" : [20, 156, "22/05"], "George" : [42, 161, "16/01"]}
def patient_details():
    patient = []
    name = (input("Enter the patients name: "))
    patient.append(input("Enter the patients age: "))
    patient.append(input("Enter the patients height in cm: "))
    patient.append(input("Enter the patients date of birth: (dd/mm) "))
    patients[name] = patient

def bmi_calc():
    weight = float(input("Enter the patients weight in kg: "))
    height = float(input("Enter the patients height in m: "))
    bmi = weight/(height ** 2)
    if bmi < 18.5:
        category = "underweight"
    elif bmi < 25:
        category = "healthy"
    elif bmi < 30:
        category = "overweight"
    elif bmi < 40:
        category = "obese"
    else:
        category = "severly obese"
    print(f"The patients bmi is {bmi}. This is calssed as {category}.")

def med_dose():
    med = input("Which medicine have you given the patient? ")
    givenDose = int(input("Enter the dosage given to the patient today in mg: "))
    patAge = input("Is the patient an adult? (Y/N) ")
    if patAge.upper() == "Y":
        if med.upper() == "PARACETEMOL":
            maxDose = 8000
        elif med.upper() == "IBUPROFEN":
            maxDose = 5000
        elif med.upper() == "MORPHINE":
            maxDose = 1500
    elif patAge.upper() == "N":
        if med.upper() == "PARACETEMOL":
            maxDose = 4000
        elif med.upper() == "IBUPROFEN":
            maxDose = 2500
        elif med.upper() == "MORPHINE":
            maxDose = 0
    
    if givenDose > maxDose:
        lessDrugs = givenDose - maxDose
        print(f"The patient has exceeded the max recommended dose by {lessDrugs}mg.")
    else:
        moreDrugs = maxDose - givenDose
        print(f"The max dose is {maxDose}. The patient can have {moreDrugs}mg more.")

def billing():
    overnight = input("Did the patient stay in the hospital overnight? (y/n) ")
    if overnight.upper() == "Y":
        room = input("What kind of room did they stay in? ")
        stay = int(input("How many days did the patient stay? "))
        if room.upper() == "PRIVATE":
            roomType = 260
        elif room.upper() == "SHARED":
            roomType = 172
        roomCost = stay * roomType
    consultation = int(input("How many doctor consultations did the patient attend? "))
    consCost = consultation * 150
    treatCost = float(input("How much did the patients treament cost? £"))
    totalCost = roomCost + consCost + treatCost
    totalBill = totalCost * 1.2
    print(f"The total cost is £{totalBill:.2f}.")

def menu():
    print("Welcome to the EHR.")
    print("----------")
    print("Enter a to enter patient details")
    print("Enter b to calculate dosage")
    print("Enter c to calculate the bill")
    print("Enter d to calculate bmi")
    choice = input("")
    if choice.upper() == "A":
        patient_details()
    elif choice.upper() == "B":
        med_dose()
    elif choice.upper() == "C":
        billing()
    elif choice.upper() == "D":
        bmi_calc()
    else:
        print("That is an invalid choice.")
        print("")
        menu()

menu()