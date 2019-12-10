"""
Zadanie 6 matura 2016 PP
(C) Jarosław Zabielski, grudzień 2019
LO w Sobolewie
"""

import math as m

with open('dane6.txt', 'r') as dane:
    dane = dane.read().split('\n')[:-1]
    liczby = []
    for x in dane:
        liczby.append(int(x))

licznik1 = 0
liczby_pierwsze = []
for x in liczby:
    dzielniki = 0
    for y in range(2,x):
        if x%y==0:
            dzielniki+=1
    if dzielniki == 0:
        licznik1 += 1
        liczby_pierwsze.append(x)

najwieksza = 0
najmniejsza = 10000000000000
for x in liczby_pierwsze:
    if x > najwieksza:
        najwieksza = x
    if x < najmniejsza:
        najmniejsza = x

poprzednia = 0
liczby_blizniacze = []
licznik3 = 0
for x in liczby_pierwsze:
    if m.fabs(poprzednia - x) == 2:
        liczby_blizniacze.append(str(poprzednia)
                                 + ';' + str(x))
        licznik3 += 1
    poprzednia = x

with open('wyniki6.txt', 'w') as wyniki:
    wyniki.write('1.\n'
                 + str(licznik1) + '\n\n')
    wyniki.write('2.\nNajmniejsza: '
                 + str(najmniejsza)
                 + '\nNajwiększa: '
                 + str(najwieksza) + '\n\n')
    wyniki.write('3.\nIlość par: '
                 + str(licznik3) + '\n')
    for x in liczby_blizniacze:
        wyniki.write(x + '\n')