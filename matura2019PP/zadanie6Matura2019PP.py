""""
Zadanie 6 Matura 2019 PP
(C) Rafał Kalbarczyk, październik 2019
LO Sobolew
"""
with open("dane.txt", "r") as plik:
    nr = 0
    for pesel in plik:
        pesel = pesel.strip()
        nr += 1
        print(nr, ". ", pesel)