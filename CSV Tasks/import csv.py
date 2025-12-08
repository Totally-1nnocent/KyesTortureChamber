import csv

FILENAME = "scores.csv"

def add_score(username, score):
    with open(FILENAME, "a", newline="") as file:
        writer=csv.writer(file)
        writer.writerow([username, score])

def show_scores():
    with open(FILENAME, "r", newline="") as file:
        reader = csv.reader(file)
        for line in reader:
            print(f"{line[0]} scored {line[1]}")

def leaderboarding():
    leaderboard = {}
    with open(FILENAME, "r+", newline="") as file:
        reader = csv.reader(file)
        for line in reader:
            leaderboard.update(int(line[1]) : str(line[0]))


def main():
    while True:
        print("\n1. Add score")
        print("2. Show all scores")
        print("3. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            score = input("Enter score: ")
            while True:
                try:
                    int(score)
                except:
                    print("Please enter a number. ")
                    score = input("Enter score: ")
                else:
                    score = int(score)
                    if score > 100 or score < 0:
                        print("The score must be between 0 and 100.")
                        score = input("Enter score: ")
                    else:
                        break
            add_score(username, score)
        elif choice == "2":
            show_scores()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()