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
| Dato       | Klokkeslett | TeaterStykke                  | Antall solgte billetter |
|------------|-------------|-------------------------------|-------------------------|
| 03-02-2024 | 18:30:00    | Størst av alt er Kjærligheten | 27                      |
| 03-02-2024 | 19:00:00    | Kongsemnene                   | 65                      |

```

### Brukstilfelle 5
```
| TeaterStykke                  | Skuespiller                | Rolle                              |
|-------------------------------|----------------------------|------------------------------------|
| Kongsemnene                   | Arturo Scotti              | Haakon Haakonssønn                 |
| Kongsemnene                   | Hans Petter Nilsen         | Skule jarl                         |
| Kongsemnene                   | Madeleine Brandtzæg Nilsen | Fru Ragnhild (Skules hustru)       |
| Kongsemnene                   | Synnøve Fossum Eriksen     | Margrete (Skules datter)           |
| Kongsemnene                   | Emma Caroline Deichmann    | Sigrid (Skules søster) / Ingebjørg |
| Kongsemnene                   | Thomas Jensen Takyi        | Biskop Nikolas                     |
| Kongsemnene                   | Per Bogstad Gulliksen      | Gregorius Jonssønn                 |
| Kongsemnene                   | Isak Holmen Sørensen       | Paal Flida                         |
| Kongsemnene                   | Emil Olafsson              | Jatgeir Skald                      |
| Kongsemnene                   | Emil Olafsson              | Dagfinn Bonde                      |
| Kongsemnene                   | Snorre Ryen Tøndel         | Peter(prest og Ingebjørgs sønn)    |
| Størst av alt er Kjærligheten | Sunniva Du Mond Nordal     | Sunniva Du Mond Nordal             |
| Størst av alt er Kjærligheten | Jo Saberniak               | Jo Saberniak                       |
| Størst av alt er Kjærligheten | Marte M. Steinholt         | Marte M. Steinholt                 |
| Størst av alt er Kjærligheten | Tor Ivar Hagen             | Tor Ivar Hagen                     |
| Størst av alt er Kjærligheten | Trond-Ove Skrødal          | Trond-Ove Skrødal                  |
| Størst av alt er Kjærligheten | Natlie Grøndahl Tangen     | Natlie Grøndahl Tangen             |
| Størst av alt er Kjærligheten | Åsmund Flaten              | Åsmund Flaten                      |
```

### Brukstilfelle 6
```
| Dato       | Klokkeslett | TeaterStykke                  | Antall solgte billetter |
|------------|-------------|-------------------------------|-------------------------|
| 03-02-2024 | 19:00:00    | Kongsemnene                   | 65                      |
| 03-02-2024 | 18:30:00    | Størst av alt er Kjærligheten | 27                      |
| 01-02-2024 | 19:00:00    | Kongsemnene                   | 0                       |
| 02-02-2024 | 19:00:00    | Kongsemnene                   | 0                       |
| 05-02-2024 | 19:00:00    | Kongsemnene                   | 0                       |
| 06-02-2024 | 18:30:00    | Størst av alt er Kjærligheten | 0                       |
| 06-02-2024 | 19:00:00    | Kongsemnene                   | 0                       |
| 07-02-2024 | 18:30:00    | Størst av alt er Kjærligheten | 0                       |
| 12-02-2024 | 18:30:00    | Størst av alt er Kjærligheten | 0                       |
| 13-02-2024 | 18:30:00    | Størst av alt er Kjærligheten | 0                       |
| 14-02-2024 | 18:30:00    | Størst av alt er Kjærligheten | 0                       |
```

### Brukstilfelle 7
```
Skriv inn skuespillernavn: Arturo Scotti
| Skuespiller A | Skuespiller B              | TeaterStykke |
|---------------|----------------------------|--------------|
| Arturo Scotti | Hans Petter Nilsen         | Kongsemnene  |
| Arturo Scotti | Madeleine Brandtzæg Nilsen | Kongsemnene  |
| Arturo Scotti | Synnøve Fossum Eriksen     | Kongsemnene  |
| Arturo Scotti | Emma Caroline Deichmann    | Kongsemnene  |
| Arturo Scotti | Thomas Jensen Takyi        | Kongsemnene  |
| Arturo Scotti | Per Bogstad Gulliksen      | Kongsemnene  |
| Arturo Scotti | Isak Holmen Sørensen       | Kongsemnene  |
| Arturo Scotti | Emil Olafsson              | Kongsemnene  |
| Arturo Scotti | Snorre Ryen Tøndel         | Kongsemnene  |
```
