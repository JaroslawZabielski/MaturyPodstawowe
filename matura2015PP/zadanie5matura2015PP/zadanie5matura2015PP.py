"""
Zadanie matura 2015 PP
(C) Jarosław Zabielski, grudzień 2019
LO w Sobolewie
"""

s = []
n = []
licznik = []
licznik2 = []
licznik2odb = []
for l in range(14):
    licznik.append(0)
for l in range(25):
    licznik2.append(0)
    licznik2odb.append(0)

with open("nowe.txt", "r") as nowe:
    for no in nowe:
        n.append(no.strip())

with open("slowa.txt", "r") as slowa:
    for sl in slowa:
        sl = sl.strip()
        s.append(sl)
            # 5.1
        dl = len(sl)
        licznik[dl] += 1
            # 5.2
        if sl in n:
            poz = n.index(sl)
            licznik2[poz] += 1
        slodb = sl[::-1]
        if slodb in n:
            poz = n.index(slodb)
            licznik2odb[poz] += 1

with open('wynik5.txt', 'w') as w:
    w.write('5.1\n')
    for i in range(1, 13):
        w.write(str(i) +
                ': ' +
                str(licznik[i]) +
                '\n')
    w.write('5.2\n')
    for i in range(25):
        w.write(n[i] +
                ' ' +
                str(licznik2[i]) +
                ' ' +
                str(licznik2odb[i]) +
                '\n')