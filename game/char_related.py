def validate_creation(self, atr: dict, specs: dict) -> bool:
    validate_atributes = sum(atr.values())
    if validate_atributes != 15:
        return False

    if specs["char_class"] not in self.available_classes:
        return False

    if specs["char_alignment"] not in self.available_alignments:
        return False

    return True
