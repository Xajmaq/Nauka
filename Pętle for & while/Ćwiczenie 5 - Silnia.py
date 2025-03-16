n = int(input("podaj Liczbę "))
silnia = 1

for i in range(1, n + 1):
    silnia *= i

print(f"silnia {n}! wynosi {silnia}")