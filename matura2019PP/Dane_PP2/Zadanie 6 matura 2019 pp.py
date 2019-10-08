"""
Matura 2019 pp zadanie 6
(c) Piotr Lysiak
LO Sobolew
"""


with open ("dane.txt","r") as plik:
    nr = 0
    for pesel in plik:
        pesel = pesel.strip()
        nr += 1
        print(nr, ". ", pesel)
