import string
alphabet = list(string.ascii_lowercase)

def encrypt(alphabet):
    message = input("Enter your message: ")
    key = input("Enter the number you would like to shift your message by: ")
    while True:
        try:
            int(key)
        except:
            print("Please enter a whole number.")
            key = input("Enter the number you would like to shift your message by: ")
        else:
            key = int(key)
            break
    newMessage = ""
    for character in message:
        if (character != " ") and (alphabet.index(character.lower()) + key < 26):
            if character.isupper():
                newCharacter = alphabet[alphabet.index(character.lower()) + key]
                newMessage = newMessage + newCharacter.upper()
            else:
                newCharacter = alphabet[alphabet.index(character) + key]
                newMessage = newMessage + newCharacter
        elif character == " ":
            newMessage = newMessage + " "
        else:
            newCharacter = alphabet[alphabet.index(character)]
            newMessage = newMessage + newCharacter
    print(f"Your encrypted message is:\n{newMessage}")

def decrypt(alphabet):
    message = input("Enter your message: ")
    key = input("Enter the number you would like to shift your message by: ")
    while True:
        try:
            int(key)
        except:
            print("Please enter a whole number.")
            key = input("Enter the number you would like to shift your message by: ")
        else:
            key = int(key)
            break
    newMessage = ""
    for character in message:
        if (character != " ") and (alphabet.index(character.lower()) - key > 0):
            if character.isupper():
                newCharacter = alphabet[alphabet.index(character.lower()) - key]
                newMessage = newMessage + newCharacter.upper()
            else:
                newCharacter = alphabet[alphabet.index(character) - key]
                newMessage = newMessage + newCharacter
        elif character == " ":
            newMessage = newMessage + " "
        else:
            newCharacter = alphabet[(alphabet.index(character) + key) % 26]
            newMessage = newMessage + newCharacter
    print(f"Your unencrypted message is:\n{newMessage}")

def menu():
    while True:
        print("Would you like to encrypt, decrypt a message or leave the program? (E/D/L) ")
        choice = input(">>>")
        if choice.upper() == "E":
            encrypt(alphabet)
        elif choice.upper() == "D":
            decrypt(alphabet)
        else:
            exit()

menu()