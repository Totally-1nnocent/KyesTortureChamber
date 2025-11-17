name = input("Enter your name: ")
phone = input("Enter your mobile phone network: ")
phoneTime = input("How many minutes have you spent on your phone this month? ")
timeCost = float(phoneTime * 0.1)
textNum = input("How many texts have you sent this month? ")
textCost = float(textNum * 0.05)
bill = textCost + timeCost
tax = bill * 0.2
totalBill = bill + tax
print("Your total phone bill is " + str(bill) + " or " + str(totalBill) + " including VAT.")