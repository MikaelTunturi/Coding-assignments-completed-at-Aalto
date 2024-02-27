'''
@author: mikaeltunturi
'''
def main():
    tulos = input("Enter the lengths of the throws (m) separated by commas.\n")
    lista = tulos.split(",")

    if lista[0] == (""):
        print("No accepted results.")
    else:
        paras_tulos = 0
        for i in lista:
            i = float(i)
            if i > paras_tulos:
                paras_tulos = i
        print("The best result is {:.2f} m.".format(paras_tulos))
    
main()
