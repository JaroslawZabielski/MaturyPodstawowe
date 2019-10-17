"""
Zadanie 6 Matura 2019 pp
(C) Arkadiusz Zgódka, październik 2019
LO Sobolew
"""

def dobry_pesel(a):
    ok = True
    suma = 1 * int(a[0]) + 3 * int(a[1]) + 7 * int(a[2]) + 9 * int(a[3]) + 1 * int(a[4]) + 3 * int(a[5]) + 7 * int(a[6]) + 9 * int(a[7]) + 1 * int(a[8]) + 3 * int(a[9]) + int(a[10])
    if suma%10 == 0:
        ok = True
    else:
        ok = False
    return ok

with open("dane.txt", "r") as plik:
    nr = 0
    licznikK = 0
    licznikM = 0
    licznik11 = 0
    zlePesele = ""
    for pesel in plik:
        pesel = pesel.strip()
        nr += 1
        # 6.1
        if int(pesel[9])%2 == 0:
            licznikK += 1
        else:
            licznikM += 1
        # 6.2
        mm = pesel[2] + pesel[3]
        if mm == "11" or mm == "31":
            licznik11 += 1
        # 6.3
        if dobry_pesel(pesel) == False:
            zlePesele = zlePesele + pesel + "\n"

with open("wyniki6.txt", "w") as wyniki:
    wyniki.write("6.1\n"
                 + str(licznikK)
                 + " - kobiety\n"
                 + str(licznikM)
                 + " - mężczyźni\n"
                 + "\n6.2\n"
                 + str(licznik11)
                 + "\n"
                 + "\n6.3\n"
                 + zlePesele)
