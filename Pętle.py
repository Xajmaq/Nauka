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

# Wpisywanie liczb od 1 do 10
x = 1
while x <= 7:
    print(x)
    x = x + 1
    # lub x += 1

# Przerywanie i pomijanie iteracji
# brake - przerywa pętlę wcześniej.
# continue - pomijaaktualną iterację i przechodzi do następnej.

# brake

for i in range(1,11):
    if i == 6:
        break
    print(i)

# continue

for i in range(1,11):
    if i == 6:
        continue
    print(i)