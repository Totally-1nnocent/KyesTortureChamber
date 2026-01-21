import pandas as pd
import csv
import matplotlib.pyplot as plt

issues = pd.read_csv("Task4a_data.csv") 

# Outputs the initial menu and validates the input
def main_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############# Botes Parcels CRM System #############")
        print("####################################################")
        print("")
        print("########### Please select an option ################")
        print("### 1. Total issues by type")
        print("### 2. ")

        choice = input('Enter your number selection here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:    
            print('Choice accepted!')
            flag = False

    return choice

  # Submenu for totals, provides type check validation for the input and returns issue type as a string
def total_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############## Total issues by type ################")
        print("####################################################")
        print("")
        print("########## Please select an issue type ##########")
        print("### 1. Customer Account Issue")   
        print("### 2. Delivery Issue") 
        print("### 3. Collection Issue")  
        print("### 4. Service Complaint")

        choice = input('Enter your number selection here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:    
            print('Choice accepted!')
            choice = int(choice)
            flag = False

    issueTypeList = ["Customer Account Issue", "Delivery Issue", "Collection Issue", "Service Complaint"]
    

    issueType = issueTypeList[choice-1]
  
    return issueType     

# Creates a new dataframe then counts the number of occurences of the requested issue type

def get_total_data(total_menu_choice, issues):
    
    total = issues['Issue Type'].value_counts()[total_menu_choice]

    msg = "The total number of issues logged as a {} was: {}".format(total_menu_choice, total)
    return msg

def time_for_issue_types(issues): ##Calculates average time to resolve different issue types and outupts in a graph
    
    ####Calculates average days to resolve for each type of issue and saves it to a list

    time_taken = []
    for issue in pd.unique(issues['Issue Type']):
        temp_df = issues[issues['Issue Type'] == issue]
        time_taken = time_taken + [sum(temp_df['Days To Resolve']) / len(temp_df['Days To Resolve'])]

    ####Creates bar chart showing average days for resolution for the different types of issues###
    plt.style.use('ggplot')
    plt.ylabel('Average Days To Resolve')
    plt.bar(pd.unique(issues['Issue Type']), time_taken)
    plt.show()

def issues_based_on_region(issues):#### Choose region and shows percentage of issues and resolutions for that region

    regions = pd.unique(issues['Region'])

    print("########## Please choose a region to view ##########") 
    for i in range(len(regions)):
        print(f'### {i + 1}. {regions[i]}')

    choice = input("Enter your number selection here: ")

    try:
            int(choice)
    except:
        print("Sorry, you did not enter a valid option")
        flag = True
    else:    
        print('Choice accepted!')
        choice = int(choice)
        flag = False
    
    resolutions = []

    region_choice = regions[choice - 1]
    for item in issues['Region']:
        temp_df = issues[issues['Region'] == region_choice]
        #for item in pd.unique(temp_df['How Resolved']):
            #temp_df = temp_df[temp_df['How Resolved'] == item]
            #resolutions = resolutions + [temp_df.value_counts()]



    #fig, (region_issues, region_resolutions) = plt.subplots(1, 2)
    #region_resolutions.pie()
    #region_issues.pie()

main_menu_choice = main_menu()
if main_menu_choice ==  "1":
    total_menu_choice = total_menu()
    print(get_total_data(total_menu_choice, issues))

issues_based_on_region(issues)