print("Ćwiczenie 1")

# Wypisz liczby od 1 do 10

for i in range(1, 11):
    print(i)

print ("Ćwiczenie 2")

# Liczby parzyste

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

print("Ćwiczenie 3")

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

print("Ćwiczenie 4")

# Odliczanie od 10 do 1
# Po zakończeniu pętki wypisz "Start!"

#  Pierwszy sposób z pętlą for

for i in range(10, 0, -1): #10 wartość startowa, 0 wartość końcowa (0 się nie wlicza) -1 o ile się zmiejsza wartość
    print(i)
print("Start")

# Pętla while

x = 10
while x > 0:
    print(x)
    x -= 1
print("Start!")
