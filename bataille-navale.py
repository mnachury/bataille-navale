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

    # Test grille trop grande (maximum maxX;maxY)
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

    # Test grille trop petite (minimum minX;minY)
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
    def test_CreateBateau(self):
        bn = batailleNavale()
        i = bn.createTypeBateau(5, 1)
        idBateau = bn.createBateau(0, 0, i)
        bateau = bn.bateau(idBateau)
        self.assertEqual(5, bateau[0])
        self.assertEqual(1, bateau[1])
        self.assertEqual(idBateau, bateau[2])


class batailleNavale():
    def __init__(self):
        self._bateaux = []

    # Fonction grille

    # Intialise une grille de taille x par y remplie de 0
    def createGrille(self, x, y):
        if x > maxX: x = maxX
        if y > maxY: y = maxY
        if x < minX: x = minX
        if y < minY: y = minY
        self._grille = [[0] * x for _ in range(y)]

    def grille(self):
        return self._grille

    # Fonction bateaux

    def createTypeBateau(self, x, y):
        self._typeBateaux.append({x, y})
        # return 1 pour 1 bateaux (même si id 0)
        return len(self._bateaux)

    def createBateau(self, x, y, z):
        self._typeBateaux.append({x, y, z - 1})
        return len(self._bateaux)

    def bateau(self, i):
        return self._bateaux(i - 1)


if __name__ == '__main__':
    unittest.main()
