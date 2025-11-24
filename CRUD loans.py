#Create Read Update Delete

import datetime

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
        while type(updateData) != bool:
            try:
                bool(updateData)
            except:
                print("Sorry, this field can only be a boolean.")
                updateData = input(f"Enter the data you would like to change the {updateField} field to: ")
            else:
                bool(updateData)
    else:
        while True:
            try:
                datetime.datetime.strptime(f"{updateData}", "%Y-%m-%d")
            except:
                print("Sorry, this date is invalid. Please input in the YYYY-MM-DD format.")
                updateData = input(f"Enter the data you would like to change the {updateField} field to: ")
            else:
                break

#def delete_loans(loans):

update_loans(loans)