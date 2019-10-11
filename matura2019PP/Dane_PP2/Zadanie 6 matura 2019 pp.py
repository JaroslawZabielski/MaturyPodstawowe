"""
Matura 2019 pp zadanie 6
(c) Piotr Lysiak
LO Sobolew
"""
def Dobry_pesel(a):
    ok = True
    suma = 1* int(a[0]) + 3* int(a[1]) + 7* int(a[2]) + 9* int(a[3]) + 1* int(a[4]) + 3* int(a[5]) + 7* int(a[6]) + 9* int(a[7]) + 1* int(a[8]) + 3* int(a[9]) + int(a[10])
    if suma%10 == 0:
        ok = True
    else:
        ok = False
    return ok
with open ("dane.txt","r") as plik:
    #6.1
    nr = 0
    k = 0
    m = 0
    listopad = 0
    zlepesele = ""
    for pesel in plik:
        pesel = pesel.strip()
        nr += 1
        if int(pesel[9])%2 == 0:
            k += 1
        else:
            m += 1
        #6.2
        mm = str(pesel[2] + pesel[3])
        if mm == "11" or mm == "31":
            listopad += 1
        if Dobry_pesel(pesel) == False:
            zlepesele  = zlepesele + pesel + "\n"

with open("wyniki6.txt","w") as wyniki:
    wyniki.write("6.1\n"+ "Licznik kobiet - " + str(k) + "\nLicznik mężczyzn - " +str(m) +
                 "\n6.2\nUrodzeni w listopadzie - " + str(listopad) + "\n6.3\n" + zlepesele)



