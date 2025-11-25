#Create Read Update Delete

from datetime import datetime

loans =[
    {"loan_id":1, "student_name":"Alex Green", "student_id":"S12345", "device_type":"Laptop", "device_id":"L-001", "date_out":"2025-11-24", "due_back":"2025-12-01", "returned":False},
    {"loan_id":2, "student_name":"Regan Keenes", "student_id":"S54321", "device_type":"Tablet", "device_id":"T-001", "date_out":"2025-11-25", "due_back":"2025-12-02", "returned":False}
    ]

def search_and_view_loans(loans):
    searchedId = input("Enter the ID of the loan you would like to view: ")
    checking = True
    while checking:
        try:
            int(searchedId)
        except:
            print("Sorry, that ID is invalid. Try again.")
            searchedId = input("Enter the ID of the loan you would like to view: ")
        else:
            checking = False
    found = False
    while found == False:
        for i in range(0, len(loans)):
            if loans[i]["loan_id"] == int(searchedId):
                print(loans[i])
                found = True
        if found == False:
            print(f"'{searchedId}' could not be found. Try another loan ID.")
            searchedId = input("Enter the ID of the loan you would like to view: ")

def update_loans(loans):
    updateId = input("Enter the loan ID of the loan you would like to edit: ") 
    checking = True
    while checking:   
        try:
            int(updateId)
        except:
            print("Sorry, that ID is invalid.")
            updateId = input("Enter the loan ID of the loan you would like to edit: ")    
        else:
            checking = False
    updateField = input("Enter the field you would like to update (due_back/returned): ")
    while updateField.upper() != "DUE_BACK" and updateField.upper() != "RETURNED":
        print("Sorry, that input is invalid. Please enter due_back or returned.")
        updateField = input("Enter the field you would like to update (due_back/returned): ")
    updateData = input(f"Enter the data you would like to change the {updateField} field to: ")
    if updateField.upper() == "RETURNED":
        looper = True
        while looper:
            if updateData.upper() != "TRUE" and updateData.upper() != "FALSE":
                print("Sorry, this input is invalid.")
                updateData = input(f"Enter the data you would like to change the {updateField} field to: ")
            elif updateData.upper() == "FALSE":
                updateData = ""
                looper = False
                updateData = bool(updateData)
            else:
                updateData = bool(updateData)
                looper = False
    else:
        while True:
            try:
                datetime.datetime.strptime(f"{updateData}", "%Y-%m-%d")
            except:
                print("Sorry, this date is invalid. Please input in the YYYY-MM-DD format.")
                updateData = input(f"Enter the data you would like to change the {updateField} field to: ")
            else:
                break
    for i in range(0, len(loans)):
            if loans[i]["loan_id"] == int(updateId):
                updateIndex = i
    loans[updateIndex][updateField] = updateData

def delete_loans(loans):     
    deletedId = input("Enter the ID of the loan you would like to delete: ")     
    validating = True
    while validating:
        try:
            int(deletedId)
        except:
            print("Sorry, this is an invalid input.")       
            deletedId = input("Enter the ID of the loan you would like to delete: ")     
        else:
            validating = False
            found = False
            for i in range(0, len(loans)):
                if loans[i]["loan_id"] == int(deletedId):
                    deletedIndex = i
                    found = True
            if not found:
                print("Sorry, this ID could not be found.")
                validating = True
    print(loans[deletedIndex])
    confirmation = input("Are you sure you would like to delete this loan? (y/n) ")
    while validating == False:
        if confirmation.upper() != "Y" and confirmation.upper() != "N":
            print("Sorry this is an invalid input. Please input Y or N.")
            confirmation = input("Are you sure you would like to delete this loan? (y/n) ")
        else:
            validating = True
    if confirmation.upper() == "Y":
        loans.remove(loans[deletedIndex])
    else:
        print("This loan has not been removed.")
    deleteAgain = input("Would you like to delete another loan? (y/n) ")
    if deleteAgain.upper() == "Y":
        delete_loans(loans)

def add_loans(loans):
    addedId = int(loans[-1]["loan_id"]) + 1
    addedStudent = input("Enter the name of the student who is taking out the loan: ")
    addedStudId = input("Enter the ID of the student: ")
    addedDevice = input("Enter the type of device the loan is for: ")
    addedDevId = input("Enter the ID of this device: ")
    addedDate = datetime.strptime(f"{datetime.now()}", "%Y-%m-%d")
    try:
        addedReturn =  addedDate.replace(year = addedDate.year + 1)
    except ValueError:
        addedReturn = addedDate + (datetime(addedDate.year + 1, 1, 1) - datetime(addedDate.year, 1, 1))
    addedDict = {"loan_id":addedId, "student_name":addedStudent, "student_id":addedStudId, "device_type":addedDevice, "device_id":addedDevId, "date_out":addedDate, "due_back":addedReturn, "returned":False}
    print(addedDict)
    confirmation = input("Would you like to add this loan? (y/n) ")
    validating = True
    while validating:
        if confirmation.upper() not in ("Y", "N"):
            print("Sorry this input is invalid. Please enter Y or N.")
            confirmation = input("Would you like to add this loan? (y/n) ")
        elif confirmation.upper() == "Y":
            validating = False
            loans.append(addedDict)
        else:
            validating = False
            print("This loan will not be added.")
        
add_loans(loans)