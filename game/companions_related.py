# Primus, Secondus, Thertios, Tetraon, Pentillon
# Everyone is available during Pentillon.
companions_routine = {
    "Marshall": {
        "days": ["Primus", "Thertios"],
        "period": "eevening",
        "first_cicle": 1,
        "dungeon": None,
    },
    "Joseph": {
        "days": ["Secondus"],
        "period": "morning",
        "first_cicle": 1,
        "dungeon": None,
    },
    "Lyra": {
        "days": ["Thertios", "Tetraon"],
        "period": "afternoon",
        "first_cicle": 1,
        "dungeon": None,
    },
}


def see_available_hangouts(self, infos):
    day = infos.current_week_day.capitalize()
    period = infos.current_period.lower()
    dungeon = infos.current_dungeon.lower()
    cicle = infos.current_cicle
    hangouts = []

    for name, c in companions_routine.items():
        if day in c["days"] or day == "Pentillon":
            if c["first_cicle"] <= cicle and period == c["period"]:
                hangouts.append(name)

    return hangouts
