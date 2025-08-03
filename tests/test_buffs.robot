*** Settings ***
Library    tests.keywords.BuffKeywords



*** Test Cases ***
Validiere Buff Datei
    Buff Datei Laden    ./buffs/buffs.yml
    Alle Buffs Müssen Gültig Sein
