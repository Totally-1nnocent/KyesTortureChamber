#num1 = int(input("Enter a number: "))
#num2 = int(input("Enter another number: "))
#ans = (float(num1/num2))
#ans2 = int(ans)
#print(str(num1) + " " + str(num2))
#print(str(ans) + " " + str(ans2))

#opinion = input("Do you like my code? (y/n)")
#if opinion == "y" or opinion =="Y":
   # boo = True
#else:
 #   boo = False

#print(boo)

#strings = ["Look", "At", "Me", "I", "Can", "Code!"]
#for word in strings:
    #print(word)

#dictionaries = {"Word": 2, "Meaning" : 3, "Use" : 4}
#for dictionary in dictionaries:
    #print(dictionary, dictionaries[dictionary])

#for use in dictionaries.keys():
    #print(use)

#for meaning in dictionaries.values():
    #print(meaning)

def lessThan(cutoffValue, *values) :
    array = []
    for value in values :
        if value < cutoffValue:
            array.append(value)
    return array

print(lessThan(11, 13, 7, 8, 122))