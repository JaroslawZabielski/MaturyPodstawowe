def NWD(a, b, c):
    nwd = 1
    min_1 = min(a, b, c)
    for i in range(2, min_1 + 1):
        if a % i == 0 and b % i == 0 and c % i == 0:
            nwd = i
    return nwd
def SumaCyfr(a):
    suma = 0
    for cyfra in a:
        suma += int(cyfra)
    return suma

rosnaco = int(0)
suma_nwd = 0
licznik35 = 0
najwieksza = 0
najwieksza_w_ilu = 1
with open ("liczby.txt","r") as dane:
    for L in dane:
        L = L.strip()
        L = L.split(" ")
        SumaCyfrWiersza = SumaCyfr(L[0] + L[1] + L[2])
        if SumaCyfrWiersza == 35:
            licznik35 += 1
        if SumaCyfrWiersza > najwieksza:
            najwieksza = SumaCyfrWiersza
            najwieksza_w_ilu = 1
        elif SumaCyfrWiersza == najwieksza:
            najwieksza_w_ilu += 1

        L[0] = int(L[0])
        L[1] = int(L[1])
        L[2] = int(L[2])

        if L[0] < L[1] < L[2]:
            rosnaco += 1

        suma_nwd += NWD(L[0], L[1], L[2])


with open ("wyniki4.txt", "w") as wyniki:
    wyniki.write("4.1\n" + str(rosnaco))
    wyniki.write("\n4.2\n" + str(suma_nwd))
    wyniki.write("\n4.3\n" + str(licznik35) + "\n" + str(najwieksza) + "\n" + str(najwieksza_w_ilu))