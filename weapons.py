from items import Weapon, WeaponType, DamageType


class LongSword(Weapon):

    def __init__(self):
        Weapon.__init__(self)
        self.setName("Long Sword")
        self.setValue(200)
        self.setWeight(12)
        self.setDamage(20)
        self.setSpeed(6)
        self.setWeaponType(WeaponType.StraightSword)
        self.setDamageType(DamageType.Normal)


class BroadSword(Weapon):

    def __init__(self):
        Weapon.__init__(self)
        self.setName("Broad Sword")
        self.setValue(180)
        self.setWeight(11)
        self.setDamage(17)
        self.setSpeed(6)
        self.setWeaponType(WeaponType.StraightSword)
        self.setDamageType(DamageType.Normal)


class Rapier(Weapon):

    def __init__(self):
        Weapon.__init__(self)
        self.setName("Rapier")
        self.setValue(240)
        self.setWeight(9)
        self.setDamage(16)
        self.setSpeed(7)
        self.setWeaponType(WeaponType.StraightSword)
        self.setDamageType(DamageType.Normal)
