# TDT4145-Prosjekt Gruppe 145
Jonas De Luna Skulberg, Falk Elvedal Bruskeland, Jenny Müller

## Kommentarer/Antagelser
- Ettersom de ansatte ikke hadde epost antok vi hva eposten ville vært.
- Alle forestillingene for et gitt skuespill har samme klokkeslett, så de er derfor satt inn med bestemt tid.
- Antar den forestillingen som har solgt best, er den med flest solgte billetter for brukertilfelle 6.
- For brukertilfelle 4 antar vi at det er ønsket å vise antall solgte billetter for hver forestilling, ikke for dagen totalt.

## Oppstartsguide
Åpne terminal og påse at du har python versjon 3 eller høyere installert. Deretter kan du kjøre kommandoene nevnt nedenfor for å teste brukstilfellene.

Brukstilfelle 1 og 2: `python3 cleanDatabase.py`

Brukstilfelle 3: `python3 useCase3.py`

Brukstilfelle 4: `python3 useCase4.py`

Brukstilfelle 5: `python3 useCase5.py`

Brukstilfelle 6: `python3 useCase6.py`

Brukstilfelle 7: `python3 useCase7.py`

TODO Oppdatere Output og sjekke om det blir det samme

## Output
### Brukstilfelle 3
```
Kjøpte en Ordinær billett på setenummer 1 og radnummer 1 i salområdet Balkong
Kjøpte en Ordinær billett på setenummer 2 og radnummer 1 i salområdet Balkong
Kjøpte en Ordinær billett på setenummer 3 og radnummer 1 i salområdet Balkong
Kjøpte en Ordinær billett på setenummer 4 og radnummer 1 i salområdet Balkong
Kjøpte en Ordinær billett på setenummer 5 og radnummer 1 i salområdet Balkong
Kjøpte en Ordinær billett på setenummer 6 og radnummer 1 i salområdet Balkong
Kjøpte en Ordinær billett på setenummer 7 og radnummer 1 i salområdet Balkong
Kjøpte en Ordinær billett på setenummer 8 og radnummer 1 i salområdet Balkong
Kjøpte en Ordinær billett på setenummer 9 og radnummer 1 i salområdet Balkong
```

### Brukstilfelle 4
```
Skriv inn datoen du vil vise billetter til (FORMAT DD-MM-YYYY): 03-02-2024
Forestilling den 03-02-2024 klokken 18:30:00 for stykke "Størst av alt er Kjærligheten" - 27 solgte billetter
Forestilling den 03-02-2024 klokken 19:00:00 for stykke "Kongsemnene" - 65 solgte billetter 
```

### Brukstilfelle 5
```
Kongsemnene:
Skuespiller: Arturo Scotti - Rolle: Haakon Haakonssønn
Skuespiller: Hans Petter Nilsen - Rolle: Skule jarl
Skuespiller: Madeleine Brandtzæg Nilsen - Rolle: Fru Ragnhild (Skules hustru)
Skuespiller: Synnøve Fossum Eriksen - Rolle: Margrete (Skules datter)
Skuespiller: Emma Caroline Deichmann - Rolle: Sigrid (Skules søster) / Ingebjørg
Skuespiller: Thomas Jensen Takyi - Rolle: Biskop Nikolas
Skuespiller: Per Bogstad Gulliksen - Rolle: Gregorius Jonssønn
Skuespiller: Isak Holmen Sørensen - Rolle: Paal Flida
Skuespiller: Emil Olafsson - Rolle: Jatgeir Skald
Skuespiller: Emil Olafsson - Rolle: Dagfinn Bonde
Skuespiller: Snorre Ryen Tøndel - Rolle: Peter(prest og Ingebjørgs sønn)

Størst av alt er Kjærligheten:
Skuespiller: Sunniva Du Mond Nordal - Rolle: Sunniva Du Mond Nordal
Skuespiller: Jo Saberniak - Rolle: Jo Saberniak
Skuespiller: Marte M. Steinholt - Rolle: Marte M. Steinholt
Skuespiller: Tor Ivar Hagen - Rolle: Tor Ivar Hagen
Skuespiller: Trond-Ove Skrødal - Rolle: Trond-Ove Skrødal
Skuespiller: Natlie Grøndahl Tangen - Rolle: Natlie Grøndahl Tangen
Skuespiller: Åsmund Flaten - Rolle: Åsmund Flaten
```

### Brukstilfelle 6
```
Forestilling den 03-02-2024 for teaterstykke "Kongsemnene"  - 65 solge billetter
Forestilling den 03-02-2024 for teaterstykke "Størst av alt er Kjærligheten"  - 27 solge billetter
Forestilling den 01-02-2024 for teaterstykke "Kongsemnene"  - 0 solge billetter
Forestilling den 02-02-2024 for teaterstykke "Kongsemnene"  - 0 solge billetter
Forestilling den 05-02-2024 for teaterstykke "Kongsemnene"  - 0 solge billetter
Forestilling den 06-02-2024 for teaterstykke "Størst av alt er Kjærligheten"  - 0 solge billetter
Forestilling den 06-02-2024 for teaterstykke "Kongsemnene"  - 0 solge billetter
Forestilling den 07-02-2024 for teaterstykke "Størst av alt er Kjærligheten"  - 0 solge billetter
Forestilling den 12-02-2024 for teaterstykke "Størst av alt er Kjærligheten"  - 0 solge billetter
Forestilling den 13-02-2024 for teaterstykke "Størst av alt er Kjærligheten"  - 0 solge billetter
Forestilling den 14-02-2024 for teaterstykke "Størst av alt er Kjærligheten"  - 0 solge billetter
```

### Brukstilfelle 7
```
Skriv inn skuespillernavn: Arturo Scotti
Arturo Scotti spilte sammen med Hans Petter Nilsen i Kongsemnene
Arturo Scotti spilte sammen med Madeleine Brandtzæg Nilsen i Kongsemnene
Arturo Scotti spilte sammen med Synnøve Fossum Eriksen i Kongsemnene
Arturo Scotti spilte sammen med Emma Caroline Deichmann i Kongsemnene
Arturo Scotti spilte sammen med Thomas Jensen Takyi i Kongsemnene
Arturo Scotti spilte sammen med Per Bogstad Gulliksen i Kongsemnene
Arturo Scotti spilte sammen med Isak Holmen Sørensen i Kongsemnene
Arturo Scotti spilte sammen med Emil Olafsson i Kongsemnene
Arturo Scotti spilte sammen med Snorre Ryen Tøndel i Kongsemnene
```
