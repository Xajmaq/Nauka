import random
tajna_liczba = random.randint(1, 10)
zgadnij = 0
while zgadnij != tajna_liczba: # != sprawdza czy liczby są nierowne
    zgadnij = int(input("Zgadnij liczbę od 1 do 10: "))

print("Brawo! Zgadłeś!")
