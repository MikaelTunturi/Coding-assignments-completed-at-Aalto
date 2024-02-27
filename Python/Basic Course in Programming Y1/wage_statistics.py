'''
Created on 16.10.2018

@author: mikaeltunturi
'''
def calculate_daily_pay(daily_hours, hourly_wages):
    if daily_hours <= 8:
        daily_pay = daily_hours * hourly_wages
    elif 8 < daily_hours <= 10:
        daily_pay = 8 * hourly_wages + (daily_hours - 8) * 1.5 * hourly_wages
    elif daily_hours > 10:
        daily_pay = 8 * hourly_wages + 2 * 1.5 * hourly_wages + (daily_hours - 10) * 2.0 * hourly_wages
    return daily_pay

def read_hours():
    print("Enter the working hours. Stop by giving a negative value.")
    hours_list = []
    daily_hours = float(input("Enter the working hours of the 1st worker:\n"))    
    if daily_hours >= 0: 
        hours_list.append(daily_hours)    
    while daily_hours >= 0:
        daily_hours = float(input("Enter the working hours of the next worker:\n"))
        if daily_hours >= 0: 
            hours_list.append(daily_hours)
    return hours_list

def calculate_wages(hours_list, hourly_wages):
    wages_list = []
    for i in hours_list:
        daily_pay = calculate_daily_pay(i, hourly_wages)
        wages_list.append(daily_pay)
    return wages_list

def calculate_average(wages_list):
    average = sum(wages_list) / len(wages_list)
    return average

def wages_out_of_interval(wages_list, lower_limit, upper_limit):
    LKM = 0
    for i in wages_list:
        if i < lower_limit or i > upper_limit:
            LKM += 1
    return LKM
        
def output_wages(wages_list):
    print("Wages:")
    for i in wages_list:
        print("{:.2f} eur".format(i))
    
def main():
    hourly_wages = float(input("Enter the hourly wages in euros:\n"))
    hours_list = read_hours()
    if len(hours_list) > 0:
        wages_list = calculate_wages(hours_list, hourly_wages)
        average = calculate_average(wages_list)
        lower_limit = 0.75 * average
        upper_limit = 1.25 * average
        LKM = wages_out_of_interval(wages_list, lower_limit, upper_limit)
        output_wages(wages_list)
        print("The average wage is {:.2f} eur.".format(average))
        print("The number of the wages that differs over 25 % from the average is {:d}.".format(LKM))
    else:
        print("No working hours were entered.")
main()