from armour import *
from items import ArmourType, WeaponType
from uuid import *


class Slot():

    def __init__(self):
        self.is_full = False
        self.item = None

    def getIsFull(self):
        return self.is_full

    def fillSlot(self, Item):
        self.is_full = True
        self.item = Item

    def emptySlot(self):
        self.is_full = False

    def getItem(self):
        return self.item.getName()


class Inventory():

    def __init__(self):
        self.items_in_bag = []
        self.max_weight = 150
        self.current_weight = 0
        self.head_slot = Slot()
        self.chest_slot = Slot()
        self.hand_slot = Slot()
        self.leg_slot = Slot()
        self.foot_slot = Slot()
        self.l_hand_slot = Slot()
        self.r_hand_slot = Slot()

    def addItem(self, item):
        if self.current_weight + item.getWeight() <= self.max_weight:
            self.items_in_bag.append(item)
        else:
            print("You're carrying too much weight!")

    def removeItem(self, item):
        self.items_in_bag.remove(item)

    def fillHeadSlot(self, armour):
        if armour in self.items_in_bag and self.head_slot.getIsFull() == False \
                and armour.getArmourType() == ArmourType.Head:
            self.head_slot.fillSlot(armour)
        elif armour in self.items_in_bag and self.head_slot.getIsFull() == True \
                and armour.getArmourType() == Armourtype.Head:
            self.head_slot.emptySlot()
            self.head_slot.fillSlot(armour)

    def getHeadSlot(self):
        if self.head_slot.getIsFull() == True:
            print("Your head slot is currently occupied by the {}".format(
                self.head_slot.getItem()))

    def fillChestSlot(self, armour):
        if armour in self.items_in_bag and self.chest_slot.getIsFull() == False \
                and armour.getArmourType() == ArmourType.Chest:
            self.chest_slot.fillSlot(armour)

    def getChestSlot()
