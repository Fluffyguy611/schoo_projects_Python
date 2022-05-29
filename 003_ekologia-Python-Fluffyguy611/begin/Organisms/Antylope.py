from .Animal import Animal


class Antylope(Animal):

    def __init__(self, antylope=None, position=None, world=None):
        super(Antylope, self).__init__(antylope, position, world)

    def clone(self):
        return Antylope(self, None, None)

    def initParams(self):
        self.power = 4
        self.initiative = 3
        self.liveLength = 11
        self.powerToReproduce = 7
        self.eating = 5
        self.diet = 'p'
        self.isDietFor = 'm'
        self.sign = 'A'
        self.escape = 2

    def getNeighboringPosition(self):
        return self.world.filterPositionsWithoutAnimals(self.world.getNeighboringPositions(self.position))

    def getAttackPosition(self):
        return self.world.filterPositionsWithOrganism(self.world.getNeighboringPositions(self.position))

    def getPredatorPosition(self):
        return self.world.filterPositionsWithOrganism(self.world.getNeighboringPositions(self.position))

    def __eq__(self, other):
        if isinstance(other, Antylope):
            return self.sign == other.sign
        return False
