import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("amazon_sales_dataset.csv")

def task1(df):
    #print(df.head())
    print(df.shape)
    print(df.columns)

def task2(df):
    print(df['quantity_sold'].sum())
    print(df['price'].mean())

def task3(df):
    total_category_sales = df.groupby('product_category')['quantity_sold'].sum()
    print(total_category_sales)
    plt.style.use("bmh")
    plt.bar(df['product_category'].unique(), total_category_sales - 24000, bottom = 24000)
    plt.xlabel("Product Categories")
    plt.ylabel("Number of Items sold")
    plt.title("Quantity of Items sold by Category")
    plt.show()

def task4(df):
    sales_by_region = df.groupby('customer_region')['quantity_sold'].sum()
    plt.style.use('bmh')
    plt.bar(df['customer_region'].unique(), sales_by_region-37000, bottom=37000)
    plt.xlabel("Regions")
    plt.ylabel("Quantity of Items Sold")
    plt.title("Items Sold by Region")
    plt.show()

task4(df)