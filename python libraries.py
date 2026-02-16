import math
import random
import datetime
import numpy as np

def task1():
    number = input("Enter a number: ")
    sqr_root = math.sqrt(number)
    sqred = math.pow(number, 2)
    round_up = math.ceil(number)
    round_down = math.floor(number)
    circ_area = math.pi * math.pow(number, 2)
    print(f"The square root of {number} is {sqr_root:.2f}/n{number} squared is {sqred:.2f}")
    print(f"{number} rounded up is {round_up:.2f} /n{number} rounded down is {round_down:.2f}")
    print(f"The area of a circle that has {number} as a diameter would be {circ_area:.2f}")

def task2():
    lives = 3
    wins = 0
    rounds = 0
    while lives > 0:
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        total_score = dice1 + dice2
        if total_score == 7 or total_score == 11:
            print("You Win!")
            wins += 1
            rounds += 1
        else:
            print("Try again.")
            lives = lives - 1
    rounds += 1
    percentage = (wins/rounds) * 100
    print(f"You have {percentage:.2f}% of rounds.")

def task3():
    current_date = datetime.datetime.now()
    birthday = input("Enter your birthday: (DD/MM/YYYY) ").split('/')
    birthdate = datetime.datetime(int(birthday[2]), int(birthday[1]), int(birthday[0]))
    age = current_date.year - birthdate.year - ((current_date.month, current_date.day) < (birthdate.month, birthdate.day))
    birthday_this_year = datetime.datetime(current_date.year, int(birthday[1]), int(birthday[0]))
    days_waiting = birthday_this_year - current_date
    print(f"Today the date and time is {current_date.strftime('%d/%m/%Y %H:%M')}")
    print(f"You are {age} years old and it is {days_waiting.days} days until your next birthday.")
    
def task4():
    sales = np.array[120,135,150,98,175,200,143]
    mean = np.mean(sales)
    total = np.sum(sales)
    highest = np.max(sales)
    lowest = np.min(sales)
    print(f"The mean value is {mean} and the total is {total}")
    print(f"The highest value is {highest} and the lowest is {lowest}")
    