"""
Zadanie 6
Matura 2016 PP
Mateusz Skoczek
"""

#########################################################

with open('dane_6.txt', 'r') as plik:
    dane = plik.read().split('\n')[:-1]
    dane_l = []
    for d in dane:
        dane_l.append(int(d))

#########################################################

licznik1 = 0
liczby_pierwsze = []
for x in dane_l:
    dzielniki = 0
    for l in range(1, 30001):
        if x % l == 0:
            dzielniki += 1
    if dzielniki == 2:
        licznik1 += 1
        liczby_pierwsze.append(x)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

najwLP = 0
najmLP = 30001
for x in liczby_pierwsze:
    if x > najwLP:
        najwLP = x
    if x < najmLP:
        najmLP = x

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

licznik3 = 0
paryLB = []
poprz = liczby_pierwsze[0]
for x in liczby_pierwsze[1:]:
    if poprz - 2 == x:
        licznik3 += 1
        paryLB.append(str(poprz) + ' ' + str(x))
    elif poprz + 2 == x:
        licznik3 += 1
        paryLB.append(str(poprz) + ' ' + str(x))
    poprz = x

#########################################################

with open('wyniki6.txt', 'w') as wyniki:
    wyniki.write('1.\n')
    wyniki.write(str(licznik1) + '\n\n')
    wyniki.write('2.\n')
    wyniki.write('Największa liczba pierwsza: ' + str(najwLP) + '\n')
    wyniki.write('Najmniejsza liczba pierwsza: ' + str(najmLP) + '\n\n')
    wyniki.write('3.\n')
    wyniki.write('Ilość par liczb bliźniaczych: ' + str(licznik3) + '\n')
    for p in paryLB:
        wyniki.write(p + '\n')