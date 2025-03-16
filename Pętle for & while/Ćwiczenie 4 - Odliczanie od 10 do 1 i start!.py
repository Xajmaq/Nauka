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