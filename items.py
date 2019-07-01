from enum import Enum


class Item():

    def __init__(self):
        self.name = ""
        self.value = 0
        self.weight = 0

    def setName(self, Name):
        self.name = Name

    def getName(self):
        return self.name

    def setValue(self, Value):
        self.value = Value

    def increaseValue(self, multiplier):
        self.value *= multiplier

    def getBuyValue(self):
        return self.value

    def getSellValue(self):
        return self.value * 0.4

    def setWeight(self, value):
        self.weight = value

    def getWeight(self):
        return self.weight


class WeaponType(Enum):
    StraightSword = 1
    CurvedSword = 2
    GreatSword = 3
    Axe = 4
    GreatAxe = 5
    Hammer = 6
    GreatHammer = 7
    Club = 8
    Spear = 9
    Bow = 10
    NoWeapon = 11


class DamageType(Enum):
    Normal = 1
    Fire = 2
    Frost = 3
    Lightning = 4
    Poison = 5
    Necrotic = 6
    Divine = 7
    NoDamage = 8


class Weapon(Item):

    def __init__(self):
        self.weapon_type = WeaponType.NoWeapon
        self.damage_type = DamageType.NoDamage
        self.attack_damage = 0
        self.attack_speed = 0
        self.upgrade_level = 1
        self.upgrade_multiplier = 1
        self.upgrade_cost = 100

    def setDamage(self, value):
        if self.attack_damage == 0:
            self.attack_damage += value * self.upgrade_multiplier
        else:
            self.attack_damage *= self.upgrade_multiplier

    def getDamage(self):
        return self.attack_damage

    def setSpeed(self, value):
        self.attack_speed += value

    def getSpeed(self):
        return self.attack_speed

    def setWeaponType(self, Type):
        self.weapon_type = Type

    def getWeaponType(self):
        return self.weapon_type.name

    def setDamageType(self, Type):
        self.damage_type = Type

    def getDamageType(self):
        return self.damage_type.name

    def upgrade(self):
        self.upgrade_level += 1
        self.upgrade_multiplier += .25
        self.upgrade_cost += self.upgrade_cost * 1.5
        self.setDamage(self.attack_damage)
        self.increaseValue(self.upgrade_multiplier)

    def getUpgradeLevel(self):
        return self.upgrade_level

    def getUpgradeCost(self):
        return self.upgrade_cost


class ArmourType(Enum):
    Head = 1
    Chest = 2
    Hand = 3
    Leg = 4
    Foot = 5
    NoArmour = 6


class ArmourMat(Enum):
    Cloth = 1
    Leather = 1.25
    Iron = 1.5
    Steel = 1.75
    Ebony = 2
    NoArmour = 0


class Armour(Item):

    def __init__(self):
        self.armour_value = 0
        self.max_durability = 0
        self.current_durability = 0
        self.bonuses = {
            "hp": 0,
            "mp": 0,
            "str": 0,
            "dex": 0,
            "con": 0,
            "int": 0,
            "wis": 0,
            "cha": 0
        }
        self.armour_type = ArmourType.NoArmour
        self.armour_mat = ArmourMat.NoArmour
        self.upgrade_level = 1
        self.upgrade_multiplier = 1
        self.upgrade_cost = 100

    def setBonus(self, stat, value):
        self.bonuses[stat] += value

    def getBonus(self, stat):
        return self.bonuses.get(stat)

    def setArmourValue(self, value):
        if self.armour_value == 0:
            self.armour_value += value * self.upgrade_multiplier
        else:
            self.armour_value *= self.upgrade_multiplier

    def getArmourValue(self):
        return self.armour_value

    def setInitialDurability(self, value):
        self.max_durability = value
        self.current_durability = value

    def getMaxDurability(self):
        return self.max_durability

    def getCurrentDurability(self):
        return self.current_durability

    def upgrade(self):
        self.upgrade_level += 1
        self.upgrade_multiplier += .25
        self.upgrade_cost += self.upgrade_cost * 1.5
        self.setArmourValue(self.armour_value)
        self.increaseValue(self.upgrade_multiplier)

    def setArmourType(self, Type):
        self.armour_type = Type

    def getArmourType(self):
        return self.armour_type

    def setArmourMat(self, Mat):
        self.armour_mat = Mat

    def getArmourMat(self):
        return self.armour_mat
