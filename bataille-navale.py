import unittest

class TestBn(unittest.TestCase):
    def testbnBase(self):
        bn = batailleNavale()

    def testCreateGrille(self):
        bn = batailleNavale()
        bn.createGrille(10, 50)
        for row in bn.grille
            for cel in row
                assertEqual(0, cel)

class  batailleNavale():
    def __init__(self):
        pass

    #Intialise une grille de taille x par y remplie de 0
    def  createGrille(self, x, y):
        self._grille = [[0] * x for _ in range(y)]

    def grille(self):
        return self._grille

unittest.main()
