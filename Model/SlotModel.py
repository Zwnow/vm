class Slot:
    def __init__(self, drink, capacity):
        self.drink = drink
        self.capacity = capacity

    def __str__(self):
        return f'{self.drink.__str__()} Restbestand: {self.capacity}'