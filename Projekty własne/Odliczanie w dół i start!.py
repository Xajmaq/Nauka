# W pycharm nie da się oddtworzyć dzięku brzęczka systemowego a nie mam podłaczonych głosników więc

import time
import winsound


def beep_sound(freq=800, duration=300):
    winsound.Beep(freq, duration)

    # print('\a', end="", flush=True) # Dzwięk systemowy (beep)

def rocket_effect():
    rakieta = [
        "    ^",
        "   /^\\",
        "  /___\\",
        " |     |",
        " |     |",
        " |_____|",
        " /     \\",
        "/_______\\",
    ]
    for linia in rakieta:
        print(linia)
        time.sleep(0.2)

tekst = "Ground Control to Major Tom\n" # \n wstawione w tekście zaczyna nową linię
for znak in tekst:
    print(znak, end="", flush=True) # end="" sprawia, że kolejny print() dopisują tekst w tej samej linii.
    time.sleep(0.05)

for i in range(10, 5, -1): #10 wartość startowa, 0 wartość końcowa (0 się nie wlicza) -1 o ile się zmiejsza wartość
    print(i, flush=True)
    beep_sound()
    time.sleep(1)

tekst2 = "Commencing countdown, engines on\n"
for znak in tekst2:
    print(znak, end="", flush=True) # flush=True wymusza natychmiastowe wyświetlenie tekstu
    time.sleep(0.05)

for i in range(5, 1, -1):
    print(i, flush=True)
    beep_sound()
    time.sleep(1)

tekst3 = "Check ignition and may God's love be with you\n"
for znak in tekst3:
    print(znak, end="", flush=True)
    time.sleep(0.05)

for i in range(1, 0, -1):
    print(i, flush=True)
    beep_sound()
    time.sleep(1)

print("\nLIFTOFF!\n")
for freq in range(600, 1200, 100):
    beep_sound(freq, 200)
    time.sleep(0.1)

rocket_effect()