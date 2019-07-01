from items import Armour, ArmourType, ArmourMat


class LeatherJerkin(Armour):

    def __init__(self):
        Armour.__init__(self)
        self.setName("Leather Jerkin")
        self.setValue(600)
        self.setWeight(5)
        self.setArmourValue(13)
        self.setInitialDurability(50)
        self.setArmourType(ArmourType.Chest)
        self.setArmourMat(ArmourMat.Leather)


class IronCap(Armour):

    def __init__(self):
        Armour.__init__(self)
        self.setName("Iron Cap")
        self.setValue(120)
        self.setWeight(2)
        self.setArmourValue(6)
        self.setInitialDurability(35)
        self.setArmourType(ArmourType.Head)
        self.setArmourMat(ArmourMat.Iron)
