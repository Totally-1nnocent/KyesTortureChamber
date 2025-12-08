def write_scores():
    with open("scores.txt","a") as scores:
        username = input("Enter your username: ")
        score = input("Enter your score: ")
        checking = True
        while checking:
            try:
                int(score)
            except:
                print("Please enter a number.")
                score = input("Enter your score: ")
            else:
                if int(score) > 100 or int(score) < 0:
                    print("That score is invalid.")
                    score = input("Enter your score: ")
                else:
                    checking = False
        scores.write(f"{username}: {score}\n")
    menu()

def read_scores():
    with open("scores.txt","r") as scores:
        print(scores.read())
    menu()

def menu():
    print("Would you like to 1. add a score 2. view all scores or 3. exit?")
    choice = input(">>>> ")
    if choice == "1":
        write_scores()
    elif choice == "2":
        read_scores()
    elif choice == "3":
        exit()
    else:
        print("That is an invalid input.")
        menu()

menu()