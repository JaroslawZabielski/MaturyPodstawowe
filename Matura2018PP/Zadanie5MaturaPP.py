"""
Zadanie 5 matura 2018 PP
(C) Rafal Kalbarczyk, pazdziernik 2019r
LO w Sobolewie
"""


#5.1

with open("liczby.txt",'r') as plik:
    liczby = []
    liczbyS = []
    for n in plik:
        n = n.strip()
        liczby.append(int(n))
        liczbyS.append(str(n))
        """naj_parzysta = str(0)
        if n % 2 == 0 and n > naj_parzysta:
            n = naj_parzysta
    print(najwieksza_parzysta)"""
    print(liczby)
    parzyste =[]
    naj_parzysta = 2
    for x in liczby:
        if x % 2 == 0 and x > naj_parzysta:
            naj_parzysta = x

#5.2
    palindromy = []
    for x in liczby:
        x = str(x)
        if x == x[::-1]:
            palindromy.append(x)
#5.3
    suma_cyfr = []
    wieksze_od_30 = []
    suma_wszystkich_cyfr = 0
    for x in liczbyS:
        liczniksum = 0
        for c in x:
            liczniksum += int(c)
            suma_wszystkich_cyfr += int(c)
        if liczniksum > 30:
            wieksze_od_30.append(x)




    with open("wyniki.txt","w") as wyniki:
        wyniki.write("5.1\n" + str(naj_parzysta) +
                     "\n5.2\n" + str(palindromy) +
                     "\n5.3\n" + str(wieksze_od_30) +
                     "\n" + str(suma_wszystkich_cyfr)
                     )