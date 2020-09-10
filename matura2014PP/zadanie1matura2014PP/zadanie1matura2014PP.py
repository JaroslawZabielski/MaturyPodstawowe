"""
Zadanie 1 matura 2014 PP
(C) Jarosław Zabielski, styczeń 2020
LO w Sobolewie
"""

n = 6
print(n)
d = 1
iloczyn = 1
while d <= n/2:
    if n%d == 0:
        print(d)
        iloczyn *= d

    d += 1
print(iloczyn)
if iloczyn == n:
    print("TAK")
else:
    print("NIE")