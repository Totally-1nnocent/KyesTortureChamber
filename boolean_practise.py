#x = 10
#y = 5
#print(x > y)
#print(x == y)

#def num_check(num1):
    #if type(num1) != int:
        #print("Please enter a whole number.")
        #menu()
    #if int(num1) >= 1 and int(num1) <= 100:
        #print(num1, "is between 1 and 100.")

#def menu():
    #num1 = input("Enter a number: ")
    #num_check(num1)
    #return num1

#def record():
    #name = input("Enter your name: ")
    #age  = int(input("Enter your age: "))
    #testScore = int(input("Enter your test score out of 100: "))
    #summarise(name, age, testScore)

#def test_pass(testScore):
    #if testScore > 50:
        #passed = True
        #return passed

#def age_check(age):
    #if age >= 18:
        #adult = True
        #return adult
    
#def summarise(name, age, testScore):
    #adultCheck = age_check(age)
    #if adultCheck == True:
        #adult = "adult"
    #else:
        #adult = "child"
    #passed = test_pass(testScore)
    #if passed == True:
        #status = "passed"
    #else:
        #status = "failed"
    #summary = f"{name} is a(n) {adult}. You have {status} your test."
    #print(summary)


##Attendance Register##
total = 0 

students = ["Rachel", "Timothy", "David", "Saoirse", "Wendy", "William", "Meghan", "Cristopher", "Joeseph", "Regan"]
for student in range(len(students)):
    att = input(f"Is {students[student]} in today? (y/n) ")
    here = att.upper() == "Y"
    if here:
        total = total + 1

totalAttendance = (total / len(students)) * 100
print(f"The total attendance today is {totalAttendance:.2f}%")

##Temp converter##

def celcius_to_farenheit():
    celcius = input("What is the temperature in celcius? ")
    farenheit = (float(celcius) * (9/5)) + 32
    print(f"It is {farenheit:.2f} F")

def farenheit_to_celcius():
    farenheit = input("What is the temperature in farenheit? ")
    celcius = (float(farenheit) - 32) * 5/9
    print(f"It is {celcius:.2f} C")

celOrFar = input("Do you have the temperature in celcius or farenheit: (c/f) ")
if celOrFar.upper() == "C":
    celcius_to_farenheit()
else:
    farenheit_to_celcius()
