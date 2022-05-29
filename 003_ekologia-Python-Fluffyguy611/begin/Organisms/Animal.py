from .Organism import Organism
from Action import Action
from ActionEnum import ActionEnum
import random


class Animal(Organism):

    def __init__(self, animal=None, position=None, world=None):
        super(Animal, self).__init__(animal, position, world)
        self.__lastPosition = position

    @property
    def lastPosition(self):
        return self.__lastPosition

    @lastPosition.setter
    def lastPosition(self, value):
        self.__lastPosition = value

    def move(self):
        result = []
        attackPositions = None
        defendPositions = None
        newPosition = None
        movePos = None
        attackPositions = self.attack()
        defendPositions = self.defend()
        movePos = self.movePos()
        if attackPositions:
            result = attackPositions
        elif defendPositions:
            result = defendPositions
        else:
            result = movePos
        return result

    def action(self):
        result = []
        newAnimal = None
        birthPositions = self.getNeighboringBirthPosition()

        if self.ifReproduce() and birthPositions:
            newAnimalPosition = random.choice(birthPositions)
            newAnimal = self.clone()
            newAnimal.initParams()
            newAnimal.position = newAnimalPosition
            self.power = self.power / 2
            result.append(Action(ActionEnum.A_ADD, newAnimalPosition, 0, newAnimal))
        return result

    def attack(self):
        result = []
        attackPositions = self.getAttackPostion()
        attackPos = None
        AttackedOrg = None
        for atack in attackPositions:
            if self.isHungry() and atack:
                AttackPos = atack.position
                AttackedOrg = self.world.getOrganismFromPosition(AttackPos)
                if self.AttackOrganism(AttackedOrg):
                    Attack = AttackPos
                    result.append(Action(ActionEnum.A_MOVE, Attack, 0, self))
                    result.extend(AttackedOrg.consequences(self))
                    self.lastPosition = self.position
                    break
            else:
                continue
        return result

    def defend(self):
        result = []
        predators = self.getPredatorPosition()
        for pre in predators:
            if pre is not None:
                predator = pre
                if self.isAbleToEscape(predator) and predator.AttackOrganism(self):
                    pomPosition = self.world.getEscapePosition(predator.position, self.position)
                    if pomPosition:
                        Org = self.world.getOrganismFromPosition(pomPosition)
                        result.append(Action(ActionEnum.A_ESCAPE, pomPosition, 0, self))
                        self.lastPosition = self.position
                        if Org is not None:
                            result.extend(Org.consequences(self))
                        break
            else:
                continue
        return result

    def movePos(self):
        result = []
        organismPositions = self.getNeighboringPosition()
        if organismPositions:
            newPosition = random.choice(organismPositions)
            result.append(Action(ActionEnum.A_MOVE, newPosition, 0, self))
            self.lastPosition = self.position
            metOrganism = self.world.getOrganismFromPosition(newPosition)
            if metOrganism is not None:
                result.extend(metOrganism.consequences(self))
        return result

    def getNeighboringPosition(self):
        return self.world.getNeighboringPositions(self.position)

    def getNeighboringBirthPosition(self):
        return self.world.filterFreePositions(self.world.getNeighboringPositions(self.position))

    def getAttackPostion(self):
        return self.world.filterPositionsWithOrganism(self.world.getNeighboringPositions(self.position))

    def getPredatorPosition(self):
        return self.world.filterPositionsWithOrganism(self.world.getNeighboringPositions(self.position))

