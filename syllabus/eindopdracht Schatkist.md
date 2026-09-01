# Eindopdracht

Op een zonnig, winderig strand ligt hij te wachten: een oude, krakkemikkige schatkist. Zijn hout is verweerd, zijn scharnieren kraken bij elke windvlaag, en op het deksel zijn nog net wat vervaagde letters te lezen: “Eigendom van Kapitein Chaos. Niet openen.”

Maar dit is geen gewone schatkist. Nee, deze kist kan praten. En niet zomaar praten — hij kan zeuren, mopperen en grapjes maken waar zelfs je oom op een verjaardag zich voor zou schamen.

“Ah, daar ben je eindelijk!” klinkt een krakerige stem. “Ik ben De Kist des Geheimen. Vier cijfers. Dat is alles wat je hoeft te vinden. Maar pas op: ik geef je alleen een paar cryptische hints. En nee, ik verklap nooit de code, hoe zielig je ook kijkt. Ik ben tenslotte een kist met principes.”

En zo begint jouw avontuur. Jij bent de codekraker. Jij gaat het opnemen tegen een kist die denkt dat hij slimmer is dan iedereen. Elke poging die je doet, wordt beantwoord met een mengeling van sarcasme en hints: hoeveel cijfers op de juiste plek zitten (*Goud*) en hoeveel cijfers wel in de code zitten maar op de verkeerde plek (*Zilver*).

Lukt het jou om de kist te slim af te zijn? Of blijft hij lachen terwijl jij je suf raadt?

We hebben even meegeluisterd met de schatkist en dit is wat we hoorden:

```
Schatkist:  Hé jij daar! Ja, jij met die nieuwsgierige blik. 
            Jij denkt zeker dat je mijn schat zomaar kunt pakken?
            Ha! Je moet eerst mijn ultrageheime-superdeluxe-code kraken.
            Vier cijfers. Succes… je zult het nodig hebben.

Speler:        3709

Schatkist:  Oei, oei, oei… Goud: 1, Zilver: 0.
            Niet slecht, maar je bent er nog lang niet. 
            Misschien moet je een andere bril opzetten? 

Speler:        4768

Schatkist:  Nou ja zeg, Goud: 2, Zilver: 1.
            Je komt gevaarlijk dichtbij. Ik begin al te zweten, hoor!

Speler:        4756

Schatkist:  WAT?! Hoe kan dit? 
            Goud: 4, Zilver: 0. 
            Neeeeee… Mijn prachtige schatten… weg!
            Nou ja, gefeliciteerd dan maar, slimmerik.
            Je score is 3.
```

## Opdracht basisvariant

Schrijf een programma in Python, waarmee dit spel door één speler gespeeld kan worden. Je programma dient:

1. Een welkomstboodschap af te drukken
2. De rol van Schatkist aan te nemen
3. Naar de code te vragen
4. Aan te geven met *Goud* en *Zilver* hoeveel cijfers er op de goede plek staan en hoeveel cijfers er goed zijn
5. Tegen foutieve invoer te kunnen
6. De score bij te houden: de eindscore is het aantal keren dat een speler nodig heeft gehad om de juiste code te raden
7. Wanneer de code juist is geraden, de score af te drukken
8. Na afloop de speler de keuze geven om het spel nog een keer te spelen of om het programma af te sluiten

**In de basisvariant hoef je dus *niet* het hele theater van de schatkist te programmeren.**

Neem in je programma de volgende code op:

Helemaal bovenaan:
```python
import random
```

en daar ergens onder:
```python
def genereer_code():
    code = ''.join(random.choices('0123456789', k=4))
    return code
```

Je kunt nu een willekeurige code in je programma maken door `geheimeCode = genereer_code()` aan te plaatsen. Let op dat `geheimeCode` een `string` is en geen `int`.

Het spel dat je maakt, is te spelen in de console. Je hoeft dus alleen `print()` te gebruiken om het speelbord te tonen en `input()` om gebruikers om hun invoer te vragen.
Hoe die interactie er precies uitziet en hoe je de staat van het spel weergeeft, is aan jou. Als je niet weet hoe je moet beginnen en iemand raadt je aan om met `pygame` aan de slag te gaan, dan moet je dat advies niet opvolgen. Dit is de basis van programmeren en `pygame` is wel een tikkie ingewikkelder dan de basis.

Deze basisvariant is 2 sterren waard, waarmee je *maximaal* een 7 kunt halen als je verder alle punten haalt (zie verderop in deze opdracht). Als je een hoger cijfer wilt, kun je meer dingen aan het spel toevoegen voor meer sterren. Met 5 sterren kun je een 10 halen.

## Uitbreidingen

Wanneer je een uitbreiding wil programmeren, wordt deze alleen beoordeeld, wanneer je bovenaan in je code (nog boven `import random`) hebt staan:

```python
# Uitbreidingen:
# - <naam van de uitbreiding>
```

`<naam van de uitbreiding>` vervang je natuurlijk de door naam of namen van de uitbreidingen die je hebt geprogrammeerd.

### Moeilijkheidsgraad (1 ster)
Aan het begin van het spel vraag je aan de speler met welke moeilijkheidsgraad het spel gespeeld gaat worden. De moeilijkheidsgraad kun je variëren door te gebruiker te laten kiezen in het aantal cijfers in de code. Het maximum aantal cijfers is 8.
 
### Schatkist drama (0,5 ster)
In het voorbeeldgesprek met de schatkist heb je gezien dat deze nog wel van een beetje drama houdt. In deze uitbreiding ga je de reactie van de schatkist wat veelzijdiger maken.

1. Wanneer de speler dicht in de buurt van het antwoord komt (dus een hoge goud of zilver score heeft), laat je de schatkist meer 'zweten'. Dus je laat de schatkist antwoorden geven, die aangeven dat de speler dichtbij de juiste code zit.
2. Wanneer de speler verder weg van een juiste score gaat (dus het aantal goud of zilver daalt), dan laat je de schatkist een beetje jennen en plagen. 

### Highscore bijhouden (2 sterren)
Het is niet alleen tof om de score bij te houden, maar ook om de laagste score ooit bij te houden. Gebruik een tekstbestand `score.txt` om de beste score in op te slaan (inclusief de naam van de speler). Wanneer er een speler is, die een nieuwe beste score heeft, dan 
1. Geef je de score weer
2. Feliciteer je de speler
3. Vraag je de naam van de speler en sla je die naam en score op in het bestand

Dit bestand lees en schrijf je in je Python code middels `write()` en `readline()`. Het bestand `score.txt` bevat precies twee regels. Op de eerste regel staat de naam van de speler met de hoogste score en op de tweede regel staat de score.

Een voorbeeld van een `score.txt`:
```
Henk
4
```

Let op: wanneer je deze uitbreiding combineert met de uitbreiding **Moeilijkheidsgraad** dan zul je ook de moeilijkheidsgraad op moeten slaan.

### De tijd loopt (1 ster)
Met deze uitbreiding programmeer je een tijdsduur, waarbinnen de speler de code moet kraken. Bij deze uitbreiding is het dus mogelijk dat de speler 'af' gaat. Je vraagt of de speler dit spel met of zonder timer willen spelen. Als die met timer willen spelen, vraag je hoeveel seconden een speler in totaal heeft (tussen de 10 en 100 seconden). De tijd begint zodra de eerste code gevraagd wordt. Je hoeft de tijd niet actief op het scherm te laten zien. Wanneer een speler een code heeft ingevoerd, laat je de resterende tijd zien. Het spel is dus verloren, wanneer de speler te laat antwoord geeft. Voor deze functionaliteit kun je de Python-bibliotheek `time` gebruiken. 

### De rollen omgedraaid (3 sterren)
Deze uitbreiding is de meest complexe. Je gaat hier de rollen omdraaien. Je gaat een apart deel programmeren. Dit deel komt dus als uitbreiding op de basisvariant. Je vraagt aan het begin van het spel of de speler de code wil raden of het goud en zilver wil uitdelen.

Wanneer de speler in de rol van de Schatkist duikt, zal de speler dus moeten antwoorden in goud en zilver. Je moet uitprogrammeren hoe de computer tot het raden van de juiste code kan komen op basis van de antwoorden goud en zilver.

## Inleveren

Je levert je programma in als een .py-bestand via je portfolio op [app.q-vakken.nl](https://app.q-vakken.nl). Als je je programma in Thonny of VSCode hebt geschreven, dan kun je dat bestand terugvinden op je computer in de map waar je het hebt opgeslagen. Andere soorten bestanden, zoals code in een Word-document, kunnen we niet uitvoeren en worden dus niet beoordeeld. 

Als je je programma over meerdere Python-bestanden hebt verdeeld, maak dan een .zip-bestand met daarin alle code en lever dat .zip-bestand in. Zie [deze pagina](https://informatica.q-vakken.nl/informatie/meerdere-bestanden-inleveren) als je daar hulp bij nodig hebt.

## Beoordeling

Je programma wordt beoordeeld op drie dingen: of het goed werkt, hoeveel functionaliteit je hebt geïmplementeerd en de kwaliteit van de code die je hebt geschreven:

| Onderdeel                                                    | Punten                    |
| ------------------------------------------------------------ | ------------------------- |
| Syntactisch correct, dus geen foutmeldingen van Python bij het uitvoeren van je programma | 0 tot 10                  |
| Logisch correct, dus je programma werkt volgens de spelregels | 0 tot 10 × aantal sterren |
| Gebruik van de verschillende en juiste elementen in Python (if, for, while etc.) | 0 tot 10                  |
| Goede, duidelijke, beschrijvende variabelenamen              | 0 tot 10                  |
| Zinvol en informatief commentaar waarin je je programma uitlegt | 0 tot 10                  |

Let op: bij het aantal punten dat je voor logisch correct kunt krijgen, telt dus ook mee hoeveel sterren je in je project verwerkt hebt. Heb je het minimale spel gemaakt, dan krijg je daar maximaal 2 sterren × 10 punten = 20 punten voor. Per uitbreiding staat vermeld hoeveel sterren er te verdienen zijn. Het maximale cijfer voor je eindopdracht is een 10, ook al heb je meer dan 5 sterren

Bij het gebruik van de verschillende elementen van Python (if, for, while etc.) kijken we niet alleen of je de verschillende onderdelen onder de knie hebt, maar ook of je de beste oplossing voor een probleem hebt gekozen.

De eerste 10 punten krijg je gratis, dus kun je maximaal 100 punten verdienen. Je eindcijfer is het aantal punten gedeeld door 10.

### Samenwerken
Soms is het fijn om samen te werken voor een eindopdracht. Voor de meeste eindopdrachten bij Q-vak Informatica is dit wel mogelijk. Voor de module Basis van Programmeren met Python is samenwerken **niet** toegestaan. We willen namelijk weten wat _jij_ kan. Daarom hebben we besloten dat je voor deze module de eindopdracht alleen maakt (dus ook niet met intensieve hulp van een broer/zus/vriend/kennis die wel goed kan programmeren).

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

Het is uitdrukkelijk niet de bedoeling dat je grote blokken code of het hele spel kopieert. In dat geval zien we het als plagiaat en zullen we daar ook naar handelen. Voor diegenen die dit ingewikkeld vinden: meer dan 5 regels code is een groot blok.

## Tips voor een goeie eindopdracht

Je leest deze opdracht helemaal tot het einde!? Dan hier een paar tips om een goede eindopdracht te maken:

- Volg het stappenplan van {ref}`programma_schrijven`.
- Speel je spel zelf!
- Nog beter: laat het testen door anderen!
- Probeer je eigen spel te breken door opzettelijk foute invoer te geven
