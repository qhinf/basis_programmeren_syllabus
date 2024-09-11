# Eindopdracht

Iedereen kent het spelletje Boter, Kaas en Eieren. Je tekent snel een paar lijntjes in de vorm van een hashtag op papier en zet om de beurt een `O` of een `X` in de vakjes. De speler, die als eerste drie van zijn tekentjes op een rij heeft, heeft gewonnen. Wanneer je weet hoe het moet, kun je met dit eenvoudige spelletjes nooit meer verliezen.

Voor deze opdracht ga je een Boter, Kaas en Eieren met andere spelregels programmeren. 

**De Italiaanse variant.** 

*Fase 1*

De start van het spel is hetzelfde als bij traditioneel Boter, Kaas en Eieren. Elke speler mag *om de beurt* zijn eerste **drie** stenen zetten. Het kan natuurlijk zijn dat in deze fase een speler slim genoeg is geweest om drie stenen op een rij te leggen. Dan is het spel afgelopen. Als dat niet het geval is, ga je door naar volgende fase.

*Fase 2*

Na deze fase wordt het anders dan je gewend bent. Er staan nu dus 6 stenen op het bord en zijn er nog 3 plekken vrij op het bord. De tweede fase van het spel is dat je met de stenen gaat *schuiven*. Een soort dammen. Het schuiven is ook aan regels gebonden:
1. Je mag een steen alleen naar een onbezette plaats schuiven,
2. Je mag altijd van en naar het midden schuiven,
3. Stenen aan de rand mogen alleen één plek verder of één plek terug over de rand.
Om een voorbeeld te geven: een `X` of een `O` op positie `2` mag naar positie `1`, `3` en `5` bewegen. Mits deze plek natuurlijk vrij is.

```
*1*| X |*3*
---+---+---
 4 |*5*| 6 
---+---+---
 7 | 8 | 9 
```

*Einde van het spel*

Dit schuiven gaat door, totdat één van de spelers drie stenen op een rij heeft. Deze speler heeft gewonnen.

*Jouw spel*

Het spel dat je maakt, is te spelen in de console. Je hoeft dus alleen `print` te gebruiken om het speelbord te 
tonen en `input` om gebruikers om hun input te vragen. Hoe die interactie er precies uitziet en hoe je de staat van het bord weergeeft, is aan jou. Als je niet weet hoe je moet beginnen en iemand raadt je aan om met pygame aan de slag te gaan, dan moet je dat advies niet opvolgen. Dit is de **basis** van programmeren en pygame is wel een tikkie ingewikkelder dan de basis.

Begin met het maken van de basisvariant, alle andere opties kun je daar dan aan toevoegen voor extra punten.

## Opdracht basisvariant
Schrijf een programma in Python, waarmee dit spel door twee spelers gespeeld kan worden. Je programma dient:
1.	Een welkomstboodschap af te drukken.
2.	Te vragen naar de namen van de spelers.
3.	Fase 1 te doorlopen (het plaatsen van de eerste 2x 3 stenen).
4.	In fase 2 de speler de mogelijke posities, waar naartoe geschoven kan worden, te geven.
5.	De speler (vriendelijk) te wijzen op foutieve invoer.
6.	De speler (vriendelijk) te wijzen op een ongeldige zet.
7.	De winnaar bekend te maken.
8.	Na afloop van het spel de keuze geven om nog een ronde te spelen.

Deze basisvariant is 2 sterren waard, waarmee je *maximaal* een 7 kunt halen als je verder alle punten haalt (zie verderop in deze opdracht). Als je een hoger cijfer wilt, kun je meer dingen aan het spel toevoegen voor meer sterren. Met 5 sterren kun je een 10 halen. Hieronder de uitbreidingen voor jouw versie van Italiaans Boter, Kaas en Eieren.

## Uitbreidingen

### Score bijhouden (1 ster)

Meestal laat je het niet bij 1x zo'n spelletje spelen en wil je er meer spelen. Dan is het fijn om de score bij te houden. Met deze uitbreiding houdt je spel de score per persoon bij. Na afloop van elke ronde, zet je de score op het scherm *en* vraag je of de spelers nog een ronde willen spelen. Wanneer de spelers klaar zijn met het spel, roep je de speler met het meeste aantal gewonnen spelen uit tot winnaar.

Bijvoorbeeld:
```
Henk: 4
Truus: 5
====
Truus heeft gewonnen
```

Zet boven in je code het volgende fragment:

```python
# Uitbreidingen:
# - Score bijhouden ...
```

### Highscore bijhouden (1 ster) samen met Score bijhouden

Het is niet alleen tof om de score bij te houden, maar ook om de hoogste score ooit bij te houden. Gebruik een tekstbestand `score.txt` om de hoogste score in op te slaan (inclusief de naam van de speler). Wanneer er een speler is, die een nieuwe hoogste score heeft, dan sla je die naam en score op in het bestand. Dit bestand lees en schrijf je in je Python code middels `write()` en `readline()`. Het bestand `score.txt` bevat precies twee regels. Op de eerste regel staat de naam van de speler met de hoogste score en op de tweede regel staat de score.

Een voorbeeld van een `score.txt`:
```
Henk
4
```
```python
# Uitbreidingen:
# - Score bijhouden
# - Highscore bijhouden
```

### Schuif het bord (1 ster)

Je maakt een uitbreiding, waarbij elke speler per ronde 1x een schuifkaart in mag zetten. Een schuifkaart verschuift het bord. Een verschuiving kan naar links, naar rechts, naar boven of naar onder plaats vinden (`L, R, B, O`). Een verschuiving naar links ziet er als volgt uit:

De stenen op het bord 
```
 1 | 2 | 3  
---+---+--- 
 4 | 5 | 6  
---+---+--- 
 7 | 8 | 9  
```

worden met een links verschuiving dan als volgt verplaatst:

```
 2 | 3 | 1
---+---+---  
 5 | 6 | 4
---+---+--- 
 8 | 9 | 7
```

**Regels voor de schuifkaart**
Per ronde mag een speler maar 1x een schuifkaart inzetten. Een schuifkaart kan alleen in fase 2 ingezet worden. 

Wanneer een schuifkaart gespeeld wordt:
- vraag je de speler of deze naar links, rechts, boven of onder wil schuiven (`L, R, B, O`),
- mag de speler geen stenen meer schuiven in die beurt. Een schuifkaart komt dus in plaats van het verschuiven van een steen.

Zet boven in je code het volgende fragment:

```python
# Uitbreidingen:
# - Schuif het bord ...
```

### De tijd loopt! (1 ster)

Net zoals bij schaken, kun je afspreken dat je een beperkte speeltijd hebt. Met deze uitbreiding programmeer je per speler per rond een timer. Je vraagt of de spelers dit spel met of zonder timer willen spelen. Als ze met timer willen spelen, vraag je hoeveel seconden een speler in totaal heeft (tussen de 10 en 100 seconden). Wanneer een speler aan de beurt is, loopt de tijd voor die speler af. Je hoeft de tijd niet actief op het scherm te laten zien. Wanneer een speler een zet heeft gedaan, laat je de resterende tijd van die speler zien. Wanneer een speler als eerste geen tijd meer over heeft, verliest deze automatisch de ronde. Voor deze functionaliteit kun je de Python-bibliotheek `time` gebruiken. 

Zet boven in je code het volgende fragment:

```python
# Uitbreidingen:
# - De tijd loopt! ...
```

## Beoordeling

Je programma wordt beoordeeld op drie dingen: of het goed werkt, hoeveel functionaliteit je hebt geïmplementeerd en de kwaliteit van de code die je hebt geschreven:

| Onderdeel                                                    | Punten                    |
| ------------------------------------------------------------ | ------------------------- |
| Syntactisch correct, dus geen foutmeldingen van Python bij het uitvoeren van je programma | 0 tot 10                  |
| Logisch correct, dus je programma werkt volgens de spelregels | 0 tot 10 × aantal sterren |
| Gebruik van de verschillende en juiste elementen in Python (if, for, while etc.) | 0 tot 10                  |
| Goede, duidelijke, beschrijvende variabelenamen              | 0 tot 10                  |
| Zinvol en informatief commentaar waarin je je programma uitlegt | 0 tot 10                  |

Let op: bij het aantal punten dat je voor logisch correct kunt krijgen, telt dus ook mee hoeveel sterren je in je project verwerkt hebt. Heb je het minimale spel gemaakt, dan krijg je daar maximaal 2 sterren × 10 punten = 20 punten voor. Heb je alle uitbreidingen gemaakt, dan kun je tot 5 sterren × 10 punten = 50 punten krijgen voor dat onderdeel.

Bij het gebruik van de verschillende elementen van Python (if, for, while etc.) kijken we niet alleen of je de verschillende onderdelen onder de knie hebt, maar ook of je de beste oplossing voor een probleem hebt gekozen.

De eerste 10 punten krijg je gratis, dus kun je maximaal 100 punten verdienen. Je eindcijfer is het aantal punten gedeeld door 10.

### Code kopiëren?

Je mag externe bronnen gebruiken als hulp bij het maken van je spel, want daar kun je veel van leren. Je mag ook stukjes code overnemen, maar die moet je wel uitgebreid van commentaar voorzien om uit te leggen wat die code doet (minstens 1 regel commentaar per regel code!) en in commentaar de bron vermelden. De bron vermelden betekent dat je een link naar de exacte bron toevoegt, dus "uit een video op YouTube" is geen bronvermelding! Een link naar de code is minimaal wat we verwachten. Indien de code via persoonlijke communicatie gedeeld, vermeld dan minstens de naam van de persoon en jouw relatie tot die persoon. Gebruik `# BRON:` om duidelijk aan te geven dat dit een bronvermelding is en zodat wij het makkelijk terug kunnen vinden. Bijvoorbeeld:

```python
# BRON: https://rosettacode.org/wiki/Reverse_words_in_a_string#Python
# Draai de volgorde van woorden in elke regel van de variabele tekst om, 
# dus deze twee regels worden dan:
# om, tekst variabele de van regel elke in woorden van volgorde de Draai
# dan: worden regels twee deze dus
# Eerst wordt de tekst per regel gesplitst, en loopen we over elke regel
for line in text.split("\n"):
    # Elke regel splitsen we dan bij elke spatie (dat is standaard met split)
    # en met [::-1] word dan die lijst van woorden omgedraaid. " ".join plakt
    # de woorden weer aan elkaar met spaties ertussen en dat wordt geprint.
    print(" ".join(line.split()[::-1]))
```

Ook code uit ChatGPT en andere chatbots dien je van een bronvermelding te voorzien. Zet dan ook de prompt die je hebt gebruikt in je commentaar.

Het is uitdrukkelijk niet de bedoeling dat je grote blokken code of het hele spel kopieert. In dat geval zien we het als plagiaat en zullen we daar ook naar handelen. Voor diegenen die dit ingewikkeld vinden: meer dan 5 regels code is een groot blok.
