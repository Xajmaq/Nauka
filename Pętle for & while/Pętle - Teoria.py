# Pętle pozwalają powtarzać fragmenty kodu wiele razy
# bez konieczności ręcznego pisania tych samych instrukcji.

# Pętla for
# Najczęściej używana do przechodzenia po elementach listy, zakresu liczb itp.

# Wyświetlanie liczby od 1-10 (11 nie jest liczone!)
for i in range(1,11):
    print(i)

# Rozbija słowo na litery
tekst = "Python"
for litera in tekst:
    print(litera)

# Pętla while
# Powtarzanie do spełnienia warunku. Działa dopóki warunek jest prawdziwy.

# Wpisywanie liczb od 1 do 7
x = 1
while x <= 7:
    print(x)
    x = x + 1
    # lub x += 1

# Przerywanie i pomijanie iteracji


# brake
# brake - przerywa pętlę wcześniej.

for i in range(1,11):
    if i == 6:
        break
    print(i)

# continue
# continue - pomija aktualną iterację i przechodzi do następnej.

for i in range(1,11):
    if i == 6:
        continue
    print(i)

# Sprawdzanie nierówności

a = 5
b = 10

if a != b:
    print("a i b są różne")

# Użycie != w pętli while

# Program prosi o wpisanie liczby dopóki użytkownik nie poda 5.

liczba = 0

while liczba != 5:
    liczba = int(input("Podaj liczbę: "))
print ("Brawo Podałeś 5.")


# Porównanie tekstu

imie = input("Podaj imie: ")

if imie != Adam:
    print("Nie jesteś Adamem!")
else:
    print("Jesteś Adam!")

