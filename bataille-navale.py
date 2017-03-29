import unittest

maxX = 99
maxY = 99

class TestBn(unittest.TestCase):
    # Test de base, instanciation classe
    def testbnBase(self):
        bn = batailleNavale()
        self.assertIsNot(None, bn)

    # Test d'initialisation d'une grille vide
    def testCreateGrille(self):
        bn = batailleNavale()
        bn.createGrille(10, 50)
        grille = bn.grille()
        self.assertEqual(50, len(grille))
        for row in grille:
            self.assertEqual(10, len(row))
            for cel in row:
                self.assertEqual(0, cel)

    # Test grille trop grande (maximum 100)
    def testTooBigGrille(self):
        bn = batailleNavale()
        bn.createGrille(500, 101)
        grille = bn.grille()
        self.assertNotEqual(101, len(grille))
        self.assertEqual(99, len(grille))

class  batailleNavale():

    
    def __init__(self):
        pass

    # Intialise une grille de taille x par y remplie de 0
    def  createGrille(self, x, y):
        if x > maxX: x = maxX
        if y > maxY: y = maxY
        self._grille = [[0] * x for _ in range(y)]

    def grille(self):
        return self._grille

unittest.main()
