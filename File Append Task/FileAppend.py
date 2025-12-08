import random

def file_appending():
    with open("fileappending", "a") as fileappending:
        for i in range(0,8):
            randomScore = random.randint(0,100)
            fileappending.write(f"Player {}: {randomScore}\n")

def file_reading():
    with open("fileappending", "r") as fileappending:
        for line in fileappending:
            print(line)

file_appending()
file_reading()