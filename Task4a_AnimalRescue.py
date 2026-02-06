import pandas as pd
import matplotlib.pyplot as plt

def main_menu():
    flag = True

    while flag:

        print("#################################################")
        print("############## Snowy Animal Rescue ##############")
        print("#################################################")
        print("")
        print("########### Please select an option #############")
        print("### 1. Average Social Media Interaction Data")
        print("### 2. Trends as graphs")

        choice = input('Enter your number selction here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:    
            print('Choice accepted!')
            flag = False

    return choice


def average_menu ():
    flag = True

    while flag:

        print("#################################################")
        print("############## Average Interaction ##############")
        print("#################################################")
        print("")
        print("########### Please select an option #############")
        print("### 1. Average number of Likes")   
        print("### 2. Average number of Shares") 
        print("### 3. Average number of Comments")  

        choice = input('Enter your number selction here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:    
            print('Choice accepted!')
            flag = False

    return choice      

def convert_avg_men_coice(avg_men_choice):
    
    if avg_men_choice == "1":
        avg_choice = "Likes"
    elif avg_men_choice == "2":
        avg_choice = "Shares"
    else:
        avg_choice = "Comments"  
    
    return avg_choice


def get_avg_data(avg_choice):
    
    df = pd.read_csv("Task4a_data.csv")
    extract = df.groupby(['Date'], as_index=False) [avg_choice].mean()
    extract_no_index = extract.to_string(index=False)
    
    print("Here is the average number of {} each day during the campaign:".format(avg_choice))
    return extract_no_index

def trend_identification():
    df = pd.read_csv("Task4a_data.csv")
    #print(df.head(5))
    #print(df.columns)
    #print(df.info())

    days = df['Date'].unique()
    averages = {}
    for day in days:
        tempdf = df[df["Date"] == day]
        average_likes = tempdf['Likes'].mean()
        average_shares = tempdf['Shares'].mean()
        average_comments = tempdf['Comments'].mean()
        averages[day] = [average_likes, average_shares, average_comments]

    types = df['Post Type'].unique()
    interactions = {}
    for type_of_post in types:
        tempdf = df[df['Post Type'] == type_of_post]
        interactions[tempdf['Likes'].sum() + tempdf['Comments'].sum() + tempdf['Shares'].sum()] = type_of_post
    #print(sorted(interactions.items()))

    times = df['Time'].unique()
    timed_interactions = {}
    for time in times:
        tempdf = df[df['Time'] == time]
        timed_interactions[tempdf['Likes'].sum() + tempdf['Comments'].sum() + tempdf['Shares'].sum()] = time
    #print(sorted(timed_interactions.items()))

    plt.style.use("bmh")

    plotting = []
    for i in range(len(averages)):
        plotting = plotting + [averages[days[i]][0]]
    
    fig, (plot1, plot2, plot3) = plt.subplots(3)

    plot1.plot(plotting)
    plot1.set_title("Average Likes per Day")
    plot1.set_ylabel("Likes")
    plot1.set_xlabel("Days into the Campaign")
    plot2.bar(interactions.values(), interactions.keys())
    plot2.set_title("Total Interactions by Post Type")
    plot2.set_ylabel("Interactions")
    plot2.set_xlabel("Post Types")
    plot3.bar(timed_interactions.values(), timed_interactions.keys())
    plot3.set_title("Total Interactions by Time of Day")
    plot3.set_ylabel("Interactions")
    plot3.set_xlabel("Time of Day")

    plt.show()

main_menu_choice = main_menu()
if main_menu_choice == "1":
    avg_men_choice = average_menu()
    avg_choice = convert_avg_men_coice(avg_men_choice)
    print(get_avg_data(avg_choice))
elif main_menu_choice == "2":
    trend_identification()

#Poll are the type of posts that get the most interaction.
#The highest point of likes is towards the middle of the campaign, 8 days in and it is followed quickly by the lowest point.
#The most interactions occur between 2pm and 4pm.