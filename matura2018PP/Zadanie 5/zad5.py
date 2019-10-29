"""
Zadanie 5
Matura 2018 PP
Mateusz Skoczek
"""

####################################################

with open('liczby.txt', 'r') as dane:
    dane = dane.read().split('\n')
    liczby = []
    for d in dane[:-1]:
        liczby.append(int(d))

####################################################

najw_parzysta = 0
for x in liczby:
    if x % 2 == 0 and x > najw_parzysta:
        najw_parzysta = x

####################################################

palindromy = []
for x in dane[:-1]:
    if x == x[::-1]:
        palindromy.append(int(x))

####################################################

suma_cyfr = 0
suma_30 = []
for x in dane[:-1]:
    liczniksum = 0
    for c in x:
        liczniksum += int(c)
        suma_cyfr += int(c)
    if liczniksum > 30:
        suma_30.append(int(x))

####################################################

with open('wyniki5.txt', 'w') as wyniki:
    wyniki.write('1.\n')
    wyniki.write(str(najw_parzysta) + '\n\n')
    wyniki.write('2.\n')
    for p in palindromy:
        wyniki.write(str(p) + '\n')
    wyniki.write('\n3.\n')
    for s in suma_30:
        wyniki.write(str(s) + '\n')
    wyniki.write('Całkowita suma cyfr: ' + str(suma_cyfr))