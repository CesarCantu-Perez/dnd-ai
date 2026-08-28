class Character:

    def __init__(
        self,
        name,
        race,
        character_class,
        level,
        max_hp,
        armor_class,
        strength,
        dexterity,
        constitution,
        intelligence,
        wisdom,
        charisma
    ):
        self.name = name
        self.race = race
        self.character_class = character_class
        self.level = level
        self.max_hp = max_hp
        self.hp = max_hp
        self.armor_class = armor_class
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

    def get_summary(self):
        return(
            f"Name: {self.name}\n"
            f"Race: {self.race}\n"
            f"Class: {self.character_class}\n"
            f"Level: {self.level}\n"
            f"HP: {self.hp}/{self.max_hp}\n"
            f"AC: {self.armor_class}\n"
            f"Strength: {self.strength}\n"
            f"Dexterity: {self.dexterity}\n"
            f"Constitution: {self.constitution}\n"
            f"Intelligence: {self.intelligence}\n"
            f"Wisdom: {self.wisdom}\n"
            f"Charisma: {self.charisma}"
        )
