def health_comparison_game(score):
    monday = []
    wednesday = []
    friday = []
    mondaySteps = int(input("How many steps did you do on Monday? "))
    monday.append(mondaySteps)
    mondaySugar = float(input("Enter your blood glucose levels on Monday in mmol/L: "))
    monday.append(mondaySteps)
    
    wednesdaySteps = int(input("\nHow many steps did you do on Wednesday? "))
    wednesday.append(wednesdaySteps)
    wednesdaySugar = float(input("Enter your bllod glucose levels on Wednesday in mmol/L: "))
    wednesday.append(wednesdaySugar)

    fridaySteps = int(input("\nHow many steps did you do on Friday? "))
    friday.append(fridaySteps)
    fridaySugar = float(input("Enter your bllod glucose levels on Friday in mmol/L: "))
    friday.append(fridaySugar)
    
    averageSteps = (monday[0] + wednesday[0] + friday[0]) / 3
    print(f"You average steps per day is {averageSteps:.2f}.")
    if averageSteps > 1500:
        print("Your average steps per day is more than 1,500. Well done!")
        score = score + 1
    elif averageSteps > 2500:
        print("Your average steps per day is more than 2,500. Well done!")
        score = score + 2

    if friday[0] > monday[0]:
        print("Well done!\n You did more steps than on Monday!")
        score = score + 1
        difference = friday[0] - monday[0]
        if difference > 1000:
            print("Wow! Big improvement!")
            score = score + 1
    else:
        print("You didn't quite improve.\nTry again next week.")
    
    if friday[1] < 11:
        if friday[1] > monday[1]:
            print("Your blood glucose levels are improving!")
            score = score + 2
    elif monday[1] > 11:
        if friday[1] < monday[1]:
            print("Your blood glucose levels are improving!")
            score = score + 2
    elif monday[1] == friday[1]:
        print("Your blood glucose levels have not changed.")
        score = score + 1
    elif friday > 11:
        print("Your blood glucose levels have increased too much!")
    else:
        print("Your blood glucose levels have decresed too much!")

    averageSugar = (monday[1] + wednesday[1] + friday[1]) / 3
    if averageSugar < 11 and averageSugar > 6:
        print(f"Your average blood glucose level is {averageSugar:.2f} mmol/L. This is healthy!")
        score = score + 1

    print(f"Your score is {score}! Well Done!")

health_comparison_game(0)

## Reflection and self assessment ##
# == is used to compare if two values are the same whereas = is used to asign a value to a variable.
# One example of when you would use >= is to check if a score is high enough to pass a test (inclusive).
# Arithmetic operators often create the values used in relational operators (e.g. ave = (2+2)/2   if ave > 1:...)
# Or relational operators dictate if or which arithmetic operators are used.