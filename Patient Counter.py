def add_patient(total_patients):
    total_patients += 1
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    print("Patient added:", name)
    print(total_patients)
    return total_patients

def view_total(total_patients):
    print("Total patients:", total_patients)

def reset_patients(total_patients):
    total_patients = 0
    print(total_patients)
    return total_patients

total_patients = 0
print(total_patients)
total_patients = add_patient(total_patients)
view_total(total_patients)
total_patients = add_patient(total_patients)
total_patients = reset_patients(total_patients)