<!-- .slide: data-background-gradient="linear-gradient(to bottom right, #f1881c, #ffffff)" -->

# Basis van Programmeren

Q-vak Informatica / Bijeenkomst 7

---

## Vandaag

- Opfrisquiz
- Een groter programma schrijven
- Vragen over de eindopdracht?

***

## Opfrisquiz

---

Hoe print je de tekst *Dit is leuk!* met Python?

- `print "Dit is leuk!"`
- `print(Dit is leuk!)`
- `print("Dit is leuk!")`
- `print('Dit is leuk!')`

<!-- .element: class="mc" -->

---

Wat print dit programma?

```python
appels = 14
appels = 8
print(appels)
```

- 14
- 8
- 22
- Dat kun je niet weten

<!-- .element: class="mc" -->

---

Wat print dit programma?

```python
kleinste = min(14, 99
grootste = max(3, 4)
print(kleinste + grootste)
```

- 28
- SyntaxError: invalid syntax
- 102
- NameError: kleinste is not defined

<!-- .element: class="mc" -->

---

Wat print dit programma? (5)

```python
print("2" + "9")
print(2 + 9)
```

- 11\
  11
- 29\
  29
- 29\
  11
- 11\
  29

<!-- .element: class="mc" style="font-size: .9em" -->

---

Wat is het verschil tussen een `int` en een `float`?

- `int` is een geheel getal; `float` is een decimaal getal
- `int` is een tekst; `float` is een getal
- `int` is een negatief getal; `float` is een positief getal
- Er is geen verschil; beide zijn hetzelfde

<!-- .element: class="mc" -->

---

Welk Python commando gebruik je om iets te vragen?

- `get`
- `print`
- `input`
- `ask`

<!-- .element: class="mc" -->

---

Welk van deze codes print "We zijn er bijna" als de variabele `invoer` gelijk is aan "zijn we er"?

-   ```python
    if invoer = "zijn we er":
        print("We zijn er bijna")
    ```
-   ```python
    if invoer == "zijn we er":
        print("We zijn er bijna")
    ``` 
-   ```python
    if invoer = "zijn we er":
    print("We zijn er bijna")
    ```
-   ```python
    if invoer == "zijn we er":
    print("We zijn er bijna")
    ```

<!-- .element: class="mc" style="width: 70%" -->

---

Wat is de output?

```python
i = 0
while i < 10:
    print(i)
    i = 27
print("En klaar!")
```

<!-- .element: style="font-size: .7em" -->

-   ```plaintext
    0
    En klaar!
    ```
-   ```plaintext
    0
    27
    ```
-   ```plaintext
    En klaar!
    ```
-   ```plaintext
    0
    27
    En klaar!
    ```
<!-- .element: class="mc grid" style="font-size: .8 style="font-size: .55em"em"  -->

---

Wat doet `def`?

- Maakt een variabele **def**initief
- Geeft een variabele later (**def**erred) een waarde
- Geeft de standaard (**def**ault) keuze
- **Def**inieert een functie

<!-- .element: class="mc" -->

---

Wat staat op de plek van de blokken?

```python
# Berekent het kwadraat van een getal
def kwadraat(x):
    ████████ x * x
```

- `return`
- `def:`
- `return:`
- `def`

<!-- .element: class="mc" -->

---

```python
dieren = [ "Olifant", "Vink", "Goudvis", 
           "Leguaan", "Muis" ]
```

Wat is `dieren[1]`?

- Olifant
- Vink
- Goudvis
- Leguaan

<!-- .element: class="mc" -->

---

Met welke functie kun je de lengte van een lijst vinden?

- `length`
- `size`
- `len`
- `count`

<!-- .element: class="mc" -->

---

Schrijf een functie die twee getallen optelt.

- ```python
  def telop a b:
      return a + b
  ```
- ```python
  def telop(a, b):
      a + b
  ```
- ```python
  def telop(a, b):
      return a + b
  ```
- ```python
  def telop a b:
      a + b
  ```

<!-- .element: class="mc" -->

***

## Een groter programma schrijven

---

### Stappenplan

1. Maak een storyboard met interacties
2. Beschrijf interactie in pseudocode
3. Vertaal naar echte Python code
4. Voeg codeblokken samen

***

### Storyboard en pseudocode

Per interactie  / "scherm":

- Wat is er te zien?
- Wat gebeurt er?
- Pseudocode

---

### Voorbeeld

*Raad het getal*:\
Gebruiker raadt een getal.\
Computer geeft aan hoger, lager of correct.\
Score is het aantal pogingen.

---

#### Storyboards

1. Startscherm
2. Invoer van de gebruiker
3. Antwoord
4. Einduitslag

---

##### 1. Startscherm

- Wat is er te zien?
  - Een welkomstboodschap <!-- .element: class="fragment" -->
- Wat gebeurt er?
  - De welkomstboodschap wordt getoond <!-- .element: class="fragment" -->
  - De score wordt op 0 gezet <!-- .element: class="fragment" -->
  - Een getal om te raden wordt gekozen <!-- .element: class="fragment" -->
- Pseudocode:
  ```plaintext
  Print welkomstboodschap
  Zet score op 0
  Kies een willekeurig doelgetal tussen 1 en 100
  ```
  <!-- .element: class="fragment" style="font-size: .55em" -->

---

##### 2. Invoer van de gebruiker

- Wat is er te zien?
  - Een plek om een getal in te voeren <!-- .element: class="fragment" -->
- Wat gebeurt er?
  - De speler wordt gevraagd een getal in te voeren <!-- .element: class="fragment" -->
- Pseudocode:
  ```plaintext
  Vraag om een getal
  Sla het getal op
  Verhoog de score met 1
  ```
  <!-- .element: class="fragment" style="font-size: .55em" -->

---

##### 3. Antwoord

- Wat is er te zien?
  - Het resultaat: te hoog, te laag of correct <!-- .element: class="fragment" -->
- Wat gebeurt er?
  - Invoer wordt met het doel vergeleken <!-- .element: class="fragment" -->
  - Feedback wordt geprint <!-- .element: class="fragment" -->
  - Als fout: opnieuw een getal invoeren <!-- .element: class="fragment" -->
- Pseudocode
  ```plaintext
  Als lager: print "te laag" en ga naar scherm 2
  Als hoger: print "te hoog" en ga naar scherm 2
  Als correct: ga naar scherm 4
  ```
  <!-- .element: class="fragment" style="font-size: .55em" -->

---

##### 4. Einduitslag

- Wat is er te zien?
  - Felicitatie en behaalde score <!-- .element: class="fragment" -->
- Wat gebeurt er?
  - Felicitatie wordt geprint <!-- .element: class="fragment" -->
  - De score wordt geprint <!-- .element: class="fragment" -->
- Pseudocode:
  ```plaintext
  Print felicitatie
  Print de score
  ```
  <!-- .element: class="fragment" style="font-size: .55em" -->

---

#### [Oefening 7.1](../7_een_programma_schrijven.html#storyboard-galgje)

Maak een storyboard voor je eindopdracht.

Gebruik het sjabloon met *Wat is er te zien?*, *Wat gebeurt er?* en *Pseudocode*.

***

### Vertaling naar Python

---

##### 1. Startscherm

```plaintext
Print welkomstboodschap
Zet score op 0
Kies een willekeurig doelgetal tussen 1 en 100
```

<!-- .element: style="font-size: .55em" -->

```python[1|2|3|]
print("Welkom bij Raad-het-getal")
score = 0
doelgetal = randint(1, 100)
```
<!-- .element: class="fragment" style="font-size: .55em" -->

```python
# Om randint beschikbaar te maken heb je een import nodig:
from random import randint
```
<!-- .element: class="fragment" style="font-size: .55em" -->

---

##### 2. Invoer van de gebruiker

```plaintext
Vraag om een getal
Sla het getal op
Verhoog de score met 1
```

<!-- .element: style="font-size: .55em" -->

```python[1|2|]
invoer = int(input("Voer een getal in tussen 1 en 100: "))
score = score + 1
```
<!-- .element: class="fragment" style="font-size: .55em" -->

---

##### 3. Antwoord

```plaintext
Als lager: print "te laag" en ga naar scherm 2
Als hoger: print "te hoog" en ga naar scherm 2
Als correct: ga naar scherm 4
```

<!-- .element: style="font-size: .55em" -->

```python[1-2|3-4|]
if invoer < doelgetal:
    print("Te laag!")
elif invoer > doelgetal:
    print("Te hoog!")
```
<!-- .element: class="fragment" style="font-size: .55em" -->

Note:
We kunnen nog niets doen met de navigatie, dat hangt af van de volgorde

---

##### 4. Einduitslag

```plaintext
Print felicitatie
Print de score
```

<!-- .element: style="font-size: .55em" -->

```python
print("Gefeliciteerd! Je hebt het getal juist geraden!")
print("Je score is", score, "punten.")
```
<!-- .element: class="fragment" style="font-size: .55em" -->

---

#### [Oefening 7.3](../7_een_programma_schrijven.html#7_een_programma_schrijven-exercise-2)

Vertaal de pseudocode van je eindopdracht naar Python codeblokken.

***

### Codeblokken samenvoegen

---

<!-- .slide: data-auto-animate -->

```python
# 1. Startscherm
# 2. Invoer van de gebruiker
# 3. Antwoord
# 4. Eindresultaat
```
<!-- .element: data-id="raad-programma" style="font-size: .55em" -->

Note:
Hoe gaat de flow? Vanuit 3 gaan we terug naar 2 of door naar 4

---

<!-- .slide: data-auto-animate -->

```python
# 1. Startscherm

goedGeraden = False

while not goedGeraden:
    # 2. Invoer van de gebruiker
    # 3. Antwoord

# 4. Einduitslag
```
<!-- .element: data-id="raad-programma" style="font-size: .55em" -->

---

<!-- .slide: data-auto-animate -->

```python[1-2]
# Om randint beschikbaar te maken heb je een import nodig:
from random import randint

# 1. Startscherm

goedGeraden = False

while not goedGeraden:
    # 2. Invoer van de gebruiker
    # 3. Antwoord

# 4. Einduitslag
```
<!-- .element: data-id="raad-programma" style="font-size: .55em" -->

---

<!-- .slide: data-auto-animate -->

```python[5-7]
# Om randint beschikbaar te maken heb je een import nodig:
from random import randint

# 1. Startscherm
print("Welkom bij Raad-het-getal")
score = 0
doelgetal = randint(1, 100)
goedGeraden = False

while not goedGeraden:
    # 2. Invoer van de gebruiker
    # 3. Antwoord

# 4. Einduitslag
```
<!-- .element: data-id="raad-programma" style="font-size: .55em" -->

---

<!-- .slide: data-auto-animate -->

```python[12-13]
# Om randint beschikbaar te maken heb je een import nodig:
from random import randint

# 1. Startscherm
print("Welkom bij Raad-het-getal")
score = 0
doelgetal = randint(1, 100)
goedGeraden = False

while not goedGeraden:
    # 2. Invoer van de gebruiker
    invoer = int(input("Voer een getal in tussen 1 en 100: "))
    score = score + 1

    # 3. Antwoord

# 4. Einduitslag
```
<!-- .element: data-id="raad-programma" style="font-size: .55em" -->

---

<!-- .slide: data-auto-animate -->

```python[16-19]
# Om randint beschikbaar te maken heb je een import nodig:
from random import randint

# 1. Startscherm
print("Welkom bij Raad-het-getal")
score = 0
doelgetal = randint(1, 100)
goedGeraden = False

while not goedGeraden:
    # 2. Invoer van de gebruiker
    invoer = int(input("Voer een getal in tussen 1 en 100: "))
    score = score + 1

    # 3. Antwoord
    if invoer < doelgetal:
        print("Te laag!")
    elif invoer > doelgetal:
        print("Te hoog!")

# 4. Einduitslag
```
<!-- .element: data-id="raad-programma" style="font-size: .55em" -->

---

<!-- .slide: data-auto-animate -->

```python[20-21]
# Om randint beschikbaar te maken heb je een import nodig:
from random import randint

# 1. Startscherm
print("Welkom bij Raad-het-getal")
score = 0
doelgetal = randint(1, 100)
goedGeraden = False

while not goedGeraden:
    # 2. Invoer van de gebruiker
    invoer = int(input("Voer een getal in tussen 1 en 100: "))
    score = score + 1

    # 3. Antwoord
    if invoer < doelgetal:
        print("Te laag!")
    elif invoer > doelgetal:
        print("Te hoog!")
    else: # invoer == doelgetal
        goedGeraden = True

# 4. Einduitslag
```
<!-- .element: data-id="raad-programma" style="font-size: .55em" -->

---

<!-- .slide: data-auto-animate -->

```python[24-25|]
# Om randint beschikbaar te maken heb je een import nodig:
from random import randint

# 1. Startscherm
print("Welkom bij Raad-het-getal")
score = 0
doelgetal = randint(1, 100)
goedGeraden = False

while not goedGeraden:
    # 2. Invoer van de gebruiker
    invoer = int(input("Voer een getal in tussen 1 en 100: "))
    score = score + 1

    # 3. Antwoord
    if invoer < doelgetal:
        print("Te laag!")
    elif invoer > doelgetal:
        print("Te hoog!")
    else: # invoer == doelgetal
        goedGeraden = True

# 4. Einduitslag
print("Gefeliciteerd! Je hebt het getal juist geraden!")
print("Je score is", score, "punten.")
```
<!-- .element: data-id="raad-programma" style="font-size: .55em" -->

---

#### [Oefening 7.5](../7_een_programma_schrijven.html#7_een_programma_schrijven-exercise-4)

Voeg de codeblokken voor je eindopdracht samen.

***

## Vragen over de eindopdracht?

---

## Dat was 'm

Denk aan de deadline:\
{{ eerste_inlevermoment }}

> Lever een `.py`-bestand in <br/>bij de Q-vakken App! 
<!-- .element: style="background-color: lightgrey; border: 1px solid black;" -->

