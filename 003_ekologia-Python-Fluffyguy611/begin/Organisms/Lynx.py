from .Animal import Animal


class Lynx(Animal):

    def __init__(self, lynx=None, position=None, world=None):
        super(Lynx, self).__init__(lynx, position, world)

    def clone(self):
        return Lynx(self, None, None)

    def initParams(self):
        self.power = 6
        self.initiative = 5
        self.liveLength = 18
        self.powerToReproduce = 14
        self.eating = 13
        self.diet = 'm'
        self.isDietFor = 'pm'
        self.sign = 'R'
        self.escape = 1

    def getNeighboringPosition(self):
        return self.world.filterPositionsWithoutAnimals(self.world.getNeighboringPositions(self.position))

    def getAttackPosition(self):
        return self.world.filterPostionWithAnimals(self.world.getNeighboringPositions(self.position))

    def getPredatorPosition(self):
        return self.world.filterPositionsWithOrganism(self.world.getNeighboringPositions(self.position))

    def __eq__(self, other):
        if isinstance(other, Lynx):
            return self.sign == other.sign
        return False
