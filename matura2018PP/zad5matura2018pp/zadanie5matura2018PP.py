"""
Zad 5. matura 2018 PP
(C) Marcin Zabiegałowski, październik 2019
LO w Sobolewie
"""
def suma_cyfr(n) :
    suma = 0
    while n > 0
        suma += n % 10
        n = n // 10
    return suma


with open("liczby.txt", "r")  as plik:
    max_parzysta = 0
    palindromy = ''
    for n in plik:
        n =n.strip()
        # 5.2
        print(n," : ", n[::-1])
        if n == n[::-1]:
            palindromy = palindromy + n + '\n'
        # 5.1
        n = int(n)
        if n%2 == 0:
            if n > max_parzysta:
                max_parzysta = n





with open("wyniki5.txt", "w") as wyniki:
    wyniki.write("5.1\n"
                 + str(max_parzysta)
                 + "\n\n5.2\n"
                 + palindromy
                 + "\n5.3\n")


    print(suma_cyfr(1234))

