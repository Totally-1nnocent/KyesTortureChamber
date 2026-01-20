import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv("retail_sales_1M_dataset.csv")

def task_1(sales):
    print(sales.head())
    print(sales.info())

def task_2(sales):
    sales['total_sale'] = sales['quantity'] * sales['price']
    total_revenue = sum(sales['total_sale'])
    print(total_revenue)
    for item in pd.unique(sales['product']):
        new_sales_dp = sales[sales['product'] == item]
        product_revenue = round(new_sales_dp['price'].sum(), 2)
        print(f"{item}: £{product_revenue}")
    for type in pd.unique(sales['category']):
        new_cat_dp = sales[sales['category'] == type]
        product_revenue = round(new_cat_dp['price'].sum(), 2)
        print(f"{type}: £{product_revenue}")
    #sorted_sales = (new_sales_dp.sort_values(by = ['total_sale'], ascending = False))
    #print(sorted_sales[0:5])
        

task_2(sales)