arcadeMachines = {
    "Pacman": {"Category":"Maze Chase", "Machine Status":"Working Order"}, 
    "Space Invaders": {"Category":"Shooter", "Machine Status": "Needs Repair"}, 
    "Tron":{"Category": "Action Minigames", "Machine Status":"Out of Order"}, 
    "Centipede":{"Category":"Shooter", "Machine Status":"Working Order"}
    }

def view_machines(arcadeMachines):
    print("")
    for key in arcadeMachines.keys():
        print(f"- {key}")

def add_machines(arcadeMachines):
    newMachine = input("Enter the name of the machine you would like to add: ")
    newCategory = input("Enter the category of the new machine: ")
    newStatus = input("Enter the working status of the new machine: ")
    arcadeMachines.update({newMachine:{"Category":newCategory, "Machine Status": newStatus}})

def update_status(arcadeMachines):
    view_machines(arcadeMachines)
    print("")
    updatedGame = input("Enter the game you would like to update the status of: ")
    newStatus = input("Enter the new status of this machine: ")
    arcadeMachines[updatedGame]["Machine Status"] = newStatus

def delete_machines(arcadeMachines):
    removedGame = input("Enter the name of the machine you would like to delete: ")
    del arcadeMachines[removedGame]

def count_status(arcadeMachines):
    counter = 0
    print("")
    searchedStatus = input("Enter the status you would like to search for: ")
    for key in arcadeMachines.keys():
        if arcadeMachines[key]["Machine Status"] == searchedStatus:
            counter = counter + 1
    print(f"Ther are {counter} machines that are {searchedStatus}.")

def menu(arcadeMachines):
    print("")
    print("1 - View Machines \n"
    "2 - Add Machines\n"
    "3 - Update Machine Status\n"
    "4 - Delete Machines\n"
    "5 - Count Machine Status \n"
    "6 - Exit\n"
    )
    navigatingChoice = input(">>>")
    match navigatingChoice:
        case "1":
            view_machines(arcadeMachines)
        case "2":
            add_machines(arcadeMachines)
        case "3":
            update_status(arcadeMachines)
        case "4":
            delete_machines(arcadeMachines)
        case "5":
            count_status(arcadeMachines)
        case "6":
            exit()



##### Cinema Ticketing System #####
cinema = {"The VelociPastor":{"Time":["19:32", "20:11", "17:00"], "Seats": 12},
          "Tron 1982":{"Time":["12:45", "14:00", "13:45"], "Seats":34},
          "Transformers: The Movie 1986":{"Time":["13:22", "15:42", "16:30"], "Seats":45},
          "Transformers One":{"Time":["14:55", "17:30", "18:00"], "Seats": 8},
          "Tron: Legacy":{"Time":["15:15", "16:22", "19:00"], "Seats": 42},
          "Tron: Ares" :{"Time":["16:52", "19:30", "20:00"], "Seats":30}
          }

def view_films_and_times(cinema):
    print("")
    for key in cinema.keys():
        print(f"{key} - {cinema[key]["Time"]}")
    
def add_new_film(cinema):
    print("")
    newTimes = []
    newFilm = input("Enter the name of the film you would like to add: ")
    numberOfTimes = int(input("How many times is this film shown in a day? "))
    for i in range(0, numberOfTimes):
        newTimes.append(input("Enter the time this film is showing: "))
    newSeats = input("Enter the number of seats available: ")
    cinema.update({newFilm:{"Time":newTimes, "Seats": newSeats}})

def book_tickets(cinema):
    print("")
    bookingFilm = input("Which film would you like to book? ")
    bookingSeats = int(input("Enter the number of seats you would like to book: "))
    if cinema[bookingFilm]["Seats"] - bookingSeats < 0:
        print(f"Sorry there are only {cinema[bookingFilm]["Seats"]} seats left.")
    else:
        cinema[bookingFilm]["Seats"] = (cinema[bookingFilm]["Seats"] - bookingSeats)