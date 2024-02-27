'''
@author: mikaeltunturi
'''
def read_file():
    name = input("Input the name of the file to be read:\n")
    sales_profit_list = []
    car_file = open(name, "r")
    info_list = []
    xd_list = []
    for i in car_file:
        xd_list.append(i)
        row = i.split(",")
        info_list.append(row)
    a = 0
    for line in info_list:
        try:
            if int(len(line)) != 5:
                line = xd_list[a].rstrip()
                print("ERROR: incorrect line: {:s}".format(line))
                a += 1
            elif int(len(line)) == 5:
                sales_profit = float(line[4]) - float(line[3])
                sales_profit_list.append(sales_profit)
                a += 1
        except ValueError:
            line = xd_list[a].rstrip()
            print("ERROR: incorrect price in line: {:s}".format(line))
            a += 1
    return sales_profit_list    
        
def calculate_profit(sales_profit_list):
    total_profit = 0
    for sales_profit in sales_profit_list:
        total_profit += float(sales_profit)
    return total_profit
    
def main():
    try:
        sales_profit_list = read_file()
        if sales_profit_list == ([]):
            print("There was no information about sold cars in the file.")
        else:
            print("Finished reading the file.")
            print("Profits (eur)")
            for sales_profit in sales_profit_list:
                print("{:.2f}".format(sales_profit))
            total_profit = calculate_profit(sales_profit_list)
            print("-----------------------------")
            print("Total {:.2f} eur.".format(total_profit))
    except OSError:
        print("ERROR in reading the file.")
main()
