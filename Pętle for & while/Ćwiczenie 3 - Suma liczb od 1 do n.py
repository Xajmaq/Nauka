# Suma liczb od 1 do n

n = int(input("Podaj liczbę n: "))
suma = 0 # Tworzymy zmienną do przechowywania sumy, początkowo suma jest równa 0 bo nic nie dodaliśmy!

for i in range(1, n + 1): # Zakres o 1 do n
    suma += i # Dodajemy i do sumy

# range(1, n + 1) tworzy listę liczb od 1 do n
# suma += i oznacza suma = suma + i czyli dodajemy kolejne liczby do sumy.

print("Suma liczb od 1 do", n,"wynosi:", suma)



# print(((1+n)/2)*n)
# Moje rozwiązanie :P Prosty wzór na Ciąg arytmetyczny :P Ech, stary człowiek jestem.
