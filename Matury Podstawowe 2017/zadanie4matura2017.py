#zadanie , 4 matura 2017 pp
#(C) Magdalena Darmetko
#LO w Sobolewie

def NWD(a, b, c):
    nwd = 1
    min_l = min(a, b, c)
    for i in range(2 ,min_l + 1):
        if a % i == 0 and b % i == 0 and c % i == 0:
            nwd = i
    return nwd

def sumaCyfr(a):    # a typu str
    s = 0
    for c in a:
        s += int(c)
    return s


licznik1 = 0
licznik35 = 0
sumaNWD = 0
maxSumaCyfr = 0
licznik3 = 1

print(NWD(12, 24, 18))

with open("liczby.txt", "r") as liczby:
    for L in liczby:
        L = L.strip()
        print(L)
        L = L.split(" ")

        #4.3
        SumaCyfrWiersza = sumaCyfr(L[0]) + sumaCyfr(L[1]) + sumaCyfr(L[2])
        if SumaCyfrWiersza == 35:
            licznik35 += 1


        L[0] = int(L[0])
        L[1] = int(L[1])
        L[2] = int(L[2])
        #4.1
        if L[0] < L[1] and L[1] < L[2]:
            licznik1 += 1
        if SumaCyfrWiersza > maxSumaCyfr:
            maxSumaCyfr = SumaCyfrWiersza
            licznik3 = 1
        elif SumaCyfrWiersza == maxSumaCyfr:
            licznik3 += 1
        #4.2
        sumaNWD += NWD(L[0] , L[1] ,L[2])

with open("wyniki4.txt", "w") as wyniki:
    wyniki.write("4.1\n"
                 + str(licznik1) + "\n\n")
    wyniki.write("4.2\n"
                 + str(sumaNWD) + "\n\n")
    wyniki.write("4.3\n"
                 + str(licznik35) + "\n"
                 + str(maxSumaCyfr) + "\n"
                 + str(licznik3))

