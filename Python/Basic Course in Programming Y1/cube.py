'''
@author: mikaeltunturi
'''
def cuber(input_number):
    number_cubed = input_number ** 3
    return(number_cubed)

def main():
    input_number = int(input("Enter a number to cube:\n"))
    number_cubed = cuber(input_number)
    print("Your number cubed is", number_cubed)

main()
