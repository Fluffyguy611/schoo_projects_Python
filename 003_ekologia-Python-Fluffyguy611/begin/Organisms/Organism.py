from abc import ABC, abstractmethod
from Position import Position
from Action import Action
from ActionEnum import ActionEnum


class Organism(ABC):

	def __init__(self, organism, position, world):
		self.__power = None
		self.__initiative = None
		self.__position = None
		self.__liveLength = None
		self.__powerToReproduce = None
		self.__eating = None
		self.__sign = None
		self.__world = None
		self.__diet = None
		self.__isDietFor = None
		self.__escape = None

		if organism is not None:
			self.__power = organism.power
			self.__initiative = organism.initiative
			self.__position = organism.position
			self.__liveLength = organism.liveLength
			self.__powerToReproduce = organism.powerToReproduce
			self.__eating = organism.eating
			self.__sign = organism.sign
			self.__world = organism.__world
			self.__diet = organism.__diet
			self.__isDietFor = organism.__isDietFor
			self.__escape = organism.__escape
		else:
			if position is not None:
				self.__position = position
			if world is not None:
				self.__world = world
			self.initParams()


	@property
	def power(self):
		return self.__power

	@power.setter
	def power(self, value):
		self.__power = value

	@property
	def initiative(self):
		return self.__initiative

	@initiative.setter
	def initiative(self, value):
		self.__initiative = value

	@property
	def position(self):
		return self.__position

	@position.setter
	def position(self, value):
		self.__position = value

	@property
	def liveLength(self):
		return self.__liveLength

	@liveLength.setter
	def liveLength(self, value):
		self.__liveLength = value

	@property
	def powerToReproduce(self):
		return self.__powerToReproduce

	@powerToReproduce.setter
	def powerToReproduce(self, value):
		self.__powerToReproduce = value

	@property
	def eating(self):
		return self.__eating

	@eating.setter
	def eating(self, value):
		self.__eating = value

	@property
	def diet(self):
		return self.__diet

	@diet.setter
	def diet(self, value):
		self.__diet = value

	@property
	def isDietFor(self):
		return self.__isDietFor

	@isDietFor.setter
	def isDietFor(self, value):
		self.__isDietFor = value

	@property
	def escape(self):
		return self.__escape

	@escape.setter
	def escape(self, value):
		self.__escape = value

	@property
	def sign(self):
		return self.__sign

	@sign.setter
	def sign(self, value):
		self.__sign = value

	@property
	def world(self):
		return self.__world

	@world.setter
	def world(self, value):
		self.__world = value

	@abstractmethod
	def move(self):
		pass

	@abstractmethod
	def action(self):
		pass

	@abstractmethod
	def initParams(self):
		pass

	@abstractmethod
	def clone(self):
		pass

	def consequences(self, atackingOrganism):
		result = []
		increse = 2
		if atackingOrganism.diet == self.isDietFor and atackingOrganism.sign != self.sign:
			if self.initiative > atackingOrganism.initiative:
				result.append(Action(ActionEnum.A_REMOVE, Position(xPosition=-1, yPosition=-1), 0, atackingOrganism))
				result.append(Action(ActionEnum.A_INCREASEPOWER, 0, increse, self))
				result.append(Action(ActionEnum.A_EAT, 0, self.__eating, self))
			else:
				result.append(Action(ActionEnum.A_REMOVE, Position(xPosition=-1, yPosition=-1), 0, self))
				result.append(Action(ActionEnum.A_INCREASEPOWER, 0, increse, atackingOrganism))
				result.append(Action(ActionEnum.A_EAT, 0, atackingOrganism.__eating, atackingOrganism))

		else:
			if self.initiative > atackingOrganism.initiative:
				result.append(Action(ActionEnum.A_REMOVE, Position(xPosition=-1, yPosition=-1), 0, atackingOrganism))
			else:
				result.append(Action(ActionEnum.A_REMOVE, Position(xPosition=-1, yPosition=-1), 0, self))
		return result

	def ifReproduce(self):
		result = False

		if self.power >= self.powerToReproduce:
			result = True
		return result

	def AttackOrganism(self, attackedOrganism):
		result = False
		if self.diet == attackedOrganism.isDietFor:
			result = True
		return result

	def isHungry(self):
		result = False
		if self.eating <= 4:
			result = True

		return result

	def isAbleToEscape(self, attackingOrganism):
		result = False
		if self.escape > attackingOrganism.escape:
			result = True
		return result

	def __str__(self):
		return '{0}: power: {1} initiative: {2} liveLength {3} eating {4} position: {5}'\
				.format(self.__class__.__name__, self.power, self.initiative, self.liveLength, self.eating, self.position)

	def __eq__(self, other):
		return self.action == other.action
