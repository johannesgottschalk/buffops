*** Settings ***
Library    tests.keywords.BuffKeywords

*** Test Cases ***
Buff Mit Ungültigem Stat
    Buff Datei Laden    buffs/bad_stat.yml
    Validierung Muss Fehler Enthalten

Buff Mit Negativer Dauer
    Buff Datei Laden    buffs/bad_duration.yml
    Validierung Muss Fehler Enthalten

