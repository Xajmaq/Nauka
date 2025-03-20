# Liczby parzyste

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# Wypisz liczby parzyste od 1 do 50

# Można w ten sposób także wypisać wielokrotności tej samej liczny

for i in range(2, 51, 2): # start od 2 skok co 2
    print(i)

# Liczby nieparzyste

n = int(input("Podaj cyfrę n: "))
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i)
