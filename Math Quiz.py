import random
import math
import numpy as np
basic_operand = np.array(["*","/","+", "-"])
complex_operand = np.array(["cos", "sin", "tan"])

def easy_question(operators, question_counter):
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    operator = operators[random.randint(0,3)]
    print(f"{question_counter}. {num1} {operator} {num2}")
    match operator:
        case "*":
            answer = num1 * num2
        case "/":
            answer = round(num1 / num2, 2)
        case "+":
            answer = num1 + num2
        case "-":
            answer = num1 - num2
    return answer

def medlow_question(operators, question_counter):
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    operator = operators[random.randint(0,3)]
    print(f"{question_counter}. {num1} {operator} {num2}")
    match operator:
        case "*":
            answer = num1 * num2
        case "/":
            answer = round(num1 / num2, 2)
        case "+":
            answer = num1 + num2
        case "-":
            answer = num1 - num2
    return answer

def medhigh_question(operators, question_counter):
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    num3 = random.randint(1,100)
    operator1 = operators[random.randint(0,3)]
    operator2 = operators[random.randint(0,3)]
    print(f"{question_counter}. {num1} {operator1} {num2} {operator2} {num3}")
    match operator1:
        case "*":
            if operator2 == "*":
                answer = num1 * num2 * num3
            elif operator2 == "/":
                answer = round(num1 * num2 / num3, 2)
            elif operator2 == "+":
                answer = num1 * num2 + num3
            else:
                answer = num1 * num2 - num3
        case "/":
            if operator2 == "*":
                answer = round(num1 / num2 * num3, 2)
            elif operator2 == "/":
                answer = round(num1 / num2 / num3, 2)
            elif operator2 == "+":
                answer = round(num1 / num2 + num3, 2)
            else:
                answer = round(num1 / num2 - num3, 2)
        case "+":
            if operator2 == "*":
                answer = num1 + num2 * num3
            elif operator2 == "/":
                answer = round(num1 + num2 / num3, 2)
            elif operator2 == "+":
                answer = num1 + num2 + num3
            else:
                answer = num1 + num2 - num3
        case "-":
            if operator2 == "*":
                answer = num1 - num2 * num3
            elif operator2 == "/":
                answer = round(num1 - num2 / num3, 2)
            elif operator2 == "+":
                answer = num1 - num2 + num3
            else:
                answer = num1 - num2 - num3
    return answer

def high_question(operands, question_num):
    num1 = random.randint(0,10)
    num2 = random.randint(0, 180)
    operator = operands[random.randint(0,2)]
    print(f"{question_num}. {num1}{operator}({num2})")
    match operator:
        case "cos":
            if num1 != 0:
                answer = num1 * math.cos(math.radians(num2))
            else:
                answer = math.cos(math.radians(num2))
        case "sin":
            if num1 != 0:
                answer = num1 * math.sin(math.radians(num2))
            else:
                answer = math.sin(math.radians(num2))
        case "tan":
            if num1 != 0:
                answer = round(num1 * math.tan(math.radians(num2)), 2)
            else:
                answer = round(math.tan(math.radians(num2)), 2)
    return answer

def check_ans(correct_ans):
    correct = False
    given_ans = input(">>> ")
    tries = 3
    while tries > 0:
        if not isinstance(given_ans, int) or not isinstance(given_ans, float):
            if float(given_ans) == correct_ans:
                print("Congratulations! You are correct.")
                correct = True
                break
            else:
                print(f"Incorrect You have {tries} more tries.")
                tries = tries - 1
                given_ans = input(">>> ")
        else:
            print("Please enter a number.")
            given_ans = input(">>> ")
    if not correct:
        print(f"You are incorrect. The answer was {correct_ans}.")
    return correct

def checkpoint(num_correct, num_questions):
    if num_questions == 1:
        return 0 
    elif num_questions == 5:
        if num_correct == 4:
            print(f"Your score so far is {num_correct}/{num_questions-1}")
            print("I think this is too easy for you. Lets fix that >:)")
            return 1
        else:
            print(f"Your score so far is {num_correct}/{num_questions-1}")
            print("I think somebody's struggling.")
            return 0
    elif num_questions == 8:
        if num_correct >= 6:
            print(f"Your score so far is {num_correct}/{num_questions-1}")
            print("Still too easy? I can fix that")
            return 2
        elif num_correct == 5:
            print(f"Your score so far is {num_correct}/{num_questions-1}")
            print("I think you're ready for somthing trickier")
            return 1
        else:
            print(f"Your score so far is {num_correct}/{num_questions-1}")
            print("Not as easy as it looks is it?")
            return 0
    elif num_questions == 11:
        if num_correct > 8:
            print(f"Your score so far is {num_correct}/{num_questions-1}")
            print("I can still make it harder")
            return 3
        else:
            print(f"Your score so far is {num_correct}/{num_questions-1}")
            print("Gotten knocked off your high horse? boohoo.")
            return 2
    else:
        return 0

def question_choice(difficulty, basic_operands, complex_operands, question_num):
    match difficulty:
        case 0:
            answer = easy_question(basic_operands, question_num)
        case 1:
            answer = medlow_question(basic_operands, question_num)
        case 2:
            answer = medhigh_question(basic_operands, question_num)
        case 3:
            answer = high_question(complex_operands, question_num)
        case _:
            answer = easy_question(basic_operands, question_num)
    return answer

def main(basic_operands, complex_operands):
    print(">>> Welcome to my Maths quiz! <<<")
    print("There are 12 questions. If the answer is a decimal please give it to 2dp.")
    correct = 0
    question_counter = 1
    difficulty = 0
    for i in range(0,12):
        if question_counter in(5, 8, 11):
            difficulty = checkpoint(correct, question_counter)
        print(difficulty)
        answer = question_choice(difficulty, basic_operand, complex_operands, question_counter)
        check_correct = check_ans(answer)
        if check_correct:
            correct += 1
        question_counter += 1
        print(difficulty)
    print("Thanks for playing my quiz!")
    print(f"Your total score was {correct}/12 ")
    print("Goodbye (enter anything to exit) ")
    if input(">>> "):
        quit()

main(basic_operand, complex_operand)