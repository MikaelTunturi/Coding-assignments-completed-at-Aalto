'''
Created on 13.11.2018

@author: mikaeltunturi
'''
def main():
    name = input("Enter the name of the file containing the bank statement.\n")
    recipient = input("Enter the name of the recipient.\n")
    try:
        bank_file = open(name, "r")
        bank_list = []
        for line in bank_file:
            line = line.split("\t")
            bank_list.append(line)
        del bank_list[0]
        del bank_list[0]
        total_sum = 0
        for line in bank_list:
            if len(line) >= 5:
                try:
                    if recipient == line[4]:
                        total_sum += float(line[3])
                except:
                    pass  
            else:
                pass
        print("The total sum paid to {:s} is {:.2f} eur.".format(recipient, total_sum * -1))
    except OSError:
        print("ERROR in reading file", name)
    except IndexError:
        print("The total sum paid to {:s} is 0.00 eur.".format(recipient))
main()
    