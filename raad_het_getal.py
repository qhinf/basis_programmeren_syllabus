from random import randint

# Startscherm
print("Welkom bij Raad-het-getal")
score = 0
doelgetal = randint(1,100)

goedgeraden = False

while not goedgeraden:
    # Invoer van de gebruiker
    invoer = int(input())
    score += 1

    # Vergelijking en feedback
    if invoer < doelgetal:
        print("Te laag")
    elif invoer > doelgetal:
        print("Te hoog")
    else: # invoer == doelgetal
        goedgeraden = True

# Einduitslag
print("Gefeliciteerd! Je hebt het getal juist geraden")
print("Je score is " + str(score) + " punten.")