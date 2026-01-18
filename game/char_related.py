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
            "base_attack": 0,
            "base_defense": 0,
            "crit_chance": 5,
        },
        "creation": datetime.now().strftime("%Y-%m-%d [%H:%M]"),
    }
    return sheet
