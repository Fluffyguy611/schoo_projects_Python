from Position import Position
from Organisms.Plant import Plant
from Organisms.Animal import Animal
from Action import Action
from ActionEnum import ActionEnum


class World(object):

    def __init__(self, worldX, worldY):
        self.__worldX = worldX
        self.__worldY = worldY
        self.__turn = 0
        self.__organisms = []
        self.__newOrganisms = []
        self.__AllOrganisms = []
        self.__separator = '.'
        self.__plague_turn = 0
        self.__plague_on = False

    @property
    def worldX(self):
        return self.__worldX

    @property
    def worldY(self):
        return self.__worldY

    @property
    def turn(self):
        return self.__turn

    @turn.setter
    def turn(self, value):
        self.__turn = value

    @property
    def organisms(self):
        return self.__organisms

    @organisms.setter
    def organisms(self, value):
        self.__organisms = value

    @property
    def newOrganisms(self):
        return self.__newOrganisms

    @newOrganisms.setter
    def newOrganisms(self, value):
        self.__newOrganisms = value

    @property
    def AllOrganisms(self):
        return self.__AllOrganisms

    @AllOrganisms.setter
    def AllOrganisms(self, value):
        self.__AllOrganisms = value

    @property
    def separator(self):
        return self.__separator

    @property
    def plague_turn(self):
        return self.__plague_turn

    @plague_turn.setter
    def plague_turn(self, value):
        self.__plague_turn = value

    def makeTurn(self):
        actions = []

        for org in self.organisms:
            if self.positionOnBoard(org.position):
                actions = org.move()
                for a in actions:
                    self.makeMove(a)
                actions = []
                if self.positionOnBoard(org.position):
                    actions = org.action()
                    for a in actions:
                        self.makeMove(a)
                    actions = []
        self.organisms = [o for o in self.organisms if self.positionOnBoard(o.position)]
        for o in self.organisms:
            o.liveLength -= 1
            o.power += 1
            o.eating -= 1
            if o.eating < 1:
                o.liveLength = 0
            if o.liveLength < 1:
                print(str(o.__class__.__name__) + ': died of old age at: ' + str(o.position))
        self.organisms = [o for o in self.organisms if o.liveLength > 0]
        self.newOrganisms = [o for o in self.newOrganisms if self.positionOnBoard(o.position)]
        self.organisms.extend(self.newOrganisms)
        self.organisms.sort(key=lambda o: o.initiative, reverse=True)
        self.newOrganisms = []

        self.turn += 1

    def isPlague(self):
        result = None
        if self.plague_turn < 2:
            result = True
        else:
            result = False
        return result

    def plague(self, userinput=0):
        if userinput == '1' and self.isPlague() or self.plague_turn >= 1 and self.isPlague():
            self.organisms = [o for o in self.organisms if self.positionOnBoard(o.position)]
            for o in self.organisms:
                o.liveLength = o.liveLength // 2
            self.plague_turn += 1
            self.__plague_on = True
        else:
            self.__plague_on = False

    def user_add_org(self, userinput=0):
        for o in self.AllOrganisms:
            if userinput == o.sign:
                result = self.user_input()
                newOrg = o.__class__(position=Position(xPosition=result[0], yPosition=result[1]), world=self)
                if self.positionOnBoard(newOrg.position) and self.getOrganismFromPosition(newOrg.position) is None:
                    self.addOrganism(newOrg)
                    self.OrganismLegend(newOrg)
                break

    @staticmethod
    def user_input(x=-1, y=-1):
        print(str('Enter coordinates'))
        while True:
            try:
                x = int(input('x: '))
                y = int(input('y: '))
            except ValueError:
                print("Not an integer! Please enter an integer.")
                continue
            else:
                break
        result = [x, y]
        return result

    #	def makeMove_dictionary(self, action):
    #		choice = {
    #			0: action.position,
    #			2: self.newOrganisms.append(action.organism),
    #			3: action.organism.initiative+action.value and action.organism.power+action.value,
    #			2:
    ##		}

    def makeMove(self, action):
        print(action)
        if action.action == ActionEnum.A_ADD:
            self.newOrganisms.append(action.organism)
        elif action.action == ActionEnum.A_INCREASEPOWER:
            action.organism.initiative += action.value
            action.organism.power += action.value
        elif action.action == ActionEnum.A_MOVE:
            action.organism.position = action.position
        elif action.action == ActionEnum.A_ESCAPE:
            action.organism.position = action.position
        elif action.action == ActionEnum.A_REMOVE:
            action.organism.position = Position(xPosition=-1, yPosition=-1)
        elif action.action == ActionEnum.A_EAT:
            action.organism.eating = action.value

    def addOrganism(self, newOrganism):
        newOrgPosition = Position(xPosition=newOrganism.position.x, yPosition=newOrganism.position.y)
        if self.positionOnBoard(newOrgPosition):
            self.organisms.append(newOrganism)
            self.organisms.sort(key=lambda org: org.initiative, reverse=True)
            return True
        return False

    def OrganismLegend(self, newOrg):
        if self.isOrganism(newOrg):
            self.AllOrganisms.append(newOrg)
            self.AllOrganisms.sort(key=lambda org: org.initiative, reverse=True)
            return True
        return False

    def isOrganism(self, organism):
        for o in self.__AllOrganisms:
            if o.sign == organism.sign:
                return False
        return True

    def positionOnBoard(self, position):
        return position.x >= 0 and position.y >= 0 and position.x < self.worldX and position.y < self.worldY

    def getOrganismFromPosition(self, position):
        pomOrganism = None

        for org in self.organisms:
            if org.position == position:
                pomOrganism = org
                break
        if pomOrganism is None:
            for org in self.newOrganisms:
                if org.position == position:
                    pomOrganism = org
                    break
        return pomOrganism

    def getNeighboringPositions(self, position):
        result = []
        pomPosition = None

        for y in range(-1, 2):
            for x in range(-1, 2):
                pomPosition = Position(xPosition=position.x + x, yPosition=position.y + y)
                if self.positionOnBoard(pomPosition) and not (y == 0 and x == 0):
                    result.append(pomPosition)
        return result

    def filterFreePositions(self, fields):
        result = []

        for field in fields:
            if self.getOrganismFromPosition(field) is None:
                result.append(field)
        return result

    def filterPositionsWithoutAnimals(self, fields):
        result = []
        pomOrg = None

        for filed in fields:
            pomOrg = self.getOrganismFromPosition(filed)
            if pomOrg is None or isinstance(pomOrg, Plant):
                result.append(filed)
        return result

    def filterPositionsWithOrganism(self, fields):
        result = []
        pomOrg = None
        for filed in fields:
            pomOrg = self.getOrganismFromPosition(filed)
            if pomOrg is not None:
                result.append(pomOrg)
        return result

    def getEscapePosition(self, position, defeningOrg):
        result = None
        pomPosition = None
        x = (position.x - defeningOrg.x) * -2
        y = (position.y - defeningOrg.y) * -2
        if position:
            pomPosition = Position(xPosition=defeningOrg.x + x, yPosition=defeningOrg.y + y)
            if self.positionOnBoard(pomPosition) and (self.getOrganismFromPosition(pomPosition) is None or Plant):
                result = pomPosition
        return result

    def __str__(self):
        result = '\nturn: ' + str(self.__turn) + '\n'
        if self.__plague_on:
            print(str('\nPlague is intiated, plague has been ongoing for: '
                      + str(self.plague_turn) + ' turns' + '\n'))
        for wY in range(0, self.worldY):
            for wX in range(0, self.worldX):
                org = self.getOrganismFromPosition(Position(xPosition=wX, yPosition=wY))
                if org:
                    result += str(org.sign)
                else:
                    result += self.separator
            result += '\n'
        return result
