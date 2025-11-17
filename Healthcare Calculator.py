def vampire():
    weight = float(input("Enter the weight of the patient in kg: "))
    bloodVolume = float(input("Enter the volume of blood given in ml: "))
    totalBlood = weight / 0.08
    remainingBlood = totalBlood - bloodVolume
    minimumBlood = totalBlood / 0.15
    if remainingBlood < minimumBlood:
        print(f"The patient has lost too much blood, they need an immediate transfusion.")
    elif remainingBlood > minimumBlood:
        availableBlood = remainingBlood - minimumBlood
        print(f"The patient can give {availableBlood:.2f} ml more blood.")
    else:
        print("Stop taking blood from the patient.")

vampire()