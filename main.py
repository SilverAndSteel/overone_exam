from tomato_bush import TomatoBush
from gardener import Gardener


if __name__ == '__main__':
    bush = TomatoBush(5)
    gard = Gardener("Tom", bush)
    gard.work()
    gard.harvest()
    gard.work()
    gard.harvest()
