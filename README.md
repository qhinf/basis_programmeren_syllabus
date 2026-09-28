# Programmeren met Python

## Runestone inrichten

1. Maak een account aan bij [onze Runestone](https://runestone.qinf.nl/admin/auth/register). Vul bij *Institution Name* de naam **Q-vak Informatica** in en vink de *I am an instructor and want to create a course for my students.* optie aan.

   Onze Runestone kan geen "wachtwoord vergeten" emails sturen, dus zorg dat je je gebruikersnaam en wachtwoord goed onthoudt of opslaat in een wachtwoordmanager. Als je je wachtwoord vergeet, zul je een nieuw account aan moeten maken.

   Bij het inloggen *moet* je gebruik maken van je gebruikersnaam. Inloggen met je emailadres **werkt niet**.
2. Ga naar *Create Course* en kies de volgende opties:
   - Institution: Q-vak Informatica
   - State: Not in hte United States
   - Internet Domain: qinf.nl
   - Your Timezone: Europe/Amsterdam
   - Course Level: High School
   - Choose a Book: Computer Science Circles: Programmeren in Python by Computer Science Circles
   - Course Name: basis_programmeren_yyyy-b-suffix
     - Vervang yyyy-b-suffix door dezelfde code als in de syllabus/branch. Dus bijvoorbeeld 2627-1-woensdag of 2627-2.
     - Gebruik deze naam als de `runestone_course` in *_config.yml* zodat alle links in de syllabus werken
   - Course Options:
     - Check: Require a username to access this course
     - Uncheck: Enable experimental pair programming features
     - Check: Make me the Instructor of this course
     - Term start date: een datum *voor* de start van de module (vandaag is altijd goed)

---

Deze syllabus maakt gebruik van Jupyter Book. Alle inhoudelijke bestanden staan in de map *syllabus*:

- *_config.yml* is de configuratie van dit "boek". Je moet daar in elk geval de titel aanpassen! Verder zijn in de meeste gevallen geen wijzigingen nodig, maar lees de comments vooral even door.
- *_toc.yml* is de inhoudsopgave, waarin alle bestanden waaruit de syllabus bestaat op een rijtje worden gezet. Dit bestand bepaalt de volgorde van de hoofdstukken en elk bestand dat niet in de lijst voorkomt, wordt ook geen onderdeel van de syllabus.
- *index.md* is de "homepagina" van deze syllabus (want die staat bij `root` in *_toc.yml*) met de gebruikelijke introductiedingen en een aantal belangrijke zaken.
- De rest van de bestanden vormen de inhoud van de syllabus.

## Benodigdheden

- Een recente versie van Python

## De syllabus bouwen

Zorg eerst dat je alle vereiste dependencies geïnstalleerd hebt:

```sh
pip install --user -r requirements.txt
```

Vervolgens kun je de syllabus bouwen met:

```sh
jupyter-book build syllabus
```

De homepagina staat dan in *syllabus\\_build\html\index.html*.
