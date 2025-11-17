def medication_safety_rule(age):
    weight = float(input("\nEnter the patient's weight in kg: "))
    if age > 12 and weight > 40:
        print("Safe to give medication to.")
    else:
        print("Not safe to give medication to.")
    menu(age)

def fitness_centre_access(age):
    medicalClearance = input("\nDoes the patient have medical clearance to enter the fitness centre? (y/n) ")
    if medicalClearance.upper() == "Y" or age > 18:
        print("The patient may enter the intensive zone.")
    else:
        print("The patient may to enter the intensive zone.")
    menu(age)

def sleep_tracker_alert(age):
    patientStatus = input("\nIs the patient asleep? (y/n) ")
    heartRate = int(input("Enter the patients heart rate: "))
    if patientStatus.upper() == "N"and heartRate > 100:
        print("Alert! Spike in heart rate.")
    menu(age)
    
def menu(age):
    navigating = True
    while navigating:
        print("\n1) Check if patient can be given medication. \n2) Check access to fitness centre intensive zone. \n3) Check heart rate. \n4) Exit program.")
        choice = input(">>")
        if choice == "1":
                navigating = False
                medication_safety_rule(age)
        elif choice =="2":
                navigating = False 
                fitness_centre_access(age)
        elif choice == "3":
                navigating = False
                sleep_tracker_alert(age)
        elif choice == "4":
                navigating = False
                print("Goodbye.")
        else:
             print("Invalid input. Try again.")

age = int(input("Enter the patient's age: "))
menu(age)