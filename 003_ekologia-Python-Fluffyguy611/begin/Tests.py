import unittest
from World import World
from Position import Position
from Organisms.Organism import Organism
from Organisms.Grass import Grass
from Organisms.Sheep import Sheep
from Organisms.Lynx import Lynx
from Organisms.Antylope import Antylope
from Action import Action
from ActionEnum import ActionEnum
from unittest.mock import Mock
from unittest.mock import patch
from Organisms.Animal import Animal
import os


class EkologiaTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pyWorld = World(10, 10)
        Org_1 = Lynx(position=Position(xPosition=3, yPosition=4), world=pyWorld)
        Org_2 = Antylope(position=Position(xPosition=4, yPosition=4), world=pyWorld)

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.pyWorld = World(10, 10)
        self.Sheep = Sheep()
        self.Lynx = Lynx(position=Position(xPosition=3, yPosition=4), world=self.pyWorld)
        self.pyWorld.addOrganism(self.Lynx)
        self.Antypole = Antylope(position=Position(xPosition=4, yPosition=4), world=self.pyWorld)
        self.pyWorld.addOrganism(self.Antypole)
        self.Grass = Grass()

    def tearDown(self):
        pass

    def test_Exists(self):
        self.assertIsNotNone(self.Sheep)
        self.assertIsNotNone(self.Lynx)
        self.assertIsNotNone(self.Grass)
        self.assertIsNotNone(self.Antypole)

    def test_values_lynx(self):
        self.assertEqual('R', self.Lynx.sign)
        self.assertEqual('A', self.Antypole.sign)

    def test_is_not_Equal(self):

        self.assertNotEqual(self.Lynx, self.Antypole)
        self.assertFalse(self.Lynx.__eq__(self.Antypole))

    def test_organism_attack_organism(self):
        self.assertTrue(Organism.AttackOrganism(self.Lynx, self.Antypole))
        self.assertFalse(Organism.AttackOrganism(self.Antypole, self.Antypole))

    def test_organism_hungry_organism(self):
        self.assertFalse(Organism.isHungry(self.Lynx))
        self.Lynx.eating = 2
        self.assertTrue(Organism.isHungry(self.Lynx))

    def test_organism_escape_organism(self):
        self.assertTrue(Organism.isAbleToEscape(self.Antypole, self.Lynx))
        self.assertFalse(Organism.isAbleToEscape(self.Lynx, self.Antypole))

    def test_organism_consequences_organism(self):
        result = []
        result.append(Action(ActionEnum.A_REMOVE, Position(xPosition=-1, yPosition=-1), 0, self.Antypole))
        result.append(Action(ActionEnum.A_INCREASEPOWER, 0, 2, self.Lynx))
        result.append(Action(ActionEnum.A_EAT, 0, self.Lynx.eating, self.Lynx))
        result1 = Organism.consequences(self.Antypole, self.Lynx)
        result2 = Organism.consequences(self.Lynx, self.Antypole)
        newpoz1 = result.__eq__(result1)
        newpoz2 = result.__eq__(result2)
        self.assertTrue(newpoz1)
        self.assertFalse(newpoz2)

    def test_world_isOrganism(self):
        result = self.pyWorld.isOrganism(self.Lynx)
        result2 = self.pyWorld.OrganismLegend(self.Lynx)
        self.assertTrue(result)
        self.assertTrue(result2)

    def test_world_getEscape(self):
        newpoz = Position(xPosition=6, yPosition=4)
        result = self.pyWorld.getEscapePosition(self.Lynx.position, self.Antypole.position)
        result2 = self.pyWorld.getEscapePosition(self.Antypole.position, self.Lynx.position)
        pos1 = Position(result).__eq__(newpoz)
        pos2 = Position(result2).__eq__(newpoz)
        self.assertTrue(pos1)
        self.assertFalse(pos2)

    def test_world_plague_reducing_live(self):
        self.pyWorld.plague_turn = 1
        Lynx_live1 = self.Lynx.liveLength
        Antylope_live2 = self.Antypole.liveLength = 15
        self.pyWorld.plague()
        self.assertEqual(Lynx_live1 // 2, self.Lynx.liveLength)
        self.assertEqual(Antylope_live2 // 2, self.Antypole.liveLength)

    def test_world_plague_2_turns(self):
        userinput = '1'
        self.pyWorld.plague(userinput)
        self.pyWorld.plague()
        self.assertEqual(2, self.pyWorld.plague_turn)

    def test_animal_attack(self):
        result = []
        self.Lynx.eating = 2
        result.append(Action(ActionEnum.A_MOVE, self.Antypole.position, 0, self.Lynx))
        result.append(Action(ActionEnum.A_REMOVE, Position(xPosition=-1, yPosition=-1), 0, self.Antypole))
        result.append(Action(ActionEnum.A_INCREASEPOWER, 0, 2, self.Lynx))
        result.append(Action(ActionEnum.A_EAT, 0, self.Lynx.eating, self.Lynx))
        actual = Animal.attack(self.Lynx)
        self.assertTrue(actual.__eq__(result))

    def test_animal_filter_organism_position(self):
        result = self.pyWorld.organisms
        actual = Animal.getPredatorPosition(self.Antypole)
        self.assertEqual(result[0], actual[0])
        self.assertLessEqual(actual, result)


if __name__ == "__main__":
    unittest.main()
