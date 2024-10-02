(programma_schrijven)=
# Een programma schrijven

Wanneer je klaar bent met de oefeningen van de vorige lessen, dan ben je al een beetje bekend met de basiselementen van de taal Python. Als het goed is, ben je in staat om bijvoorbeeld 5 regels Python-code te schrijven, die doen wat jij wil dat het moet doen. Maar hoe zit dat nou met grotere programma's van bijvoorbeeld 200 regels? Dat is andere koek. Wanneer je programma groter wordt dan wat je nu gewend bent, is het gemakkelijk om het overzicht kwijt te raken en niet te weten wat je moet doen. In dit hoofdstuk staat uitleg en een oefening hoe je een groter programma kunt aanpakken. Dit is best handig voor het maken van de eindopdracht.

## Verdeel en heers
Je hebt vast wel eens een keer in een probleem of puzzel vastgezeten. Er zijn heel veel mogelijkheden om uit zo'n puzzel of probleem te komen. De gemakkelijkste is natuurlijk naar de oplossing kijken, maar dat een beetje flauw. Het is wel de bedoeling dat je zelf tot een oplossing komt. Een van de mogelijkheden is om het probleem op te delen in kleinere problemen. Of de grote stappen op te delen in kleinere stappen. In het programmeer-onderwijs noemen we dit de *Top-Down*-benadering. In deze benadering bekijk je een opdracht van een kleine afstand en breek je de opdracht op in kleinere deelopdrachten. Eigenlijk net zoals je een bord met veel eten aanvalt. Die eet je ook niet in één hap op. 

Met de Top-down benadering voor jouw grotere Python-programma ga je gebruik maken van *Storyboarden*. Een storyboard is een reeks eenvoudige tekeningen, waarmee je laat zien wat er in je programma gebeurt. Dit helpt je na te denken over de structuur van je programma, zonder dat je meteen met Python-code bezig bent. Vervolgens ga je de verschillende delen van het overzicht uitwerken in *pseudo-code*. Dat is een opstap naar echte Python code. Wanneer je alle delen hebt uitgewerkt, kun je aan de slag met het omzetten van je pseudo-code naar werkende Python code en uiteindelijk naar een compleet programma. Dat wordt dus het volgende stappenplan:

(stappenplan)=
:::{admonition} Stappenplan
1. Maak een storyboard van de belangrijkste interacties van je programma
2. Beschrijf elke interactie in pseudocode
3. Zet de pseudocode om in echte codeblokken in Python
4. Lijm de codeblokken aan elkaar tot een echt werkend programma
:::

In een storyboard beschrijf je de belangrijke interacties met de gebruiker van je spel. Je mag dit tekenen/schetsen. Je mag het ook in woorden omschrijven. In het uitgewerkte voorbeeld hieronder worden woorden gebruikt om de belangrijkste interacties te omschrijven. Je kunt zelf natuurlijk de volgende hulpmiddelen ook gebruiken:
- Powerpoint
- Pen en papier (zelfs met kleurtjes)
- Google Slides
- whiteboard (vergeet dan niet een foto te maken, anders raak je je storyboard gemakkelijk kwijt)

De methode van storyboarden kan je later ook helpen, wanneer je programma's wil schrijven met een grafische gebruikersinterface, een GUI. Een programma met echt knoppen, tekstvelden en andere klikbare elementen, zoals op een website of een app. Voor nu blijven we even met tekst werken.

**Voorbeeld**
We gaan het spelletje *Raad het getal* als voorbeeld nemen. In dit spelletje moet de speler een getal raden. De computer zegt dan of je gok te hoog, te laag of juist is. Je score is het aantal pogingen wat je nodig hebt gehad om het getal te raden. Tot zover de beschrijving van het spel.
We gaan een storyboard maken.

### Storyboard Raad het getal

**1. Startscherm**
| | |
|-|-|
|Wat is er te zien? | Een welkomstboodschap op het scherm. Bijv. "Welkom bij Raad het Getal! Voer een getal in tussen 1 en 100." |
|Wat gebeurt er? | Een welkomstboodschap wordt op het scherm gezet.<br/>De score wordt op 0 gezet.<br/>Bepaal het getal wat geraden moet worden. |
|Pseudocode | `Druk welkomstboodschap af.`<br/>`Zet score op 0`<br/>`Kies een willekeurig doelgetal tussen 1 en 100`.|

**2. Invoer van de gebruiker**
| | |
|-|-|
|Wat is er te zien? | Een tekstvak waar de gebruiker een getal in kan voeren. |
|Wat gebeurt er? | Vraag de speler om een getal in te voeren en sla dit getal op als 'gok' |
|Pseudocode | `De speler voert een getal in`<br/>`Sla het getal op.`<br/>`Verhoog de score met 1` |

**3. Vergelijking en feedback**
| | |
|-|-|
|Wat is er te zien? | Een tekst die aangeeft of het ingevoerde getal te hoog, te laag of correct is. |
|Wat gebeurt er? | Het programma vergelijkt de invoer van de speler met het doelgetal en geeft feedback. Als het fout is, wordt de speler gevraagd opnieuw een getal in te voeren. |
|Pseudocode | `Als het ingevoerde getal lager is dan het doelgetal, zeg "Te laag" en ga naar scherm 2.`<br/>`Als het ingevoerde getal hoger is dan het doelgetal, zeg "Te hoog" en ga naar scherm 2.`|

**4. Einduitslag**
| | |
|-|-|
|Wat is er te zien? | Een boodschap met felicitaties en de behaalde score |
|Wat gebeurt er? | Het programma drukt "Gefeliciteerd, je hebt het juiste getal geraden!" en de score af |
|Pseudocode | `Druk felicitatie en score af`|

(storyboard_galgje)=
:::{exercise} Galgje

Je kent het spel Galgje vast wel. Je kiest een woord en de speler moet het woord letter voor letter raden. Je begint met een aantal ..., net zoveel als er letters in het woord zijn. De speler moet een letter raden. Heeft deze het juist, dan zet je de letter op de juiste puntjes. Heeft de speler de letter niet juist, dan wordt de galg iets meer opgebouwd. In totaal mag je meestal 10 letters fout hebben. De fout geraden letters schrijf je ook op.

Je gaat een storyboard maken voor dit spel. Je mag het te raden woord als een variabele gebruiken. Bijvoorbeeld: `woord = 'picknick'`. 

Volg het storyboard sjabloon van *Raad het getal*. Natuurlijk krijg je meer interacties en schermen :)

:::

## Van storyboard naar code blokken
Nu we de belangrijkste interacties van ons programma *Raad het getal* hebben beschreven, gaan we per interactie de Python-code schrijven. Dit zijn nog losse blokken. Je zult zien dat het resultaat al behoorlijk op een werkend programma lijkt. Dit is het nog niet, want het zijn nog losse blokken. In de volgende paragraaf gaan we kijken hoe we deze blokken aan elkaar gaan koppelen.

### Code blokken
**1. Startscherm**

Pseudocode

`Druk welkomstboodschap af.`<br/>`Zet score op 0`.<br/>`Kies een willekeurig doelgetal tussen 1 en 100`|

Python code
```python
# Startscherm
print("Welkom bij Raad-het-getal")
score = 0
doelgetal = randint(1,100)
```

Met de functie `randint` kun je de computer een random integer laten kiezen tussen twee grenzen. In dit geval tussen 1 en 100. Deze functie maakt deel uit van de Python bibliotheek `random`. Voor nu laten we deze code zo staan. Wanneer we het complete programma maken, moeten we nog een extra regel toevoegen aan ons programma willen we het werkend krijgen.

**2. Invoer van de gebruiker**

Pseudocode

 `De speler voert een getal in`<br/>`Sla het getal op.`<br/>`Verhoog de score met 1` 

Python code
```python
# Invoer van de gebruiker
invoer = int(input("Voer een getal in tussen de 1 en de 100: "))
score += 1
```

De regel met `invoer = int(input(...` werkt natuurlijk op zich prima, wanneer de gebruiker ook daadwerkelijk een getal invoert. Je zult bij CS Circles al gemerkt hebben dat Python een vervelende foutmelding geeft wanneer je iets anders dan een geheel getal invoert. Als je het echt een beetje boomer-proof wil maken, dan gebruik je hier een functie met input-validatie!

**3. Vergelijking en feedback**

Pseudocode 

`Als het ingevoerde getal lager is dan het doelgetal, zeg "Te laag" en ga naar scherm 2.`<br/>`Als het ingevoerde getal hoger is dan het doelgetal, zeg "Te hoog".`

Python code
```python

# Vergelijking en feedback
if invoer < doelgetal:
    print("Te laag")
elif invoer > doelgetal:
    print("Te hoog")
```

**4. Einduitslag**

Pseudocode

`Druk felicitatie en score af`

```python
# Einduitslag
print("Gefeliciteerd! Je hebt het getal juist geraden")
print("Je score is " + str(score) + " punten.")
```

:::{exercise} Invoervalidatie blok 2
In de conversie van pseudocode naar Python code in het blok **2. Invoer van gebruikers** wordt in het voorbeeld nog gebruik gemaakt van `int(input())`. Deze code is natuurlijk niet erg robuust. Je kunt als gebruiker het programma snel crashen.

Verander deze code zodanig dat het programma niet meer crashed bij invoer, die geen geheel getal is, maar netjes een foutmelding teruggeeft en alleen gehele getallen als invoer accepteert.
:::

:::{exercise} Python codeblokken Galgje

Schrijf de Python codeblokken op basis van je storyboard van het spel Galgje van opdracht {ref}`storyboard_galgje`

:::

## Van code blokken naar programma
We zijn er nu nog niet. We hebben nu losse codeblokken, maar hebben nog niet vastgesteld wat er nu precies moet gebeuren als de gebruiker het getal niet goed geraden heeft. Het programma moet het dan *weer* aan de gebruiker vragen. Dit wordt een herhaling. Wanneer je er even over nadenkt, dan wil je dat het programma blijft vragen naar de invoer, totdat het juist antwoord is gegeven. Je maakt dan gebruik van een interactie lus. In pseudecode ziet dat er zo uit:

```python
goedgeraden = False

while not goedgeraden: # deze lus 
    # vraag invoer
    # vergelijk invoer
    # onjuist? geef feedback
    
    # juist! Dan voer je de regel hieronder uit
    goedgeraden = True

# wanneer het programma uit de vorige while lus is, weten we 100% zeker dat het getal geraden is

# Einduitslag
```

Dit vertaalt zich voor **Raad het getal** naar het volgende programma:

**Het hele programma**
```python
# de regel hieronder is nodig om randint te kunnen gebruiken
from random import randint

# Startscherm
print("Welkom bij Raad-het-getal")
score = 0
doelgetal = randint(1,100)

goedgeraden = False

while not goedgeraden:
    # Invoer van de gebruiker
    invoer = int(input("Voer een getal in tussen de 1 en de 100: "))
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
```

:::{exercise} Python code Galgje

Schrijf het volledige programma op basis van je eerder gemaakte codeblokken van het spel Galgje van opdracht {ref}`storyboard_galgje`. 

Maak ook hier gebruik van de interactie lus zoals in het voorbeeld bij *Raad het getal* is gebruikt.

:::