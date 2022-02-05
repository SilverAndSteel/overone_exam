from tomatos import Tomato


class TomatoBush:
    def __init__(self, quantity):
        self.tomatoes = [Tomato(index) for index in range(0, quantity)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        return self.tomatoes.clear()

