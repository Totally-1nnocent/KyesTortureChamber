#x = 25
#y = 3.14
#print(type(x), type(y))

#a = 10
#b = 3
#print(type(a/b))
#print(type(a//b))
#print(type(a*2.5))

#name = "Alex"
#greeting = "Hello "+name
#print(name.upper(), len(name))

#scores = {"David" : 83, "Amalia" : 67, "Rebecca" : 87}
#def mean(scores):
    #total = 0
    #for score in range(len(scores)):
       #total = total + 
    #average = total / len()
    #print("The average score is " + str(average))

#def menu(scores):
    #name = input("Enter your name: ")
    #result = int(input("Enter your score: "))
    #scores[name] = result


def name_length():
    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name: ")
    fullName = str(firstName) + str(lastName)
    length = len(fullName)
    if length > 20:
        print("ERROR - Enter your name again.")
        name_length()
    print("Your name is " + fullName)

name_length()