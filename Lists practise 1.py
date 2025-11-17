def lists_for_music():
    your_songs = []
    print("Enter your top 5 favourite songs.")
    for i in range(0,5):
        invertedCounter = 5 - i
        match invertedCounter:
            case 3:
                topSongCounter = "3rd"
            case 2:
                topSongCounter = "2nd"
            case 1:
                topSongCounter = "1st"
            case 4:
                topSongCounter = "4th"
            case 5:
                topSongCounter = "5th"
        song = input(f"Enter your {topSongCounter} favourite song: ")
        artist = input("Enter the artist: ")
        addedSong = song + " - " + artist
        your_songs.append(addedSong)
    return your_songs

def remove_songs(your_songs):
    removedSong = input("\nEnter the song you would like to remove in the format: song - artist\n")
    your_songs.remove(removedSong)

def add_songs(your_songs):
    adding = True
    while adding:
        addedSong = ("\nEnter the song you would like to add in the format: song - artist ")
        your_songs.append(addedSong)
        coninuation = input("\nWould you like to continue adding songs? (y/n) ")
        if coninuation.upper() == "N":
            adding = False

def view_songs(your_songs):
    print(f"\nThere are {len(your_songs)} in your playlist.\n")
    your_songs.sort()
    for i in range(1, (len(your_songs)+ 1)):
        print(f"{i}. {your_songs[i]}")

def menu(your_songs):
    print("\n1. Remove songs from your playlist. \n2. Add songs to your playlist. \n3. View your playlist. \n4. Exit")
    navigationChoice = input(">> ")
    match navigationChoice:
        case "1":
            remove_songs(your_songs)
        case "2":
            add_songs(your_songs)
        case "3":
            view_songs(your_songs)
        case "4":
            exit()
    menu(your_songs)

#your_songs = lists_for_music()
#menu(your_songs)

##cinema time!!!###

def add_movie(movies): #appending movie to list
    addedMovie = input("\nEnter the title of the movie you would like to add: ")
    movies.append(addedMovie)
    print(f"{addedMovie} had been added.")

def remove_movie(movies): #remove movie from list
    removedMovie = input("\nEnter the title of the movi you would like to remove: ")
    movies.remove(remove_movie)
    print(f"{removedMovie} has been removed.")

def view_movie(movies): #viewing all movies
    movies.sort()
    for i in range (0, len(movies)):
        print(movies[i])

def find_movie(movies): #serching for mmovie in list
    searchedMovie = input("\nEnter the title of the movie you would like to search for: ")
    found = False
    for i in range(0, len(movies)):
        if movies[i] == searchedMovie:
            print(f"Movie found. {searchedMovie} is showing.")
            found = True
    if found == False:
        print(f"Sorry. {searchedMovie} is not currently showing.")

def menu(movies): #navigating between subprograms
    print("\n1. Add movies to showing list. \n2. Remove movies from showing list. \n3. View showing list.\n4. Search for movies in shwing list.\n5. Exit.")
    choice = input(">> ")
    match choice:
        case "1":
            add_movie(movies)
        case "2":
            remove_movie(movies)
        case "3":
            view_movie(movies)
        case "4":
            find_movie(movies)
        case "5":
            exit()
    menu(movies)

movies = ["Friday the 13th", "Corpse Bride", "It Follows", "The Purge", "The Shining", "The Conjuring", "Skinamarink", "Scream", "Halloween", "Nightmare on Elm Street"]

##Tracking Populr Games##

games = [["Game", "Played", "Favourited", "Currently Playing"], ["Elden Ring", True, False, False], ["Baldurs Gate 3", False, False, False], ["Devil May Cry", False, False, False], ["Devil May Cry 2", False, False, False], ["Devil May Cry 3", False, False, False], ["Devil May Cry 5", False, False, False], ["Diablo V", False, False, False], ["Diablo IV", False, False, False]]

def display_games(games):
    print("")
    statusPlayed = ""
    statusFavourite = " "
    statusCurrent = ""
    for i in range(1, len(games)):
        if games[i][1]:
            statusPlayed = "Played"
        if games[i][2]:
            statusFavourite = " Favourited"
        if games [i][3]:
            statusCurrent = " Currently Playing"
        print(f"{i}. {games[i][0]}   {statusPlayed}{statusFavourite}{statusCurrent}")
        statusPlayed = ""
        statusFavourite = " "
        statusCurrent = ""

def game_status_update(games):
    statusPlayed = ""
    statusFavourite = " "
    statusCurrent = ""
    for i in range(1, len(games)):
        if games[i][1]:
            statusPlayed = "Played"
        if games[i][2]:
            statusFavourite = " Favourited"
        if games [i][3]:
            statusCurrent = " Currently Playing"
        print(f"{i}. {games[i][0]} {statusPlayed}{statusFavourite}{statusCurrent}")
        statusPlayed = ""
        statusFavourite = " "
        statusCurrent = ""
    chosenGame = input("Which game would you like to update the status of? ")
    for i in range(0, len(games)):
        if chosenGame == games[i][0]:
            updatedGame = i
    changedStatus = input("Would you like to mark a game as favourited or as played or as currently playing? (f/p/c) ")
    if changedStatus.upper() == "F":
        games[updatedGame][2] = True
        print(f"{chosenGame} has been favourited.")
    elif changedStatus.upper() == "P":
        games[updatedGame][1] = True
        print(f"{chosenGame} has been updated to played.")
    elif changedStatus.upper() == "C":
        for i in range(1, len(games)):
            games[i][3] = False
        games[updatedGame][3] = True
        print(f"{chosenGame} has been updated to urrently playing.")
    else:
        print("That is an invalid input. Try Again")
        game_status_update(games)

def menu(games):
    print("\n1 - View games\n2 - Update game status\n3 - Exit")
    navigation = input(">>> ")
    match navigation:
        case "1":
            display_games(games)
        case "2":
            game_status_update(games)
        case "3":
            exit()
    menu(games)

menu(games)