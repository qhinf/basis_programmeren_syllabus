# Handige programmeerpatronen

Zoals je misschien al gemerkt hebt tijdens het werken in CS Circles, komen bepaalde programmeerpatronen vaker voor. Net zoals bij het communiceren in de klas, waar ook patronen in voorkomen. Bijvoorbeeld aan de leerkracht vragen of je even naar de WC mag. Daar zit een patroon in. We gaan in dit hoofdstuk een aantal van deze patronen bekijken.

## Validatie van je invoer
Bij het schrijven van een programma is het belangrijk om rekening te houden met wat een gebruiker kan invoeren. Vaak verwachten we dat de gebruiker bijvoorbeeld een getal invoert, maar wat gebeurt er als de gebruiker een letter of een ander symbool invoert? In CS Circles heb je de volgende code geleerd om gebruikers een getal in te laten voeren.

```python
getal = int(input("Voer een getal in: "))
```

Als de gebruiker inderdaad een geldig getal invoert, gaat alles goed. Maar wat gebeurt er als de gebruiker per ongeluk een letter typt, bijvoorbeeld ‘a’? In dat geval krijgt de gebruiker een foutmelding zoals deze:

```python
ValueError: invalid literal for int() with base 10: 'a'
```

De uitvoer van je programma stopt en dat is eigenlijk niet bedoeling. Er zijn verschillende manieren om dit op te lossen. Een van die manieren gaan we nu ontdekken. Het idee is dat je net zo lang om invoer vraagt, totdat de invoer juist is. Dat ziet er in een zogenaamde *flowchart* als volgt uit.

```{image} assets/invoer_validatie.png
:align: center
```

Je begint met het aannemen dat er nog geen correcte invoer is. Wat natuurlijk ook klopt, want er is helemaal geen invoer. Vervolgens ga je de gebruiker net zolang lastig vallen totdat er een juiste invoer is. Laten we weer het voorbeeld van het invoeren van een getal nemen. Gecombineerd met de flowchart van hierboven levert dit de volgende Python-code op.

```python
# invoer validatie

invoerCorrect = False

while not invoerCorrect:
    invoer = input("Voer een getal in: ")

    if invoer.isdigit():
        invoerCorrect = True

# na deze lus weten we zeker dat de invoer een getal is.
```

We hebben hiervoor een nieuwe functie gebruikt. `.isdigit()`. Met deze functie kun je kijken of een string een getal is of niet. Wanneer de string alleen maar cijfers bevat, zal deze `True` opleveren. Wanneer er ook maar één letter of ander teken, wat niet een cijfer is, zal deze `False` opleveren. Dat is natuurlijk erg handig voor onze functie.

Deze code is natuurlijk niet echt vriendelijk. Het programma geeft geen enkele vorm van feedback. Dit kunnen we als volgt aanpassen.

```python
# invoer validatie

invoerCorrect = False

while not invoerCorrect:
    invoer = input("Voer een getal in: ")

    if invoer.isdigit():
        invoerCorrect = True
    else: # de invoer is geen getal
        # feedback boodschap
        print("De invoer is geen getal. Probeer opnieuw!")

# na deze lus weten we zeker dat de invoer een getal is.
```

Nu zal het programma elke keer, wanneer er geen getal ingevoerd wordt de gebruiker vertellen dat de invoer geen getal is. Wel zo vriendelijk!

We kunnen hier nog een mooie functie van maken, zodat we deze code vaker kunnen gebruiken. Je mag deze code ook gebruiken in je eigen code. Let op dat deze code dus alleen werkt bij de invoer van getallen.

```python
# invoer validatie

def getalInvoer():
    invoerCorrect = False

    while not invoerCorrect:
        invoer = input("Voer een getal in: ")

        if invoer.isdigit():
            invoerCorrect = True
        else: # de invoer is geen getal
            # feedback boodschap
            print("De invoer is geen getal. Probeer opnieuw!")

    # na deze lus weten we zeker dat de invoer een getal is.

    return int(invoer)

a = getalInvoer()
print(f"Je hebt het getal {a} ingevoerd")
```

:::{exercise} Bepaalde getallen
Het programma van het bovenstaande voorbeeld accepteert alle positieve getallen. Herschrijf de functie `getalInvoer()` zodat alleen de getallen `1, 2, 3, 4, 5, 6, 7, 8, 9` en `10` geaccepteerd worden.
Let op dat je de feedback bij foutieve invoer ook aanpast.

:::

:::{exercise} Ja of nee
We hebben tot nu toe alleen nog maar gekeken naar de invoer van getallen. Het is natuurlijk ook handig om een functie te hebben, die `J` of `N` accepteert op het moment dat je een gesloten vraag stelt.

1. Vraag de gebruiker: `Wilt u doorgaan? (J/N) `
2. Accepteer alleen `J` of `N` als invoer.
3. Pas de feedback boodschap aan.

Hint: de gebruiker zal natuurlijk ook `j` of `n` in willen kunnen voeren. Gebruik hiervoor de functie `.upper()` op een slimme manier. In Python zal `"informatica".upper()` dus de string `"INFORMATICA"` opleveren.

:::

::::{exercise} Echt alle getallen. Een uitdaging.
De functie `getalInvoer()`, die we hierboven geschreven hebben, heeft nog steeds wat beperkingen. Probeer maar eens wat wildere getallen in te voeren. Bijvoorbeeld `3.2` of `-4`. Deze worden niet geaccepteerd.

We passen de functie `getalInvoer()` nu als volgt aan. Je ziet dat er een functie `isGetal()` bijgekomen is. Schrijf deze functie zodat:

1. Kommagetallen zoals `0.33` of `123.356` geaccepteerd worden. `0.33.33` is natuurlijk geen getal.
2. Negatieve getallen zoals `-2` of `-4.778` geaccepteerd worden. `--3` is natuurlijk geen getal. `+4` mag ook nog even niet meedoen.

Hint 1: je mag natuurlijk zelf hulp functies schrijven `isKommaGetal()` en `isGeheelGetal()`.

Hint 2: je kunt je er met enkele regels code vanaf maken door RegExp te gebruiken. Let op: dit is voor gevorderden. Het is niet erg wanneer je dit niet kan.  

```python
def isGetal(str):
    # schrijf hier jouw code

    # return
    pass # haal deze regel weg wanneer je klaar bent met schrijven

def kommaGetalInvoer():
    invoerCorrect = False

    while not invoerCorrect:
        invoer = input("Voer een getal in: ")

        if isGetal(invoer):
            invoerCorrect = True
        else: # de invoer is geen getal
            # feedback boodschap
            print("De invoer is geen getal. Probeer opnieuw!")

    # na deze lus weten we zeker dat de invoer een getal is.

    return float(invoer)

a = kommaGetalInvoer()
print(f"Je hebt het getal {a} ingevoerd")
```

::::

## De interactie lus

Het gebruik van `while`, wat we hierboven hebben gezien, kunnen we aanpassen zodat we het ook voor meer dan de validatie van invoer kunnen gebruiken.

Stel dat je een klein spelletje in het console aan het schrijven bent. Wanneer het spelletje klaar is, wil je aan de gebruiker vragen of die nog een keer wil spelen. Wanneer de gebruiker met *Nee* antwoordt is het simpel, dan is het spel klaar. Maar wanneer de gebruiker nog een keer wil spelen, dan zul je een manier moeten verzinnen om terug te gaan naar het begin. Dit kun je zien in de volgende flowchart.

```{image} assets/Gameloop.png
:align: center
```

Dit vertaal je als volgt naar Python-code:

```python

def vraagJaNee():
    # Dit is natuurlijk een opdracht bij de vorige paragraaf ^^
    # Je geeft de string "J" of "N" terug
    pass

spelActief = True

while spelActief:
    # initialiseer spel
    # speel het spel tot het klaar is

    doorgaan = vraagJaNee()

    if doorgaan == "N": spelActief = False
    elif doorgaan == "J": print("Leuk! We gaan nog een keer spelen.")

print("Bedankt voor het spelen en tot een volgende keer!")

```

Het gebruik van `while` en een variabele als `spelActief` of `invoerCorrect` heet programmeren met *state* of *toestand*. Je maakt in je programma keuzes op basis van de toestand van je programma. Wanneer je je spelverloop beschrijft en termen gebruikt als '*net zolang als*' of '*totdat er*' gebruikt, dan doe je er verstandig aan een `while`-loop met een toestand variabele te gebruiken!