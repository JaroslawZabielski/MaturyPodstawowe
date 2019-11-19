"""
Zadanie 4
Matura 2017 PP
Mateusz Skoczek
"""

#################################################

with open('liczby.txt', 'r') as plik:
    dane = plik.read().split('\n')[:-1]

#################################################

dane_liczby = []
for x in dane:
    ciag = []
    t = x.split(' ')
    for c in t:
        ciag.append(int(c))
    dane_liczby.append(ciag)

#################################################

licznik1 = 0
for x in dane:
    liczby = x.split(' ')
    if int(liczby[1]) > int(liczby[0]) and int(liczby[2]) > int(liczby[1]):
        licznik1 += 1

#################################################

suma_dzielników = 0
for x in dane_liczby:
    nwd = 0
    for dzielnik in range(1, 32768):
        if x[0] % dzielnik == 0 and x[1] % dzielnik == 0 and x[2] % dzielnik == 0:
            nwd = dzielnik
    suma_dzielników += nwd

#################################################

licznik31 = 0
nsc = 0
liczba_nsc = 0
for x in dane:
    suma_cyfr = 0
    x = x.split(' ')
    y = ''
    for m in x:
        y += m
    for c in y:
        suma_cyfr += int(c)

    if suma_cyfr == 35:
        licznik31 += 1

    if suma_cyfr > nsc:
        nsc = suma_cyfr
        liczba_nsc = 1
    elif suma_cyfr == nsc:
        liczba_nsc += 1

#################################################

with open('wyniki4.txt', 'w') as wyniki:
    wyniki.write('1.\n')
    wyniki.write(str(licznik1) + '\n\n')
    wyniki.write('2.\n')
    wyniki.write(str(suma_dzielników) + '\n\n')
    wyniki.write('3.\n')
    wyniki.write('Liczba wierszy, gdzie suma cyfr = 35: ' + str(licznik31) + '\n')
    wyniki.write('Największa suma cyfr:' + str(nsc) + '\n')
    wyniki.write('Liczba wierszy, w których suma cyfr jest równa największej sumie cyfr: ' + str(liczba_nsc))
