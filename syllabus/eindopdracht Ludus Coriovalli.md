# Eindopdracht

Het spel dat jullie gaan maken is Ludus Coriovalli. Dit is een Romeins bordspel waarvan het speelbord is gevonden in het Thermenmuseum in Heerlen, in het zuiden van Nederland. De Romeinen noemden Heerlen *Coriovallum*, vandaar de naam. Het bijzondere aan dit spel is dat niemand meer wist hoe het gespeeld werd — totdat onderzoekers van de Universiteit Maastricht in 2026 met behulp van kunstmatige intelligentie de spelregels hebben gereconstrueerd. Ze lieten een AI miljoenen potjes spelen op het bord en vergeleken het slijtagepatroon van de spelstukken met het slijtagepatroon op de originele steen. Zo ontdekten ze welke regels het beste bij het spel pasten. Het is daarmee het eerste bordspel waarvan de regels door AI zijn gereconstrueerd! Wil je er meer over weten, bekijk dan de [pagina op het Ludii-portaal](https://ludii.games/details.php?keyword=Ludus%20Coriovalli).

Het spel is een zogeheten *jachtspel* (in het Engels: *hunt game*), vergelijkbaar met het Deense spel Haretavl. Eén speler speelt met de **honden** en de andere speler speelt met de **hazen**. De honden proberen de hazen in te sluiten zodat ze niet meer kunnen bewegen. De hazen proberen zo lang mogelijk vrij te blijven.

Het spel dat je maakt, is te spelen in de console. Je hoeft dus alleen `print` te gebruiken om het speelbord te tonen en `input` om gebruikers om hun input te vragen. Het zou er dus bijvoorbeeld zo uit kunnen zien:

```
        [1]
       / | \
      /  |  \
   [2]--[3]--[4]
    | \  |  / |
    |  \ | /  |
   [5]--[6]--[7]
    |  / | \  |
    | /  |  \ |
   [8]--[9]-[10]
      \  |  /
       \ | /
       [11]

Honden: 1, 2, 4
Hazen: 8, 11
```

Hoe die interactie er precies uitziet en hoe je de staat van het spel weergeeft, is aan jou. Als je niet weet hoe je moet beginnen en iemand raadt je aan om met pygame aan de slag te gaan, dan moet je dat advies niet opvolgen. Dit is de **basis** van programmeren en pygame is wel een tikkie ingewikkelder dan de basis.

## Het speelbord

Het speelbord bestaat uit 11 punten die met lijnen zijn verbonden. Stukken staan op de punten en mogen alleen bewegen langs de lijnen naar een aangrenzend punt. Het bord ziet er als volgt uit:

```
        [1]
       / | \
      /  |  \
   [2]--[3]--[4]
    | \  |  / |
    |  \ | /  |
   [5]--[6]--[7]
    |  / | \  |
    | /  |  \ |
   [8]--[9]-[10]
      \  |  /
       \ | /
       [11]
```

De verbindingen (welke punten aan elkaar grenzen) zijn:

- **1**: verbonden met 2, 3, 4
- **2**: verbonden met 1, 3, 5, 6
- **3**: verbonden met 1, 2, 4, 6
- **4**: verbonden met 1, 3, 6, 7
- **5**: verbonden met 2, 6, 8
- **6**: verbonden met 2, 3, 4, 5, 7, 8, 9, 10 *(het midden)*
- **7**: verbonden met 4, 6, 10
- **8**: verbonden met 5, 6, 9, 11
- **9**: verbonden met 6, 8, 10, 11
- **10**: verbonden met 6, 7, 9, 11
- **11**: verbonden met 8, 9, 10

## De spelregels

Voor de basisvariant gelden de volgende spelregels:

Eén speler speelt met **drie honden** en de andere speler speelt met **twee hazen**. De honden beginnen bovenaan het bord op de punten **1**, **2** en **4**. De hazen beginnen onderaan het bord op de punten **8** en **11**.

- Spelers zijn om de beurt aan zet en verplaatsen één stuk per beurt naar een aangrenzend *leeg* punt. Er wordt dus niet geslagen: stukken worden nooit van het bord verwijderd.
- De **honden** mogen alleen **naar beneden of opzij** bewegen. Ze mogen *niet* naar een punt dat hoger op het bord ligt (richting punt 1). Concreet: een hond mag nooit naar een punt met een *lager* nummer bewegen dat hoger op het bord ligt (zie de uitgebreide tabel hieronder). De honden proberen de hazen in te sluiten.
- De **hazen** mogen **alle kanten** op bewegen langs de verbindingen. De hazen proberen zo lang mogelijk vrij te blijven.
- De honden winnen als **beide hazen** niet meer kunnen bewegen (ze zijn ingesloten).
- De hazen winnen als ze de honden voorbij weten te komen, dat wil zeggen: als een haas een punt bereikt dat *boven* alle honden op het bord ligt. Concreet: een haas wint als die punt **1** bereikt, of als de hazen op het bord zo gepositioneerd zijn dat de honden ze niet meer kunnen insluiten.

Om het spel eerlijk te maken wordt er **twee keer** gespeeld: na de eerste ronde wisselen de spelers van rol. De speler die als hazen het langste heeft volgehouden (het meeste beurten), wint het spel. Als beide spelers even lang volhielden, is het gelijkspel.

:::{admonition} Bewegingsbeperking honden
:class: note

Om het simpel te houden zijn dit de toegestane richtingen per punt voor de honden:

| Hond op punt | Mag naar                    |
| ------------ | ----------------------------|
| 1            | 2, 3, 4                     |
| 2            | 3, 5, 6                     |
| 3            | 6                           |
| 4            | 3, 6, 7                     |
| 5            | 6, 8                        |
| 6            | 5, 7, 8, 9, 10              |
| 7            | 6, 10                       |
| 8            | 9, 11                       |
| 9            | 10, 11                      |
| 10           | 11                          |
| 11           | *(kan nergens heen)*        |

De hazen mogen langs elke verbinding in beide richtingen bewegen.
:::

Verder moet je programma aan de volgende eisen voldoen:

- Het spel start met een begroeting en een korte uitleg van het spel.
- Je vraagt de namen van de twee spelers en gebruikt tijdens de rest van het spel die namen. Twee spelers mogen niet dezelfde naam invoeren.
- Je programma kiest willekeurig welke speler in de eerste ronde met de honden begint.
- Per beurt laat je programma duidelijk het bord zien, inclusief waar de honden en hazen staan.
- De speler kiest welk stuk hij/zij wil verplaatsen en naar welk punt. Bij een foutieve invoer (bijvoorbeeld geen geldig punt, een punt dat niet aangrenzend is, een punt dat bezet is, of een hond die de verkeerde kant op beweegt) wordt de speler daarop gewezen en mag opnieuw iets invoeren.
- Het spel detecteert automatisch wanneer de honden gewonnen hebben (hazen kunnen niet meer bewegen) of wanneer de hazen gewonnen hebben (een haas is voorbij de honden gekomen).
- Na de eerste ronde wisselen de spelers van rol en wordt er opnieuw gespeeld. Na twee rondes wordt de winnaar bekendgemaakt.
- Na afloop vraagt je programma of de spelers nog een keer willen spelen of willen stoppen.

De basisvariant is 2 sterren waard, waarmee je *maximaal* een 7 kunt halen als je verder alle punten haalt (zie verderop in deze opdracht). Als je een hoger cijfer wilt, kun je meer dingen aan het spel toevoegen voor meer sterren. Met 5 sterren kun je een 10 halen. Hieronder vind je een aantal mogelijke uitbreidingen:

### Plaatsingsfase (0.5 sterren)

In de basisvariant staan de stukken op vaste startposities. In deze uitbreiding beginnen de spelers met een lege bord en plaatsen de stukken om de beurt op het bord. Eerst plaatst de hondenspeler al zijn drie honden (één per beurt), daarna plaatst de hazenspeler zijn twee hazen (één per beurt). De honden mogen alleen op de bovenste helft van het bord geplaatst worden (punten 1 t/m 7) en de hazen alleen op de onderste helft (punten 5 t/m 11). Punt 5, 6 en 7 mogen dus door beide spelers gekozen worden. Daarna gaat het spel verder als normaal.

Bij een ongeldige plaatsing (bezet punt, verkeerde helft) vraagt je programma opnieuw wat de speler wil.

Zet in het commentaar bovenaan je programma:

```python
# Uitbreidingen:
# - Plaatsingsfase
```

### Vier honden (0.5 sterren)

In deze uitbreiding speelt de hondenspeler met **vier** honden in plaats van drie. De vierde hond begint op punt **3** (in de basisvariant) of wordt als vierde geplaatst (als je ook de plaatsingsfase hebt). Het bord wordt hierdoor wat krapper voor de hazen, maar door het grotere aantal stukken is het ook uitdagender om te programmeren.

Zet in het commentaar bovenaan je programma:

```python
# Uitbreidingen:
# - Vier honden
```

### Score bijhouden (0.5 sterren)

Meestal laat je het niet bij één potje en wil je er meer spelen. Met deze uitbreiding houdt je spel de score per persoon bij over meerdere rondes. Na afloop van elke volledige ronde (twee keer spelen met rolwisseling) zet je de score op het scherm en vraag je of de spelers nog een ronde willen spelen. Wanneer de spelers klaar zijn met spelen, roep je de speler met de meeste gewonnen rondes uit tot winnaar.

Bijvoorbeeld:
```
Henk: 3
Truus: 2
====
Henk heeft gewonnen!
```

Zet in het commentaar bovenaan je programma:

```python
# Uitbreidingen:
# - Score bijhouden
```

### Slimme hond (0.5 tot 1 sterren)

In deze variant laat je de gebruiker kiezen of ze met twee spelers willen spelen, of tegen de computer. De computer speelt dan als de honden en probeert de hazen zo slim mogelijk in te sluiten. Bedenk een strategie waarbij de honden samenwerken om de hazen klem te zetten. Hoe slimmer je computerspeler, hoe meer punten je krijgt (0.5 voor een eenvoudige strategie, 1 ster voor een sterke strategie).

Zet in het commentaar bovenaan je programma:

```python
# Uitbreidingen:
# - Slimme hond
```

### De tijd loopt! (0.5 sterren)

Net zoals bij schaken kun je afspreken dat je een beperkte speeltijd hebt. Met deze uitbreiding programmeer je per speler een timer. Je vraagt of de spelers met of zonder timer willen spelen. Als ze met timer willen spelen, vraag je hoeveel seconden een speler in totaal heeft (tussen de 10 en 120 seconden). Wanneer een speler aan de beurt is, loopt de tijd voor die speler af. Je hoeft de tijd niet actief op het scherm te laten zien. Wanneer een speler een zet heeft gedaan, laat je de resterende tijd van die speler zien. Wanneer een speler geen tijd meer over heeft, verliest deze automatisch de ronde. Voor deze functionaliteit kun je de Python-bibliotheek `time` gebruiken.

Zet in het commentaar bovenaan je programma:

```python
# Uitbreidingen:
# - De tijd loopt!
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

### Samenwerken
Soms is het fijn om samen te werken voor een eindopdracht. Voor de meeste eindopdrachten bij Informatica Q-Highschool is dit wel mogelijk. Voor de module Basis van Programmeren met Python is samenwerken **niet** toegestaan. We willen namelijk weten wat _jij_ kan. Daarom hebben we besloten dat je voor deze module de eindopdracht alleen maakt (dus ook niet met intensieve hulp van een broer/zus/vriend/kennis die wel goed kan programmeren).

### In gesprek

Omdat we graag willen weten hoe je tot jouw uitwerking van de eindopdracht bent gekomen, selecteren we ongeveer de helft van de uitwerkingen en vragen deze leerlingen op gesprek. Als we je niet in de les hebben gezien of we hebben het idee dat je je code niet zelf hebt geschreven, dan kun je natuurlijk sowieso rekenen op een uitnodiging. Als je hiervoor wordt gekozen, dan wordt je eindcijfer na afloop van dit gesprek bepaald. Wil je zelf graag iets uitleggen over je code? Geef dan bij je docent aan dat je ook graag een beoordelingsgesprek wilt hebben.

Tijdens zo'n gesprek krijg je eerst de kans om je programma te demonstreren en vervolgens zal de docent aan de hand van je ingeleverde code je enkele vragen stellen. Je mag uitleggen wat bepaalde stukken code doen, hoe je ze geschreven hebt en welke keuzes je daarbij gemaakt hebt.

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

Het is uitdrukkelijk niet de bedoeling dat je grote blokken code of het hele spel kopieert. In dat geval zien we het als plagiaat en zullen we daar ook naar handelen. Voor diegenen die dit ingewikkeld vinden: meer dan 5 regels is een groot blok.

## Tips voor een goeie eindopdracht

- Volg het stappenplan van {ref}`programma_schrijven`.
- Begin met het bord en de verbindingen. Sla deze op in een dictionary of een lijst van lijsten.
- Test eerst of de bewegingen werken voordat je de spellogica toevoegt.
- Speel je spel zelf!
- Nog beter: laat het testen door anderen!
- Probeer je eigen spel te breken door opzettelijk foute invoer te geven.
