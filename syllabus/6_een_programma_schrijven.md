# Een programma schrijven

Wanneer je klaar bent met de oefeningen van de vorige lessen, dan ben je al een beetje bekend met de basiselementen van de taal Python. Als het goed is, ben je in staat om bijvoorbeeld 5 regels Python-code te schrijven, die doen wat jij wil dat het moet doen. Maar hoe zit dat nou met grotere programma's van bijvoorbeeld 200 regels? Dat is andere koek. Wanneer je programma groter wordt dan wat je nu gewend bent, is het gemakkelijk om het overzicht kwijt te raken en niet te weten wat je moet doen. In dit hoofdstuk staat uitleg en een oefening hoe je een groter programma kunt aanpakken. Dit is best handig voor het maken van de eindopdracht.

## Verdeel en heers
Je hebt vast wel eens een keer in een probleem of puzzel vastgezeten. Er zijn heel veel mogelijkheden om uit zo'n puzzel of probleem te komen. De gemakkelijkste is natuurlijk naar de oplossing kijken, maar dat een beetje flauw. Het is wel de bedoeling dat je zelf tot een oplossing komt. Een van de mogelijkheden is om het probleem op te delen in kleinere problemen. Of de grote stappen op te delen in kleinere stappen. In het programmeer-onderwijs noemen we dit de *Top-Down*-benadering. In deze benadering bekijk je een opdracht van een kleine afstand en breekt de opdracht op in kleinere deelopdrachten. Eigenlijk net zoals je een bord met veel eten op eet. Die eet je ook niet in één hap op. 

Met de Top-down benadering voor jouw grotere Python-programma ga je gebruik maken van *Storyboarden*. Een storyboard is een reeks eenvoudige tekeningen, waarmee je laat zien wat er in je programma gebeurt. Dit helpt je na te denken over de structuur van je programma, zonder dat je meteen met Python-code bezig bent. Vervolgens ga je de verschillende delen van het overzicht uitwerken in *pseudo-code*. Dat is een opstap naar echte Python code. Wanneer je alle delen hebt uitgewerkt, kun je aan de slag met het omzetten van je pseudo-code naar werkende Python code.

In een storyboard beschrijf je de belangrijke interacties met de gebruiker van je spel. Je mag dit tekenen/schetsen. Je mag het ook in woorden omschrijven. In het uitgewerkte voorbeeld hieronder worden woorden gebruikt om de belangrijkste interacties te omschrijven. Je kunt zelf natuurlijk de volgende hulpmiddelen ook gebruiken:
- Powerpoint
- Pen en papier (zelfs met kleurtjes)
- Google Slides
- whiteboard (vergeet dan niet een foto te maken, anders raak je je storyboard gemakkelijk kwijt)

**Voorbeeld**
We gaan het spelletje *Raad het getal* als voorbeeld nemen. In dit spelletje moet de speler een getal raden. De computer zegt dan of je gok te hoog, te laag of juist is. Je score is het aantal pogingen wat je nodig hebt gehad om het getal te raden. Tot zover de beschrijving van het spel.
We gaan een storyboard maken.

:::{admonition} Storyboard Raad het getal

**1. Startscherm**
| | |
|-|-|
|Wat is er te zien? | Een welkomstboodschap op het scherm. Bijv. "Welkom bij Raad het Getal! Voer een getal in tussen 1 en 100." |
|Wat gebeurt er? | Een welkomstboodschap wordt op het scherm gezet.<br/>De score wordt op 0 gezet. |
|Pseudocode | `Druk welkomstboodschap af.`<br/>`Zet score op 0`.|

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
|Pseudocode | `Als het ingevoerde getal lager is dan het doelgetal, zeg "Te laag" en ga naar scherm 2.`<br/>`Als het ingevoerde getal hoger is dan het doelgetal, zeg "Te hoog" en ga naar scherm 2.`<br/>`Als het ingevoerde getal gelijk is aan het doelgetal, ga naar scherm 4.`|

**4. Einduitslag**
| | |
|-|-|
|Wat is er te zien? | Een boodschap met felicitaties en de behaalde score |
|Wat gebeurt er? | Het programma drukt "Gefeliciteerd, je hebt het juiste getal geraden!" en de score af |
|Pseudocode | `Druk felicitatie en score af`|

<<<<<<< Updated upstream
:::
=======
## 

:::


Validatie van invoer!
>>>>>>> Stashed changes
