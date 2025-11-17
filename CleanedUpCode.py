def hospital():
    name = input("Enter patient name: ") #variable name should be spelt correctly and only constant names should be capitalised and input prompt should have correct grammar
    age = int(input("Enter patient age: ")) #input prompt should have correct grammar and variable name should not begin with a capital letter and casting this to an integer allows it to be used in the if comparison later in the code
    height = float(input("Enter patient height in m: ")) #input prompt should be clear to understand and have correct grammar and casting this to a float reduces the need to do so later in calculations
    weight = float(input("Enter patient weight in kg: ")) #input prompt should be clear to understand and have correct grammar and casting this to a float reduces the need to do so later in the code
    bmi = weight / (height ** 2) #since I cast the weight and height variables to float earlier in the code it can be removed here
    if bmi > 30: #the content of the if statement should be indented on a seperate line
        print("The patient is overweight.")
    else:
        print("The patient is has a healthy bmi.")
    if age > 65:
        print("Senior citizen discount applied")
    print(f"Patient: {name} has a bmi of {bmi:.2f}")

hospital()