imie = input("Podaj swoje imię: ")
wiek = int(input("Podaj swoje wiek: "))
miasto = input("Mieszkam w...: ")

print(f"Cześć, mam na imię {imie}, mam {wiek} lat i mieszkam w {miasto}")
if wiek >= 18:
    print("Jestem Pełnoletni")
elif wiek >= 12:
    print("Jestem nastolatkiem")
else:
    print("Jestem dzieckiem")

a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))

print(f"Suma liczb: {a + b}")
print(f"Różnica liczb: {a - b}")
print(f"Iloczyn liczb: {a * b}")
print(f"Iloraz liczb: {a / b}")
print(f"Reszta z dzielenia liczb: {a % b}")
print(f"Iloraz całkowity: {a // b}")
print(f"Potęga liczb: {a ** b}")

szerokosc = int(input("Podaj szerokość: "))
wysokosc = int(input("Podaj wysokość: "))

# float użyszamy jak chcemy mieć cyfry z przecinkiem a int bez.

print(f"Pole Prostokąta równa się: {szerokosc * wysokosc}")

zwierze = input("Podaj zwierze: ")
kolor = input("Podaj kolor zwierzęcia: ")
wiek_psa = int(input("Podaj wiek zwierzęcia: "))

print(f"Mam {kolor} {zwierze} który ma {wiek_psa} lata.")
if 18>= wiek_psa <=99:
    print ("Iście stary zwierzak")
elif wiek_psa >= 100:
    print ("To on pamięta Marszałka!")
else:
    print("Młody wiek")

liczba = int(input("Podaj liczbę: "))
if liczba % 2 == 0:
    print("Liczba jest parzysta.")
else:
    print("Liczba jest nieparzysta.")

ocena = int(input("Podaj ocenę szkolną: "))

if ocena == 1:
    print("Ocena jest Niedostateczna")
elif ocena == 2:
    print("Ocena jest Dostateczna")
elif ocena == 3:
    print("Ocena jest Dopuszczająca")
elif ocena == 4:
    print("Ocena jest Dobra")
elif ocena == 5:
    print("Ocena jest Bardzo dobra")
elif ocena == 6:
    print("Ocena jest Celująca")
else:
    print("Wróć do szkoły! To nie jest ocena szkolna!")

liczba1 = float(input("Podaj pierwszą liczbę do porównania: "))
liczba2 = float(input("Podaj drugą liczbę do porównania: "))

if liczba1 > liczba2:
    print("Pierwsza liczba jest większa.")
elif liczba1 < liczba2:
    print("Druga liczba jest większa.")
else:
    print("Obie są równe")

# Wiek zwierzęcia do poprawy