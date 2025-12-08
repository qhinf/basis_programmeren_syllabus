<!-- .slide: data-background-gradient="linear-gradient(to bottom right, #f1881c, #ffffff)" -->

# Basis van Programmeren

Q-highschool / Bijeenkomst 5

---

## Vandaag

- Opfrisquiz
- Zelf functies maken met `def`
- Lijsten
- Afsluiting

***

## Opfrisquiz

---

Wat is de output?

```python
antwoord = "nee"
if antwoord == "ja":
    print("Oke, doen we")
else:
    print("Dan niet")
print("Goedemiddag")
```

<!-- .element: style="font-size: .6em" -->

- ```plaintext
    Oke, doen we
    Goedemiddag
    ```
- ```plaintext
    Oke, doen we
    ```
- ```plaintext
    Dan niet
    Goedemiddag
    ```
- ```plaintext
    Dan niet
    ```

<!-- .element: class="mc grid" -->

---

Je wilt de tafel van 7 printen. Welke Python constructie kies je?

- `if`
- `while`
- `loop`
- `for`

<!-- .element: class="mc" -->

---

Wat is de output?

```python
antwoord = "ja"
while antwoord == "ja":
    print("Oke, doen we")
    antwoord = "nee"
print("Goedemiddag")
```

<!-- .element: style="font-size: .6em" -->

- ```plaintext
    Oke, doen we
    Goedemiddag
    ```
- ```plaintext
    Oke, doen we
    ```
- ```plaintext
    Goedemiddag
    ```
- ```plaintext
    Oke, doen we
    Oke, doen we
    Oke, doen we
    Oke, doen we
    Oke, doen we
    Oke, doen we
    Oke, doen we
    Oke, doen we
    ...
    ```

<!-- .element: class="mc" style="font-size: .8em" -->

---

Wat is de output?

```python
for i in range(0, 10):
    print(i, "* 7 =", i * 7)
```

- ```plaintext
    1 * 7 = 7
    2 * 7 = 64
    ...
    10 * 7 = 70
    ```
- ```plaintext
    0 * 7 = 0
    1 * 7 = 7
    ...
    9 * 7 = 63
    ```
- ```plaintext
    0* 7 =0
    1* 7 =7
    ...
    10* 7 =7
    ```
- ```plaintext
    0 * 7 = 0
    1 * 7 = 7
    ...
    10 * 7 = 7
    ```

<!-- .element: class="mc grid" style="font-size: .8em" -->

---

## Tip:

Maak een spiekbriefje!

***

## Zelf functies maken met `def`

---

Notes:
- Doel: code uitsplitsen en hergebruiken
    - Een begroeting printen, `def groet(naam):`
- Meerdere argumenten
    - Uitgebreide begroeting, `def groet(dagdeel, naam):`
- return: waarde teruggeven
    - Voorbeeld: `absoluut`

Daarna code hierop zetten en de belangrijke syntaxdingetjes aantekenen

---

```python
def absoluut(x):
    if x >= 0:
        return x 
    else:
        return -x
```

---

### Oefening

> 99 bottles of beer on the wall, 99 bottles of beer.\
> Take one down, pass it around, 98 bottles of beer on the wall.
<!-- .element: style="font-size: .75em; width: 100%" -->

Schrijf een functie die als argument een getal krijgt en het bijbehorende couplet van "bottles of beer" print. Verzin zelf iets leuks voor de laatste zin van couplet 0.

Gebruik die functie om alle coupletten van 99 t&NoBreak;/&NoBreak;m 1 te printen.

Notes:
Drink met mate. Andere dranken naar keuze zijn ook toegestaan.

---

```python
def bottles_of_beer(n):
    # hier komt dus jouw code

for n in range(100, 1, -1):
    bottles_of_beer(n)
```

***

## Lijsten

---

Notes:
- Variabelen: een ding opslaan, `naam`
- Lijsten: meerdere dingen combineren, `aanwezigen`
- syntax, code kopiëren en aantekenen
- index, `aanwezigen[1]`
- lengte, `len(aanwezigen)`
- for over een lijst, `for persoon in aanwezigen: print(persoon)`

---

### Oefening

Schrijf een functie die het gemiddelde van de getallen in een lijst berekent.

```python
def gemiddelde(getallen):
    # Schrijf hier je code

resultaat = gemiddelde([ 2, 9, 4, 15, 7 ])
print(resultaat)
```

---

```python
def gemiddelde(getallen):
    totaal = 0
    for n in getallen:
        totaal = totaal + n

    return totaal/len(getallen)
```

***

## Afsluiting

---

Wat doet `def`?

- Maakt een variabele **def**initief
- **Def**inieert een functie
- **Def**inieert een variabele
- Geeft de standaard (**def**ault) keuze

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

Wat is de output? (1)

```python
def zeghallo(naam):
    print("Hallo, " + naam + "!")

zeghallo("Pieter")
zeghallo("Jeroen")
```

<!-- .element: style="font-size: .6em" -->

- ```plaintext
    Hallo, PieterJeroen!
    ```
- ```plaintext
    
    ```
- ```plaintext
    Hallo, !
    Hallo, !
    ```
- ```plaintext
    Hallo, Pieter!
    Hallo, Jeroen!
    ```

<!-- .element: class="mc" style="font-size: .8em" -->

---

Wat is de output? (2)

```python
def zeghallo(naam):
    return "Hallo, " + naam + "!"

zeghallo("Pieter")
zeghallo("Jeroen")
```

<!-- .element: style="font-size: .6em" -->

- ```plaintext
    Hallo, PieterJeroen!
    ```
- ```plaintext
    
    ```
- ```plaintext
    Hallo, !
    Hallo, !
    ```
- ```plaintext
    Hallo, Pieter!
    Hallo, Jeroen!
    ```

<!-- .element: class="mc" style="font-size: .8em" -->

---

Wat is de output? (3)

```python
def zeghallo(naam):
    return "Hallo, " + naam + "!"

print(zeghallo("Pieter"))
print(zeghallo("Jeroen"))
```

<!-- .element: style="font-size: .6em" -->

- ```plaintext
    Hallo, PieterJeroen!
    ```
- ```plaintext
    
    ```
- ```plaintext
    zeghallo("Pieter")
    zeghallo("Jeroen")
    ```
- ```plaintext
    Hallo, Pieter!
    Hallo, Jeroen!
    ```

<!-- .element: class="mc" style="font-size: .8em" -->

---

```python
dieren = [ "Olifant", "Vink", "Goudvis", 
           "Leguaan", "Muis" ]
```

Wat is `dieren[2]`?

- Olifant
- Vink
- Goudvis
- Leguaan

<!-- .element: class="mc" -->

---

```python
dieren = [ "Olifant", "Vink", "Goudvis", 
           "Leguaan", "Muis" ]
```

Wat is `dieren[5]`?

- Muis
- `IndexError: list index out of range` <!-- .element: style="font-size: .8em" -->
- Penguin
- Olifant

<!-- .element: class="mc" -->

---

Met welke functie kun je de lengte van een lijst vinden?

- `length`
- `size`
- `len`
- `count`

<!-- .element: class="mc" -->

---

```python
dieren = [ "Olifant", "Vink", "Goudvis", 
           "Leguaan", "Muis" ]
```

Hoe pak je het laatste element uit deze lijst?

- `dieren[0]`
- `dieren[-1]`
- `dieren[len(dieren)]`
- `dieren[len(dieren) - 1]`

<!-- .element: class="mc" -->

Notes:
Zowel `dieren[-1]` als `dieren[len(dieren) - 1]` zijn correct

---

## Volgende week

Fysieke bijeenkomst: handige programmeerpatronen
