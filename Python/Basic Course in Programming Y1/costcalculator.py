'''
Created on 16.10.2018

@author: mikaeltunturi
'''
def main():
    osallistujat_lkm = int(input("Enter the number of the participants.\n"))
    while osallistujat_lkm < 2:
        print("The number must be at least 2!")
        osallistujat_lkm = int(input("Enter the number of the participants.\n"))
    kustannukset = [0.0] * osallistujat_lkm
    kok_kustannukset = 0
    for i in range(osallistujat_lkm):
        yks_kustannukset = float(input("Enter the sum (eur) paid by participant no {:d}.\n".format(i + 1)))
        kustannukset[i] = yks_kustannukset
        kok_kustannukset += yks_kustannukset
    print("Total costs are {:.2f} eur.".format(kok_kustannukset))
    keskiarvo = kok_kustannukset / osallistujat_lkm
    b = 1
    for a in kustannukset:
        if a >= keskiarvo:
            print("Participant no", b, "should receive {:.2f} eur.".format(a - keskiarvo))
            b += 1
        elif a < keskiarvo:
            print("Participant no", b, "should pay {:.2f} eur.".format(keskiarvo - a))
            b += 1
main()