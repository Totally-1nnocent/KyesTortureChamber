# Clinic vaccine stock (single brand for simplicity)

def dispense(stock, doses):
    stock = stock - doses
    print("Dispensed:", doses, "Remaining:", stock)
    return stock

def restock(stock, amount):
    print("Before restock:", stock)
    stock = stock + amount
    print("After restock:", stock)
    return stock

stock = 50
dispense(stock, 5)
restock(stock, 10)
print("End of day stock:", stock)
