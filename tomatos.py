
class Tomato:

    states = {
        1: "Green tomatoes",
        2: "Yellow tomatoes",
        3: "Red tomatoes"
    }

    def __init__(self, index, state=1):

        self._index = index
        self._state = state

    def grow(self):
        if self._state < 3:
            self._state += 1
        print(f"Tomato {self._index} is {Tomato.states[self._state]}")

    def is_ripe(self):
        if self._state == 3:
            return True
        return False



