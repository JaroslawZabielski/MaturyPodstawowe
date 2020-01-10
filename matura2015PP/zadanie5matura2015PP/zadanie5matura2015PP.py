"""
Zadanie matura 2015 PP
(C) Jarosław Zabielski, grudzień 2019
LO w Sobolewie
"""

s = []
n = []

with open("slowa.txt", "r") as slowa:
    for sl in slowa:
        sl = sl.strip()
        s.append(sl)
    print(s[1])
with open("nowe.txt", "r") as nowe:
    for no in nowe:
        n.append(no.strip())
    print(n)