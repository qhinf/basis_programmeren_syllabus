# Eindopdracht

Het spel dat jullie gaan maken is speciale editie van Ganzenbord. Hieronder staan een aantal variaties, oplopend in moeilijkheidsgraad om je op weg te helpen. Begin met het maken van de basisvariant, alle andere opties kun je daar dan aan toevoegen voor extra punten.

Het spel dat je maakt, is te spelen in de console. Je hoeft dus alleen `print` te gebruiken om het speelbord te tonen en `input` om gebruikers om hun input te vragen. Hoe die interactie er precies uitziet en hoe je de staat van het bord weergeeft, is aan jou. Als je niet weet hoe je moet beginnen en iemand raadt je aan om met pygame aan de slag te gaan, dan moet je dat advies niet opvolgen. Dit is de **basis** van programmeren en pygame is wel een tikkie ingewikkelder dan de basis.

## De spelregels

Voor de basisvariant gelden de volgende spelregels:

- Ganzenbord heeft een bord met 63 vakjes. Wie het eerst op het 63ste vakje eindigt, wint.
- Je speelt met twee spelers, die om en om aan de beurt komen.
- Als een speler aan de beurt is, moet die de dobbelsteen rollen voor het aantal stappen dat gezet wordt op het bord. Om te rollen moet de speler een expliciet commando geven (bijvoorbeeld "rol" of "r"). Een speler mag ook kiezen om op te geven. Dan stopt het spel en wint de andere speler. Als spelers iets anders invoeren dan rollen of opgeven, dan geeft je programma aan dat de input niet klopt en vraagt de speler opnieuw om een commando.
- De spelers moeten precies op 63 uitkomen om te winnen: als je hoger gooit dan nodig is om 63 te bereiken worden de volgende stappen teruggeteld. Voorbeeldje: je staat op 62 en gooit 3. Je maakt dus 3 stappen: naar 63, terug naar 62 en dan naar 61.
- Wat is jouw geluksgetal? Spelers die op dat vak terecht komen, mogen nogmaals het aantal stappen dat ze gerold hebben zetten. Voorbeeldje: een speler staat op 11, rolt 3 en komt dus op 14. Dat is jouw geluksgetal, dus mag de speler nogmaals 3 stappen zetten naar 17.
- Het spel is afgelopen als een speler gewonnen heeft. Je programma print welke speler het spel gewonnen heeft en vraagt vervolgens of de gebruiker nog een keer wil spelen of dat het programma moet sluiten. Als de gebruiker nog een keer wil spelen, start het spel opnieuw en als de gebruiker wil stoppen, dan sluit het programma (uiteraard).

De basisvariant is 2 sterren waard, waarmee je maximaal een 6 kunt halen als je verder alle punten haalt (zie verderop in deze opdracht). Als je een hoger cijfer wilt, kun je meer dingen aan het spel toevoegen voor meer sterren. Met 5 sterren kun je een 10 halen. Hieronder een aantal klassieke en minder klassieke uitbreidingen voor Ganzenbord:

### In de put (0.5 sterren)

Wat is jouw ongeluksgetal? Spelers die op dat vak terecht komen, komen in de put terecht. Ze blijven daar net zo lang zitten tot een medespeler ook in de put terecht komt. Die geeft de eerste speler dan een zetje om uit de put te komen en blijft zelf in de put zitten. Voorbeeld:

- De put zit op vakje 31.
- Purk staat op 26, rolt een 5, komt op het vakje van de put terecht en zit dus in de put. De beurt gaat naar de volgende speler.
- Wanneer de beurt normaal gesproken aan Purk zou zijn, wordt Purk overgeslagen, want die zit in de put.
- Op een gegeven moment staat Tommie op 30, rolt een 1 en komt dus in de put. Op dat moment wordt Purk uit de put geholpen en blijft Tommie in de put zitten. Purk komt op vakje 32 te staan. De eerstvolgende keer dat Purk in de normale volgorde aan de beurt is, mag Purk weer gewoon verder spelen.

Om verwarring te voorkomen (of om het nog een beetje in te wrijven) print je programma "Speler *x* wordt overgeslagen, want die zit in de put." op het moment dat dat die speler eigenlijk aan de beurt zou zijn.

Zet in het commentaar bovenaan je programma:

```python
# Uitbreidingen:
# - In de put op vakje ...
```

### De doornstruik (0.5 sterren)

Kies een vakje uit waar de tuinman al te lang niet is geweest en waar nu een grote doornstruik groeit. Als een speler op dat vakje terecht komt, wordt die teruggeplaatst naar een eerder vakje op het bord. Voorbeeld:

- Bert staat op vakje 40, op 42 staat de doornstruik en Bert rolt 2. Bert gaat terug naar vakje 37.

Zet in het commentaar bovenaan je programma:

```python
# Uitbreidingen:
# - De doornstruik op vakje ... (gaat terug naar ...)
```

### Double trouble (0.5 sterren)

Vanaf nu spelen we niet met één, maar met twee dobbelstenen. Er is wel een *maar*: als een speler dubbele ogen gooit (dus bijvoorbeeld 5 met beide dobbelstenen), dan is die speler gediskwalificeerd en mag die niet meer meespelen. Als alle spelers gediskwalificeerd zijn, stopt het spel.

Zet in het commentaar bovenaan je programma:

```python
# Uitbreidingen:
# - Double trouble
```

### Meer vreugd (1 ster)

Ganzenbord kun je prima met meer dan 2 spelers spelen. Breidt je programma uit zodat het aan het begin vraagt hoeveel spelers er zijn en wat hun namen zijn. Gebruik de ingevoerde namen om aan te geven wie er aan de beurt is. Je programma moet in theorie (op een computer met oneindig geheugen) met een oneindig aantal spelers te spelen zijn, dus daar mag geen limiet op zitten. Als een speler opgeeft, spelen de andere spelers gewoon door tot er nog maar één speler over is. Als alle spelers behalve één opgeven, dan heeft die speler gewonnen.

Zet in het commentaar bovenaan je programma:

```python
# Uitbreidingen:
# - Meer vreugd
```

### Marathon (1 ster)

Altijd maar weer hetzelfde spel is ook saai, dus vraagt je programma aan het begin hoe lang het Ganzenbord moet zijn, oftewel hoeveel vakjes het heeft. Om ervoor te zorgen dat niet alle "leuke" vakjes aan het begin zitten of buiten het bord vallen, moet je voor je geluksgetal (en eventueel voor de put en de doornstruik) aan het begin een willekeurig getal kiezen. Uiteraard laat je dan ook de spelers weten op welk vakje elk element terecht is gekomen.

Het minimum aantal vakjes is 10. Als de gebruiker een getal lager dan 10 invoert, dan geeft je programma aan dat dat niet correct is en laat de gebruiker een nieuw getal kiezen.

Zet in het commentaar bovenaan je programma:

```python
# Uitbreidingen:
# - Marathon
```

## Beoordeling

Je programma wordt beoordeeld op drie aspecten: de correctheid, de uitgebreidheid en de kwaliteit. Voor de correctheid kijken we naar twee aspecten:

- Syntactisch correct, dus geen foutmeldingen van Python bij het uitvoeren van je programma.
- Logisch correct, dus je programma werkt volgens de spelregels.

Voor beide onderdelen kun je 10 punten krijgen.

Voor de uitgebreidheid kijken we naar de hoeveelheid sterren die je in je programma geïmplementeerd hebt. Als je de basis of verschillende uitbreidingen niet volledig geïmplementeerd hebt, kunnen we ook een deel van de sterren toekennen. Het aantal punten voor logisch correct wordt geschaald met het aantal sterren.

Wat betreft de kwaliteit kijken we naar drie aspecten:

- Gebruik van de verschillende elementen in Python (if, for, while etc). Hierbij kijken we niet alleen of je de verschillende onderdelen onder de knie hebt, maar ook of je de beste oplossing voor een probleem hebt gekozen.
- Goede, duidelijke, beschrijvende variabelenamen.
- Zinvol en informatief commentaar waarin je je programma uitlegt.

Ook hier kun je voor elk aspect 10 punten krijgen.

Je krijgt 10 punten gratis, waarmee je cijfer uitkomt op het aantal punten gedeeld door 10.

### Code kopiëren?

Je mag externe bronnen gebruiken als hulp bij het maken van je spel, want daar kun je veel van leren. Je mag ook stukjes code overnemen, maar die moet je wel uitgebreid van commentaar voorzien om uit te leggen wat die code doet (minstens 1 regel commentaar per regel code!) en in commentaar de bron vermelden. De bron vermelden betekent dat je een link naar de exacte bron toevoegt, dus "uit een video op YouTube" is geen bronvermelding, een link naar de code is minimaal wat we verwachten. Indien de code via persoonlijke communicatie gedeeld, vermeld dan minstens de naam van de persoon en jouw relatie tot die persoon. Gebruik `# BRON:` om duidelijk aan te geven dat dit een bronvermelding is en zodat wij het makkelijk terug kunnen vinden.

Ook code uit ChatGPT en dergelijke dien je van een bronvermelding te voorzien.

Het is uitdrukkelijk niet de bedoeling dat je grote blokken code of het hele spel kopieert. In dat geval zien we het als plagiaat en zullen we daar ook naar handelen. Voor diegenen die dit ingewikkeld vinden: meer dan 4 regels is een groot blok.
