import yaml
from logic.validator import validate_buffs

BUFFS = []

def buff_datei_laden(pfad):
    global BUFFS
    with open(pfad, "r", encoding="utf-8") as f:
        BUFFS = yaml.safe_load(f)

def alle_buffs_müssen_gültig_sein():
    errors = validate_buffs(BUFFS)
    if errors:
        raise AssertionError(f"Ungültige Buffs gefunden:\n" + "\n".join(errors))

def validierung_muss_fehler_enthalten():
    errors = validate_buffs(BUFFS)
    if not errors:
        raise AssertionError("Es wurden keine Fehler gefunden, obwohl welche erwartet wurden.")
