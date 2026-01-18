from typing import Dict, List
from pydantic import BaseModel


class Atributes(BaseModel):
    """Expects<br>
    strenght: int<br>
    intelligence: int<br>
    dexterity: int<br>
    constitution: int<br>
    charisma: int<br>
    """

    strenght: int
    intelligence: int
    dexterity: int
    constitution: int
    charisma: int

    @property
    def total(self) -> int:
        return sum(self.model_dump().values())


class CreateSpecs(BaseModel):
    """Expects<br>
    name: str<br>
    char_class: str<br>
    char_alignment: str<br>
    """

    name: str
    char_class: str
    char_alignment: str
