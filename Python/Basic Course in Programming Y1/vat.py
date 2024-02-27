'''
Created on 6.11.2018

@author: mikaeltunturi
'''
def main():
    name = input("Enter the name of the file containing selling prices.\n")
    total_vat = 0
    try:
        vat_file = open(name, "r")
        print("    Price       VAT    Price (incl. VAT)")
        for line in vat_file:
            line = line.rstrip()
            price = float(line)
            vat = 0.24 * price
            total_price = price + vat
            total_vat += vat
            print("{:9.2f} {:9.2f} {:9.2f}".format(price, vat, total_price))
        vat_file.close()
        print("------------------------------------------")
        print("Total VAT {:.2f} eur.".format(total_vat))
    except OSError:
        print("Error in reading file {:s}. Closing program.".format(name))
    except ValueError:
        print("Incorrect line in file {:s}. Closing program.".format(name))
main()