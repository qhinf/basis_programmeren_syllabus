from random import randint

def Zet_alles_klaar():
    global score, gok, doelgetal
    score = 0
    gok = 0
    doelgetal = randint(1,100)
    print(doelgetal)

def Welkomstboodschap():
    print("Welkom bij Raad het Getal!")

def Vraag_invoer_gebruiker():
    global gok, score
    gok = int(input("Voer een getal in tussen 1 en 100: "))
    score += 1

def Vergelijk_invoer():
    global gok, doelgetal
    if gok < doelgetal:
        print("Te laag!")
        Vraag_invoer_gebruiker()
    elif gok > doelgetal:
        print("Te hoog!")
        Vraag_invoer_gebruiker()
    else:
        Einduitslag()

def Einduitslag():
    global score
    print("Gefeliciteerd, je hebt het juiste getal geraden!")
    print("Je score is " + str(score))
    print("Dankjewel voor het spelen!")

# Het spel begint hier

Zet_alles_klaar()
Welkomstboodschap()
Vraag_invoer_gebruiker()
Vergelijk_invoer()

