def arithmetic_basics():
    GOAL = 10000
    steps = int(input("Enter the number of steps you have done so far: "))
    percentOfGoal = (steps / GOAL) * 100
    if steps < GOAL:
        remainingSteps = GOAL - steps
        print(f"You have done {steps} steps. This is {percentOfGoal:.2f}% of your goal.\nYou have {remainingSteps} steps to go.")
    elif steps == GOAL:
        print("Well done! You have reachhed your goal.")
    else:
        remainingSteps = steps - GOAL
        print(f"Well Done! You have exceeded your goal by {remainingSteps} steps.")

def bmi_buckets():
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in m: "))
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        print("You are underweight.")
    elif bmi < 25:
        print("You are a healthy weight.")
    elif bmi < 30:
        print("You are overweight.")
    else:
        print("You are obese.")

def flag_user(daily_screen_minutes, night_screen_minutes, steps):
    if (daily_screen_minutes > 240 and steps < 5000) or night_screen_minutes > 60:
        return True
    
def hydration():
    water = int(input("Enter how much water you have drank today in ml: "))
    score = water // 250
    score = score + ((water // 2000) * 5)
    print(f"You have earned {score} points today.")
    return score

def eligible_for_free_class(age, low_income, days_since_last_free):
    if ((age >= 16 and age <= 25) or low_income) and days_since_last_free > 30:
        return True
    
def weekly_tier(steps, water_ml):
    points = (steps // 1000) * 2 + (water_ml // 500)
    if points <= 19:
        return "Bronze"
    elif points <= 39:
        return "Silver"
    else:
        return "Gold"
    
def safe_average_minutes(total_minutes, sessions):
    if sessions == 0:
        return 0
    else:
        avg = total_minutes / sessions
        return round(avg, 1)
    
def summary_line(steps, water_ml, screen_mins):
    GOAL = 10000
    percentSteps = int(steps) / GOAL
    points = hydration()
    if screen_mins <= 240:
        screenLabel = "OK"
    else:
        screenLabel = "High"
        print(f"Steps: {steps} ({percentSteps:.2f}), Water: {water_ml}ml (+{points} pts), Screen: {screen_mins} mins - {screenLabel}.")