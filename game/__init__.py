class Game:
    available_classes = ["ranger", "fighter", "mage"]
    available_alignments = [
        "sun-born",
        "moon-blessed",
        "stars-gazer",
        "land-dweller",
        "sea-voyager",
        "sky-dreamer",
    ]
    bonus_health_map = {
        "ranger": 2,
        "fighter": 3,
        "mage": 1,
        "sun-born": 0,
        "moon-blessed": 0,
        "stars-gazer": 0,
        "land-dweller": 1,
        "sea-voyager": 1,
        "sky-dreamer": 2,
    }
    bonus_mana_map = {
        "ranger": 2,
        "fighter": 1,
        "mage": 3,
        "sun-born": 1,
        "moon-blessed": 2,
        "stars-gazer": 0,
        "land-dweller": 0,
        "sea-voyager": 0,
        "sky-dreamer": 0,
    }

    from .char_related import validate_creation, generate_char_sheet
    from .companions_related import see_available_hangouts
