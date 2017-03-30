import unittest

maxX = 99
maxY = 99
minX = 5
minY = 5

class TestBn(unittest.TestCase):
    # Test de base, instanciation classe
    def test_bnBase(self):
        bn = batailleNavale()
        self.assertIsNot(None, bn)

    # Test d'initialisation d'une grille vide
    def test_CreateGrille(self):
        bn = batailleNavale()
        bn.createGrille(10, 50)
        grille = bn.grille()
        self.assertEqual(50, len(grille))
        for row in grille:
            self.assertEqual(10, len(row))
            for cel in row:
                self.assertEqual(0, cel)

    # Test grille trop grande (maximum 100)
    def test_TooBigGrille(self):
        bn = batailleNavale()
        bn.createGrille(500, 101)
        grille = bn.grille()
        self.assertNotEqual(101, len(grille))
        self.assertEqual(maxY, len(grille))
        for row in grille:
            self.assertNotEqual(500, len(row))
            self.assertEqual(maxX, len(row))
            for cel in row:
                self.assertEqual(0, cel)

    # Test grille trop petite (minimum 5)
    def test_TooSmallGrille(self):
        bn = batailleNavale()
        bn.createGrille(3, 2)
        grille = bn.grille()
        self.assertNotEqual(2, len(grille))
        self.assertEqual(minY, len(grille))
        for row in grille:
            self.assertNotEqual(3, len(row))
            self.assertEqual(minX, len(row))
            for cel in row:
                self.assertEqual(0, cel)

    # Test initialisation bateau
    # def testCreateBateau(self):
    #     bn = batailleNavale()
    #     i = bn.createBateau(5, 1)
    #     bateau = bn.bateau(i)
    #     self.assertEqual(1, len(bateau))
    #     for row in bateau:
    #         self.assertEqual(10, len(row))
    #         for cel in row:
    #             pass

class  batailleNavale():

    def __init__(self):
        self._bateaux = []

    # Fonction grille

    # Intialise une grille de taille x par y remplie de 0
    def  createGrille(self, x, y):
        if x > maxX: x = maxX
        if y > maxY: y = maxY
        if x < minX: x = minX
        if y < minY: y = minY
        self._grille = [[0] * x for _ in range(y)]

    def grille(self):
        return self._grille

    # Fonction bateaux

    def createBateau(self,x,y,z):
        self._bateaux.append({x,y,z})
        return len(self._bateaux-1)

    def bateau(self,i):
        return self._bateaux(i)

if __name__ == '__main__':
    unittest.main()
