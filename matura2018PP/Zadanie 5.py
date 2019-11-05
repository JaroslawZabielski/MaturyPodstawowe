"""
Zadanie 5 matura 2018PP
(C) Laura Andrzejewska, pażdziernik 2019
LO w Sobolewie
"""
def suma_cyfr(n):
    suma = 0
    while n>0:
        suma += n % 10
        n = n // 10
    return suma




with open("liczby.txt", "r") as plik:
    max_parzysta = 0
    palindromy = 0
    cyfrony30 = ''
    suma_wszystkich_cyfr = 0
    for n in plik:
        n = n.strip()
        #5.2
        print(n, " : ", n[ : : -1])
        if n == n[::-1]:
            palindromy = palindromy + n + '\n'
            cyfrony = 30
        # 5.1
        n = int(n)
        if n % 2 == 0:
            if n > max_parzysta:
                max_parzysta = n


                #5.3
                suma_wszystkich_cyfr += suma_cyfr(n)
                if suma_cyfr(n) > 30:
                    cyfrony30 += str(n) +"\n"


with open("wyniki.txt", "w") as wyniki:
    wyniki.write("5.1\n"
                        + str(max_parzysta)
                        + "\n\n5.2\n"
                        + palindromy
                        + "\n5.3\n"
                        + cyfrony30
                        + 'Suma wszystkich cyfr: '
                        + str(suma_wszystkich_cyfr))