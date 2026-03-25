#### Parcel Logging System ####

#### Parcel Code Input ####
def parcel_code():
    code = input("Enter the parcel code: ")
    if not length_check(code):
        print("The parcel code must be 7 digits long.")
        parcel_code()
    else:
        if number_check(code):
            print("The parcel must only contain numbers.")
        else:
            checksum(code)


#### Checks length ####
def length_check(code):
    if len(code) == 7:
        return True
    else:
        return False
    
#### Checks numbers ####
def number_check(code):
    return isinstance(code, int)

#### Checksum ####
def checksum(code):
    numbers = [int(digits) for digits in str(code)]
    first_numbers = numbers[0:6]
    last_number = numbers[6]
    new_number = 0
    for i in range(len(first_numbers)):
        new_number = new_number + (first_numbers[i] * (i + 1))
    if (new_number % 10) == last_number:
        print("The checksum is correct. The code is valid.")
    else:
        print("The checksum is incorrect. The code is invalid.")
    
#### Main Program ####
parcel_code()