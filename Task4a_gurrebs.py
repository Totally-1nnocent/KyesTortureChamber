import pandas as pd
import matplotlib.pyplot as plt
import datetime

#Displays the main menu and collects choice of menu item

def menu():

    flag = True

    while flag:
        print("###############################################")
        print("Welcome! Please choose an option from the list")
        print("1. Show total sales for a specific item") 
        print("2. Compare sales between services")
        print("3. Show sales for items and different services")
        print("4.")

        main_menu_choice = input("Please enter the number of your choice (1-4): ")

        try:
            int(main_menu_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(main_menu_choice) < 1 or int(main_menu_choice) > 4:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                return int(main_menu_choice)    

#Menu item selection form user and validates it
def get_product_choice():

    flag = True

    while flag:
        print("######################################################")
        print("Please choose a menu item form the list:")
        print("Please enter the number of the item (1-8)")
        print("1.  Nachos")
        print("2.  Soup")
        print("3.  Burger")
        print("4.  Brisket")
        print("5.  Ribs")
        print("6.  Corn")
        print("7.  Fries")
        print("8.  Salad")
        print("######################################################")

        menu_list = ["Nachos","Soup","Burger", "Brisket","Ribs","Corn", "Fries", "Salad"]

        item_choice = input("Please enter the number of your choice (1-8): ")

        try:
            int(item_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(item_choice) < 1 or int(item_choice) > 8:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                item_name = menu_list[int(item_choice)-1]
                return item_name

#Gets user input of start of date range
#Converts to a date to check data entry is in correct format and then returns it as a string
def get_start_date():
    
    flag = True
    
    while flag:
        start_date = input('Please enter start date for your time range (DD/MM/YYYY) : ')

        try:
           pd.to_datetime(start_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False

    return start_date

#Gets user input of end of date range
#Converts to a date to check data entry is in correct format and then returns it as a string
def get_end_date():
    
    flag = True
    
    while flag:
        end_date = input('Please enter end date for your time range (DD/MM/YYYY) : ')

        try:
           pd.to_datetime(end_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False

    return end_date


#imports data set and extracts data and returns data for a specific menu item within a user defined range
def get_selected_item(item, startdate, enddate):
    df1 = pd.read_csv("Task4a_data.csv") 
    df2 = df1.loc[df1['Menu Item'] == item]
    df3 = df2.loc[:,startdate:enddate]

    return df3

#creates a chart comparing lunch and dinner item sales between chosen dates
def compare_lunch_and_dinner(start_date, end_date):
    df = pd.read_csv("Task4a_data.csv")
    dinner_df = df.loc[df['Service'] == 'Dinner']
    lunch_df = df.loc[df['Service'] == 'Lunch']
    dinner = dinner_df.loc[:,start_date:end_date]
    lunch = lunch_df.loc[:,start_date:end_date]
    dates = dinner.columns

    plt.plot(dates, lunch.sum(), label = 'Lunch', color = 'r')
    plt.plot(dates, dinner.sum(), label = 'Dinner', color = 'b')
    plt.legend()
    plt.xlabel('Dates')
    plt.ylabel('Sales')
    plt.title('Sales per Service')
    plt.show()

#creates a chart for rhe sales of an item with two plots for different services
def lunch_and_dinner(item, start_date, end_date):
    df = pd.read_csv("Task4a_data.csv")
    temp_df = df.loc[df['Menu Item'] == item]
    dinner_item = temp_df.loc[temp_df['Service'] == 'Dinner']
    lunch_item = temp_df.loc[temp_df['Service'] == 'Lunch']
    dinner = dinner_item.loc[:,start_date:end_date]
    lunch = lunch_item.loc[:,start_date:end_date]
    dates = dinner.columns
    print(dates)

    plt.plot(dates, lunch.sum(), label = 'Lunch', color = 'g')
    plt.plot(dates, dinner.sum(), label = 'Dinner', color = "#8316ba")
    plt.legend()
    plt.xlabel('Dates')
    plt.ylabel('Sales')
    plt.title(f'Sales per Service for {item}')
    plt.show()

def avg_and_total_sales(start_date, end_date):
    df = pd.read_csv('Task4a_data.csv')
    items = df["Menu Item"].unique()
    item_sales = []
    total_sales = []
    for item in items:
        temp_df = df[df['Menu Item'] == item]
        sales_per_day = temp_df.loc[:, start_date:end_date].sum()
        total_sales = total_sales + [sales_per_day.sum()]
    minus = min(total_sales) * 0.75
    for i in range(len(total_sales)):
        item_sales = item_sales + [total_sales[i] - minus]
    
    plt.bar(items, item_sales, bottom = minus, color = "#ff00b7")
    plt.xlabel('Menu Items')
    plt.ylabel('Sales')
    plt.title('Sales per Item')
    plt.show()

    averages = []
    for x in range(item_sales):
        avg = item_sales[x] /
        averages = averages + avg

main_menu = menu()
if main_menu == 1:

    item = get_product_choice()
    start_date = get_start_date()
    end_date = get_end_date()
 
    extracted_data = get_selected_item(item, start_date, end_date)
    
    print("Here is the sales data for {} between dates {} and {}:".format(item, start_date, end_date))
    extract_no_index = extracted_data.to_string(index=False)

    print(extract_no_index)
elif main_menu == 2:
    start_date = get_start_date()
    end_date = get_end_date()
    compare_lunch_and_dinner(start_date, end_date)
elif main_menu == 3:
    item = get_product_choice()
    start_date = get_start_date()
    end_date = get_end_date()
    lunch_and_dinner(item, start_date, end_date)
elif main_menu == 4:
    start_date = get_start_date()
    end_date = get_end_date()
    avg_and_total_sales(start_date, end_date)
else:
    print('This part of the program is still under development')
