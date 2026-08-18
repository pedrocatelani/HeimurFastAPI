from datetime import datetime


def validate_creation(self, atr: dict, specs: dict) -> bool:
    validate_atributes = atr.total
    if validate_atributes != 15:
        return False

    if specs.char_class not in self.available_classes:
        return False

    if specs.char_alignment not in self.available_alignments:
        return False

    return True


def generate_char_sheet(self, atr: dict, specs: dict):
    hp_calc = (
        3 * atr.constitution
        + self.bonus_health_map[specs.char_class]
        + self.bonus_health_map[specs.char_alignment]
    )

    mana_calc = (
        2 * atr.intelligence
        + self.bonus_mana_map[specs.char_class]
        + self.bonus_mana_map[specs.char_alignment]
    )

    sheet = {
        "atr": atr.model_dump(),
        "specs": specs.model_dump(),
        "status": {
            "max_hp": hp_calc,
            "current_hp": hp_calc,
            "max_mana": mana_calc,
            "current_mana": mana_calc,
            "max_stance": 0,
            "current_stance": 0,
            "base_attack": 0,
            "base_defense": 0,
            "crit_chance": 5,
            "crit_mult": 1.5,
            "elemental_strike": 1.25,
            "craft_discount": 0,
            "harvest_bonus": 0,
            "damage_resistance": 0,
        },
        "creation": datetime.now().strftime("%Y-%m-%d [%H:%M]"),
    }

    sheet = add_alignments_bonus(sheet)
    return sheet


def add_alignments_bonus(sheet: dict) -> dict:
    """This function is dumb. If you know how to optimize it, please let me know."""
    path = sheet["specs"]["char_alignment"]
    if path == "sun-born":
        sheet["status"]["elemental_strike"] += 0.15
    if path == "moon-blessed":
        sheet["atr"]["charisma"] += 2
    if path == "stars-gazer":
        sheet["status"]["base_attack"] += 2
        sheet["status"]["crit_mult"] += 0.5
    if path == "land-dweller":
        sheet["status"]["craft_discount"] += 1
        sheet["status"]["harvest_bonus"] += 2
    if path == "sea-voyager":
        sheet["atr"]["dexterity"] += 2
        sheet["status"]["crit_chance"] += 5
    if path == "sky-dreamer":
        sheet["status"]["base_defense"] += 2
        sheet["status"]["damage_resistance"] += 2

    sheet["status"]["max_stance"] = (
        sheet["atr"]["constitution"] / 2 + sheet["atr"]["intelligence"] / 2
    )
    sheet["status"]["current_stance"] = sheet["status"]["max_stance"]

    return sheet
