from World import World
from Position import Position
from Organisms.Grass import Grass
from Organisms.Sheep import Sheep
from Organisms.Lynx import Lynx
from Organisms.Antylope import Antylope
import os


if __name__ == '__main__':
	pyWorld = World(10, 10)

	newOrg = Grass(position=Position(xPosition=9, yPosition=9), world=pyWorld)
	pyWorld.addOrganism(newOrg)
	pyWorld.OrganismLegend(newOrg)

	newOrg = Grass(position=Position(xPosition=1, yPosition=1), world=pyWorld)
	pyWorld.OrganismLegend(newOrg)

	newOrg = Grass(position=Position(xPosition=9, yPosition=1), world=pyWorld)
	pyWorld.addOrganism(newOrg)
	pyWorld.OrganismLegend(newOrg)

	newOrg = Sheep(position=Position(xPosition=2, yPosition=2), world=pyWorld)
	pyWorld.addOrganism(newOrg)
	pyWorld.OrganismLegend(newOrg)

	newOrg = Sheep(position=Position(xPosition=3, yPosition=4), world=pyWorld)
	pyWorld.addOrganism(newOrg)
	pyWorld.OrganismLegend(newOrg)

	newOrg = Lynx(position=Position(xPosition=3, yPosition=5), world=pyWorld)
	pyWorld.addOrganism(newOrg)
	pyWorld.OrganismLegend(newOrg)

	newOrg = Antylope(position=Position(xPosition=4, yPosition=4), world=pyWorld)
	pyWorld.addOrganism(newOrg)
	pyWorld.OrganismLegend(newOrg)

	newOrg = Antylope(position=Position(xPosition=7, yPosition=3), world=pyWorld)
	pyWorld.addOrganism(newOrg)
	pyWorld.OrganismLegend(newOrg)

	print(pyWorld)
	print('To init plague, press 1')

	for _ in range(0, 50):
		user = input('')
		os.system('cls')
		pyWorld.user_add_org(user)
		pyWorld.makeTurn()
		pyWorld.plague(user)
		print(pyWorld)
