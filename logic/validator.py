def validate_buffs(buff_list):
    """
    Erwartet: Liste von Dicts mit Keys:
      - name (str)
      - stat (one of: health, stamina, attack_power)
      - value (float|int|numeric string)
      - duration (float|int|numeric string > 0)
    """
    errors = []
    if not isinstance(buff_list, list) or not buff_list:
        return ["Datei enthält keine Liste von Buffs. Erwartet: eine Liste von Objekten."]

    allowed_stats = {"health", "stamina", "attack_power"}

    for i, buff in enumerate(buff_list, start=1):
        # Basis-Keys prüfen
        for key in ("name", "stat", "value", "duration"):
            if key not in buff:
                errors.append(f"Eintrag {i}: Feld '{key}' fehlt.")
        if errors:
            continue

        # Stat prüfen
        stat = str(buff["stat"]).strip()
        if stat not in allowed_stats:
            errors.append(f"{buff['name']}: ungültiger Stat '{stat}' (erlaubt: {', '.join(sorted(allowed_stats))})")

        # Value prüfen (Zahl)
        try:
            float(buff["value"])
        except (TypeError, ValueError):
            errors.append(f"{buff['name']}: 'value' ist keine Zahl.")

        # Duration prüfen (> 0)
        try:
            if float(buff["duration"]) <= 0:
                errors.append(f"{buff['name']}: 'duration' muss > 0 sein.")
        except (TypeError, ValueError):
            errors.append(f"{buff['name']}: 'duration' ist keine Zahl.")

    return errors
