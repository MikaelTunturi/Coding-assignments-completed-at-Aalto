'''
Created on 13.11.2018

@author: mikaeltunturi
'''
def read_file():
    name = input("Enter the name of the file containing the currency rates.\n")
    currency_dictionary = {}
    
    currency_file = open(name, "r")
    for line in currency_file:
        try:
            row = line
            line = line.split(",")
            if len(line) != 2:
                line = row.rstrip()
                print("ERROR in line: {:s}".format(line))
            else:
                if float(line[1]) > 0:
                    currency_dictionary[line[0]] = float(line[1])
                elif float(line[1]) <= 0:
                    line = row.rstrip()
                    print("ERROR: the currency rate is not positive: {:s}".format(line))
        except ValueError:
            line = row.rstrip()
            print("ERROR: the currency rate is not valid: {:s}".format(line))
    return currency_dictionary    
        
def calculate_sum_in_euros(currency_dictionary):
    currency_type = input("Enter the name of the currency (stop by an empty line).\n")
    while currency_type != "":
        if currency_type in currency_dictionary:
            correct_currency = 0
            while correct_currency < 1:    
                try:
                    sum = float(input("Enter the sum in that currency.\n"))
                    sum_in_euros = sum / currency_dictionary[currency_type]
                    print("The sum is {:.2f} euros.".format(sum_in_euros))
                    correct_currency += 1
                except ValueError:
                    print("ERROR: give the sum as a decimal number!")
        else:    
            print("ERROR: unknown currency.")
        currency_type = input("Enter the name of the currency (stop by an empty line).\n")
        
def main():
    try:
        currency_dictionary = read_file()
        calculate_sum_in_euros(currency_dictionary)
        print("Program closing.")
    except OSError:
        print("ERROR in reading file. Program terminates.")
main()