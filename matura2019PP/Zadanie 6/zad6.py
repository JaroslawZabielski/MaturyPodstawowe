"""
Zadanie 6 - 2019 PP
Mateusz Skoczek
"""



with open('dane.txt', 'r') as dane:
    dane = dane.read().split('\n')
    pesele = []
    for x in dane[:-1]:
        pesele.append(x)

####################################

licznikm = 0
licznikk = 0
for x in pesele:
    x = int(x[-2])
    if x % 2 == 0:
        licznikk += 1
    else:
        licznikm += 1

####################################

licznik2 = 0
for x in pesele:
    x = str(x)[2:4]
    if x == '11' or x == '31' or x == '51' or x == '71' or x == '91':
        licznik2 += 1

####################################

bledne_pesele = []
for x in pesele:
    x = str(x)
    l = 1 * int(x[0]) + 3 * int(x[1]) + 7 * int(x[2]) + 9 * int(x[3]) + 1 * int(x[4]) + 3 * int(x[5]) + 7 * int(x[6]) + 9 * int(x[7]) + 1 * int(x[8]) + 3 * int(x[9]) + int(x[10])
    if l % 10 != 0:
        bledne_pesele.append(x)

####################################

with open('wyniki6.txt', 'w') as wyniki:
    wyniki.write('6.1.\n')
    wyniki.write('Mężczyźni: ' + str(licznikm) + '\n')
    wyniki.write('Kobiety: ' + str(licznikk) + '\n\n')
    wyniki.write('6.2.\n')
    wyniki.write('Osób urodzonych w listopadzie: ' + str(licznik2) + '\n\n')
    wyniki.write('6.3.\n')
    for x in bledne_pesele:
        wyniki.write(x + '\n')