<!-- .slide: data-background-gradient="linear-gradient(to bottom right, #f1881c, #ffffff)" -->

# Basis van Programmeren

Q-highschool / Bijeenkomst 3

---

## Vandaag

- Opfrisquiz
- Input vragen
- `if`/`else`
- Afsluiting

***

## Opfrisquiz

---

Wat print dit programma? (1)

```python
a = 12
b = 39
c = 16.4
min(max(a, b), b)
```

- 12
- 39
- 16.4
- Niets

<!-- .element: class="mc" -->

---

Wat print dit programma? (2)

```python
a = 12
b = 39
r = min(max(a, b), b)
print(r)
```

- 12
- 39
- b
- r

<!-- .element: class="mc" -->

---

Wat print dit programma? (3)

```python
print("max(7, 83, 5.5)")
```

- 83
- max(7, 83, 5.5)
- 7
- 5.5

<!-- .element: class="mc" -->

---

Wat betekent een `#` in Python?

- De rest van het programma is commentaar
- Het volgende woord is commentaar
- De rest van de regel is commentaar
- Deze regel is commentaar

<!-- .element: class="mc" -->

---

Wat is commentaar?

- Een soort foutmelding
- Tekst in de code, bijvoorbeeld om te printen
- Extra tekst die niet als code wordt gezien
- Duidelijke variabelenamen

<!-- .element: class="mc" -->

---

Wat print dit programma? (4)

```python
print(type(3 + 4.5))
```

- `<class 'str'>`
- `<class 'float'>`
- `<class 'complex'>`
- `<class 'int'>`

<!-- .element: class="mc" -->

---

Wat is het verschil tussen een `int` en een `float`?

- `int` is een geheel getal; `float` is een decimaal getal
- `int` is een tekst; `float` is een getal
- `int` is een negatief getal; `float` is een positief getal
- Er is geen verschil; beide zijn hetzelfde

<!-- .element: class="mc" -->

---

Wat print dit programma? (5)

```python
print("5" + "3")
print(5 + 3)
```

- 8\
  8
- 53\
  53
- 53\
  8
- 8\
  53

<!-- .element: class="mc" style="font-size: .9em" -->

---

Wat print dit programma? (6)

```python
a = "3"
b = "5"
print(a * b)
```

- 15
- 555
- 33333
- `TypeError: can't multiply sequence by non-int of type 'str'`

<!-- .element: class="mc" -->

---

Hoe reken je met een `str`?

```python
getal = "15"
```

- `2 * int(getal)`
- `"2" * getal`
- `2 * int("getal")`
- `int(2) * getal`

<!-- .element: class="mc" -->

***

## Input vragen

---

Maak een papegaai, die precies terugzegt wat jij tegen de papegaai zegt.

&nbsp;

```python[|2|2-3]
print("Ik ben een papegaai!")
tekst = input("Wat zeg jij? ")
print(tekst)
```

<!-- .element: class="fragment" -->

---

<!-- .slide: data-auto-animate data-auto-animate-id="rekenmachine" -->

Een simpele rekenmachine: vraag twee getallen en print de vermenigvuldiging.

&nbsp;

```python
a = input("Eerste getal: ")
b = input("Tweede getal: ")
print(a * b)
```

<!-- .element: class="fragment" data-id="rekenmachine-code" -->

&nbsp;

```text
TypeError: can't multiply sequence by 
           non-int of type 'str'
```

<!-- .element: class="fragment" -->

---

<!-- .slide: data-auto-animate data-auto-animate-id="rekenmachine" -->

Een simpele rekenmachine: vraag twee getallen en print de vermenigvuldiging.

&nbsp;

```python
a = int(input("Eerste getal: "))
b = int(input("Tweede getal: "))
print(a * b)
```

<!-- .element: data-id="rekenmachine-code" -->

Notes:
En wat als we met kommagetallen willen rekenen?

***

## `if`/`else`-statements

---

### Keuzes maken

Een bot die alleen iets doet als je er Hallo tegen zegt.

```python
tekst = input("Hoi! ")
if tekst == "Hallo":
    print("Tot ziens!")
```
<!-- .element: class="fragment" -->

---

<div class="columns" style="font-size: .8em">
<div>

`=`

<!-- .element: style="font-size: 6em; line-height: .6;" -->

- Een waarde in een variabele zetten
  <!-- .element: class="fragment" data-fragment-index="1" -->
- Spreek uit als 'wordt'
  <!-- .element: class="fragment" data-fragment-index="2" -->

</div>
<div>

`==`

<!-- .element: style="font-size: 6em; line-height: .6;" -->

- Twee waardes vergelijken
  <!-- .element: class="fragment" data-fragment-index="1" -->
- Spreek uit als 'is'
  <!-- .element: class="fragment" data-fragment-index="2" -->
<li class="fragment">

    Geeft een booleaanse waarde:\
    `True` (waar) of\
    `False` (niet waar)

</li>

</div>
</div>

---

### Of anders

```python
tekst = input("Hoi! ")
if tekst == "Hallo":
    print("Tot ziens!")
else:
    print("Je moet Hallo zeggen.")
```

---

<!-- .slide: data-auto-animate data-auto-animate-id="oefening" -->

### Oefening
                    
Schrijf een Python programma dat controleert of een ingevoerd wachtwoord correct is. Het wachtwoord mag je zelf kiezen.

Gebruik `input()` en `if` als bouwstenen voor je programma.

Werk in Visual Studio Code, Thonny of de [CS Circles Console](https://cscircles.cemc.uwaterloo.ca/console-nl/)

---

<!-- .slide: class="full-height top" data-auto-animate data-auto-animate-id="oefening" -->

### Oefening

Schrijf een Python programma dat controleert of een ingevoerd wachtwoord correct is. Het wachtwoord mag je zelf kiezen.

<!-- .element: style="font-size: .75em" -->

Notes:
Uitwerking:

```python
wachtwoord = input("Voer het wachtwoord in: ")
if wachtwoord == "geheim123":
    print("Wachtwoord correct!")
else:
    print("Wachtwoord onjuist.")
```

***

## Aan de slag!

[*Les 3* in de syllabus](../3_input_if.html)

Let op: hoofdstuk 5, 6 en *9* in CSCircles

***

## Afsluiting

---

Wat is de output?

```python
antwoord = "nee"
if antwoord == "ja":
    print("Oke, doen we")
else:
    print("Dan niet")
print("Dikke doei!")
```

<!-- .element: style="font-size: .6em" -->

- ```plaintext
    Oke, doen we
    Dikke doei!
    ```
- ```plaintext
    Oke, doen we
    ```
- ```plaintext
    Dan niet
    Dikke doei!
    ```
- ```plaintext
    Dan niet
    ```

<!-- .element: class="mc grid" -->

---

## Volgende week

Fysieke bijeenkomst
