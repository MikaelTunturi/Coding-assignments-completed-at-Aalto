'''
Created on 16.10.2018

@author: mikaeltunturi
'''
def main():
    count = int(input("Enter the number of the days.\n"))
    orders = [0.0] * count
    for i in range(count):
        no_of_orders = int(input("Enter the number of orders sold the next day.\n"))
        orders[i] = no_of_orders
    
    print("Payments of each day:")
    total_payment = 0
    a = 0
    for a in orders:
        if a <= 10:
            payment = a * 5.0
        elif a > 10:
            payment = (10 * 5.0) + ((a - 10) * 8.0)
        print("{:.2f} eur".format(payment))
        total_payment += payment
    print("Total payment: {:.2f} eur".format(total_payment))
    
main()