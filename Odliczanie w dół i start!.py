import time

tekst = "Ground Control to Major Tom\n" # \n wstawione w tekście zaczyna nową linię
for znak in tekst:
    print(znak, end="", flush=True) # end="" sprawia, że kolejny print() dopisują tekst w tej samej linii.
    time.sleep(0.05)

for i in range(10, 5, -1): #10 wartość startowa, 0 wartość końcowa (0 się nie wlicza) -1 o ile się zmiejsza wartość
    print(i, flush=True)
    time.sleep(1)

tekst2 = "Commencing countdown, engines on\n"
for znak in tekst2:
    print(znak, end="", flush=True) # flush=True wymusza natychmiastowe wyświetlenie tekstu
    time.sleep(0.05)

for i in range(5, 1, -1):
    print(i, flush=True)
    time.sleep(1)

tekst3 = "Check ignition and may God's love be with you\n"
for znak in tekst3:
    print(znak, end="", flush=True)
    time.sleep(0.05)

for i in range(1, 0, -1):
    print(i, flush=True)
    time.sleep(1)

print("liftoff!")