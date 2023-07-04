# Breinbrekers

Lastige opgaven die alle stof, inclusief de extra’s, behandelt. *Maak
deze dus pas als je de stof voldoende* *snapt.* Voor meer breinbrekers,
ga vooral naar [Project Euler](https://projecteuler.net/). Dit staat vol
met uitdagende opgaven.

1.  In een bepaalde regio zijn alle plaatsen door een rechtstreekse weg
    met elkaar verbonden. Maar voor alle wegen geldt
    éénrichtingsverkeer; als je van A naar B mag via de directe weg, mag
    je dus niet langs die weg van B naar A. Als je dat wel wilt zul je
    een omweg moeten nemen.
    
    In zo’n gebied ga je op zoek naar een route waarbij je iedere plaats
    precies één keer bezoekt.
    
    Schrijf een programma dat van [dit
    bestand](https://light-theme-hurts.my-ey.es/7yrsk1m.txt) met 100
    gegevensreeksen eerst willekeurig één reeks kiest. De reeksen zijn
    gescheiden door blank lines.
    
    Als de reeks bepaald is, laat je script regels hiervan inlezen.
    Het aantal in te lezen regels wordt bepaald door de eerste regel van
    elke reeks, een getal N (2 < N < 27). Hiermee wordt het aantal
    plaatsen in het gebied aangegeven. De plaatsen hebben als naam een
    hoofdletter; de eerste N hoofdletters worden gebruikt als
    plaatsnaam.
    
    Vervolgens leest je programma van de reeks in kwestie in N regels
    informatie over de richting van de verbindingswegen.
    Op de eerste regel staan de N verbindingen van A naar alle andere
    plaatsen; een 0 betekent dat de weg in A eindigt, een 1 dat de weg
    in A begint. De volgende regels gaan over de volgende plaatsen.
    
    Tussen twee plaatsen is altijd precies één weg; er zijn geen wegen
    van een plaats naar zichzelf!
    
    Je programma schrijft naar standaard output één regel met daarop een
    route waarin alle plaatsen precies één keer worden bezocht. Er is
    altijd een oplossing mogelijk.
    
    LET OP: Er wordt niet gevraagd om weer terug te gaan naar de plaats
    waar je begonnen bent.
    TIP: Kijk het .txt-bestand met reeksen door voor beter begrip van
    het format.
    
     _Naar: Nederlandse Informatica Olympiade 2019, Eerste Ronde_

2.  Schrijf een functie dat de reeksen zoals hierboven beschreven
    genereerd.
    Laat deze ook schrijven naar een bestand.

3.  Schrijf een nieuw telefoonboek-script. Je programma moet bij
    invoeren van een naam het geregistreerde telefoonnummer teruggeven,
    en vice versa.
    Ook moet je een modus hebben voor het toevoegen, verwijderen en
    bewerken (bestaand persoon, nieuw nummer) van telefoonnummers, waar
    je in blijft totdat je *exit* zegt.
    Gebruik voor alle checks (bestaat deze persoon in het telefoonboek
    etc.) een try/except statement (dit vergemakkelijkt namelijk de
    code).
    Zorg dat je script terugslaat op een telefoonboek-bestand.
