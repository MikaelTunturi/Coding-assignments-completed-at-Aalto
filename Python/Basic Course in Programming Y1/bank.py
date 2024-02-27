'''
@author: mikaeltunturi
'''
import bank_account

def main():
    eka_olio = bank_account.BankAccount("FI5511112222333344", "Kari Kemisti")
    eka_olio.deposit(112.50)
    print("The balance of the first account is {:.2f} eur.".format(eka_olio.get_balance()))
    eka_olio.withdraw(90.00)
    print("The amount withdrawn from the first account was 90.00 eur.")
    second_id = input("Enter the id of the second bank account.\n")
    second_owner = input("Enter the owner of the second bank account.\n")
    toka_olio = bank_account.BankAccount(second_id, second_owner)
    deposit_2 = float(input("Enter the amount to be deposited into the second account.\n"))
    toka_olio.deposit(deposit_2)
    print("The balance of the second account is {:.2f} eur.".format(toka_olio.get_balance()))
    withdraw_2 = float(input("Enter the amount to be withdrawn from the second account.\n"))
    print("The amount withdrawn was {:.2f} eur.".format(toka_olio.withdraw(withdraw_2)))
    print("The bank accounts:")
    print(eka_olio)
    print(toka_olio)
    transfer_from_1_to_2 = float(input("Enter the amount to be transferred\n"))
    if eka_olio.transfer(transfer_from_1_to_2, toka_olio) == True:
        print("Transfer from the first account into the second account was successful!")
    elif eka_olio.transfer(transfer_from_1_to_2, toka_olio) == False:
        print("It was not possible to carry out the bank transfer!")
    print("Bank accounts at the end:")
    print(eka_olio)
    print(toka_olio)
main()
