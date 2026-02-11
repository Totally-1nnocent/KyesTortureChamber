import datetime
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Task4a_Data_2022.csv')


def mainmenu():
    print("\t\t****Welcome to the Dashboard****")
    print('1) Return all current data')
    print('2) Return data for a specific region')
    print('3) Return highest overall increase in property value')
    print('4) Return property types and sizes within a region')
    return int(input(""))


def region_check(region, startdate, enddate):  # region, startdate, enddate

    df1 = df.loc[:, startdate:enddate]
    df2 = df.loc[:, 'Region Code':'Rooms']

    result = pd.concat([df2, df1], axis=1, join='inner').where(df2["Region"] == region)
    result = pd.DataFrame(result)
    result.dropna(inplace=True)
    print(result)
    ave = df1.mean()
    ave.plot()
    plt.show()
    return result

def highest_property_values():
    while True: ##get startdate and enddate
        startdate = input("Please enter a start date as month-year e.g. JAN-20\n")
        startdate = startdate.capitalize()
        if startdate not in df.columns:
            print("Error start date not found")
        else:
            while True:
                enddate = input("Please enter an end date as month-year e.g. JAN-20\n")
                enddate = enddate.capitalize()
                if enddate not in df.columns:
                    print("Error end date not found")
                else:
                    break

        result = pd.concat([df], axis=1, join='inner') ##finding overall property value increase
        starttotal = result.groupby('Region')[startdate].sum()
        endtotal = result.groupby('Region')[enddate].sum()
        overallincrease = (endtotal - starttotal) * 100

        plt.style.use('bmh')
        plt.bar(df['Region'].unique(), overallincrease)
        plt.ylabel("Percentage Value Increase of All Propeties")
        plt.xlabel("Region")
        plt.title("Percentage Propety Value Increase by Region")
        plt.show()

def types_and_sizes():
     print("")

def navigation_check():
    x = mainmenu()
    while x in (1, 2, 3, 4):
        if x == 1:
            print(df)
        elif x == 3:
            highest_property_values()
        elif x == 4:
            types_and_sizes()
        elif x == 2:
            while True:
                print()

                region = input("Please enter the name of the region you would like to check:")
                region = region.capitalize()
                if region in df.Region.values:
                    while True:
                        startdate = input("Please enter a start date as month-year e.g. JAN-20\n")
                        startdate = startdate.capitalize()
                        if startdate not in df.columns:
                            print("Error start date not found")
                        else:
                            while True:
                                enddate = input("Please enter an end date as month-year e.g. JAN-20\n")
                                enddate = enddate.capitalize()
                                if enddate not in df.columns:
                                    print("Error end date not found")
                                else:
                                    region_check(region, startdate, enddate)
                                    break
                            break
                    break
                else:
                    print("Region not found")
        x = mainmenu()


navigation_check()