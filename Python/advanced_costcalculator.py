'''
Created on 29.10.2018

@author: mikaeltunturi
'''
def read_names():
    print("Input the names of the participants.")
    print("Stop by entering an empty line.")
    participants = {}
    name = input("")
    while len(name) > 0:
        participants[name] = 0.0
        name = input("")
    return participants
    
def add_costs(cost_statistics):
    print("Next, the information about costs are added")
    print("Stop by entering an empty line as a name.")
    name = input("Enter the name of the participant.\n")
    while len(name) > 0:
        if name in cost_statistics:
            amount = float(input("Enter the amount to be added.\n"))
            if amount >= 0:
                cost_statistics[name] = cost_statistics[name] + amount
            elif amount < 0:
                print("Negative amounts are not added.")
        else:
            print("This name is not among the participants.")
        name = input("Enter the name of the participant.\n")
    print("Information about costs stored.")
    return cost_statistics
    
def calculate_average(cost_statistics):
    if len(cost_statistics) == 0:
        average = 0.0
    else:
        total_amount = 0
        number_of_participants = 0
        for name in cost_statistics:
            total_amount = total_amount + cost_statistics[name]
            number_of_participants += 1
        average = total_amount / number_of_participants
    return average
    
def list_totals(cost_statistics):
    print("Total sums paid:")
    names_in_the_right_order = sorted(cost_statistics)
    for name in names_in_the_right_order:
        print("{:15s} {:8.2f} eur.".format(name, cost_statistics[name]))
    print("")
    
def list_debts(cost_statistics):
    average = calculate_average(cost_statistics)
    names_in_the_right_order = sorted(cost_statistics)
    for name in names_in_the_right_order:
        if cost_statistics[name] < average:
            amount_to_pay_back = average - cost_statistics[name]
            print(name, "should pay {:.2f} eur.".format(amount_to_pay_back))
        elif cost_statistics[name] >= average:
            amount_to_receive = cost_statistics[name] - average
            print(name, "should receive {:.2f} eur.".format(amount_to_receive))
   
def main():
    cost_statistics =  read_names()
    cost_statistics = add_costs(cost_statistics)
    average = calculate_average(cost_statistics)
    list_totals(cost_statistics)
    list_debts(cost_statistics)
    print("The program ends.")
main()