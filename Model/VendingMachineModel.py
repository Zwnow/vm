from Model.DrinkModel import Drink
from Model.SlotModel import Slot

class VendingMachine:
    def __init__(self):
        self.drinkslots = [
            Slot(Drink(1, 'Cola', 1.45), 20),
            Slot(Drink(2, 'Wasser', 1.20), 20),
            Slot(Drink(3, 'Bier', 1.50), 20),
            Slot(Drink(4, 'Kaffee', 1.65), 20),
            Slot(Drink(5, 'En lüdde en', 1.00), 100),
        ]
        self.capacity = sum(slot.capacity for slot in self.drinkslots)
        self.cash_register = 0