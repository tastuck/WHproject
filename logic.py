def process_order(data):
    pull_items = []
    drop_count = 0
    mark_lines = []
    waffle_plates = 0
    platters = 0
    plates = 0
    bowls = 0
    total = 0.0

    for seat_num, guest in enumerate(data['guests'], 1):
        seat_mark = []

        # --- Waffles ---
        waffle_data = guest.get('waffles', {})
        flavor = waffle_data.get('flavor', '')
        count = waffle_data.get('qty', 0)

        if flavor and count > 0:
            waffle_plates += count
            seat_mark.append(f"{count} {flavor.replace('_', ' ')} waffle{'s' if count > 1 else ''}")
            total += 4.00 * count
            if flavor in ['pecan', 'chocolate_chip', 'peanut_butter', 'blueberry']:
                total += 0.50 * count

        # --- Eggs ---
        egg = guest.get('eggs')
        if egg and egg != 'none':
            seat_mark.append(egg.replace('_', ' '))
            if 'cheese' in egg:
                total += 0.50

        # --- Toast ---
        toast = guest.get('toast')
        if toast and toast not in ['white', 'none', '']:
            seat_mark.append(f"{toast} toast")

        # --- Meat / Pull ---
        meat = guest.get('meat')
        if meat and meat != 'none':
            pull_items.append(meat)

        # --- Hashbrowns ---
        hashbrowns = guest.get('hashbrowns')
        if hashbrowns and hashbrowns != 'none':
            drop_count += 1
            seat_mark.append(f"{hashbrowns} hashbrowns")
            mods = guest.get('hashbrownMods', [])
            for mod in mods:
                seat_mark.append(mod)
                total += 0.50

        # --- Grits Bowl ---
        if guest.get('gritsBowl') and guest['gritsBowl'] != 'none':
            bowls += 1
            meat = guest['gritsBowl']
            pull_items.append(meat)
            seat_mark.append(f"grits bowl with {meat}")
            total += 4.00

        # --- Sandwich ---
        sandwich = guest.get('sandwich')
        if sandwich and sandwich != 'none':
            seat_mark.append(f"{sandwich.replace('_', ' ')} sandwich")
            total += 4.00

        # --- Drink ---
        drink = guest.get('beverage')
        if drink and drink != 'none':
            seat_mark.append(drink.replace('_', ' '))
            total += 2.00

        # --- Platter logic (meat + egg + toast) ---
        if meat and meat != 'none' and egg and egg != 'none' and toast and toast not in ['none', '', 'white']:
            platters += 1
            seat_mark.insert(0, 'platter')

        mark_lines.append(f"seat {seat_num}: " + ", ".join(seat_mark))

    # --- Pull / Drop / Mark construction ---
    pull = sorted(set(pull_items))
    drop = [f"drop {drop_count} hashbrowns scattered"] if drop_count else []

    plate_summary = []
    if platters: plate_summary.append(f"{platters} platter{'s' if platters > 1 else ''}")
    if plates: plate_summary.append(f"{plates} plate{'s' if plates > 1 else ''}")
    if waffle_plates: plate_summary.append(f"{waffle_plates} waffle plate{'s' if waffle_plates > 1 else ''}")
    if bowls: plate_summary.append(f"{bowls} bowl{'s' if bowls > 1 else ''}")

    mark = ["mark"]
    if plate_summary:
        mark[0] += " " + ", ".join(plate_summary)
    mark += mark_lines

    return {
        'pull': pull,
        'drop': drop,
        'mark': mark,
        'total': round(total, 2)
    }

