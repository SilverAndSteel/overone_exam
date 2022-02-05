from tomato_bush import TomatoBush


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print("Gardener is working.")
        self._plant.grow_all()
        print("Gardener stop working.")

    def harvest(self):
        print("Gardener is harvesting...")
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Harvesting is finished!")
        else:
            print("Too early! Your plant is green and not ripe.")

    @staticmethod
    def knowledge_base():
        print("Use all what you know about gardens)")
