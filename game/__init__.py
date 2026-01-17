class Game:
    available_classes = ["ranger", "fighter", "mage"]
    available_alignments = [
        "sun-born",
        "night-blessed",
        "stars-gazer",
        "land-dweller",
        "sea-voyager",
        "sky-dreamer",
    ]

    from .char_related import validate_creation
