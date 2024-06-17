from Model.VendingMachineModel import VendingMachine
from Views.IndexView import IndexView
from Views.PayDrinkView import PayDrinkView 
from Views.ErrorView import ErrorView

class VendingMachineController:
    def __init__(self):
        self.vending_machine = VendingMachine()
    # Views
    def index(self):
        selection = IndexView(self.vending_machine.drinkslots)
        return selection
    
    def pay_drink(self, drink):
        payment = PayDrinkView(drink)
        return payment
    
    # Controls
    def get_drink(self, id):
        for slot in self.vending_machine.drinkslots:
            if slot.drink.id == id and slot.capacity != 0:
                return slot.drink
        ErrorView('Das Getränk wurde leider nicht gefunden oder ist ausverkauft.')
        quit()

    def add_to_cash_register(self, payment):
        self.vending_machine.cash_register += payment

    def remove_drink(self, drink):
        self.vending_machine.drinkslots[drink.id - 1].capacity -= 1
    
    def get_cash_register(self):
        return self.vending_machine.cash_register
        