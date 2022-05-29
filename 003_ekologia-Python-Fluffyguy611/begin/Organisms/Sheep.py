from .Animal import Animal


class Sheep(Animal):

    def __init__(self, sheep=None, position=None, world=None):
        super(Sheep, self).__init__(sheep, position, world)

    def clone(self):
        return Sheep(self, None, None)

    def initParams(self):
        self.power = 3
        self.initiative = 3
        self.liveLength = 10
        self.powerToReproduce = 6
        self.eating = 5
        self.diet = 'p'
        self.isDietFor = 'm'
        self.sign = 'S'
        self.escape = 1

    def getNeighboringPosition(self):
        return self.world.filterPositionsWithoutAnimals(self.world.getNeighboringPositions(self.position))

    def getAttackPosition(self):
        return self.world.filterPositionsWithOrganism(self.world.getNeighboringPositions(self.position))

    def getPredatorPosition(self):
        return self.world.filterPositionsWithOrganism(self.world.getNeighboringPositions(self.position))

    def __eq__(self, other):
        if isinstance(other, Sheep):
            return self.sign == other.sign
        return False
