import unittest

maxX = 99
maxY = 99
minX = 5
minY = 5


class TestBn(unittest.TestCase):
    # Test de base, instanciation classe
    def test_bnBase(self):
        bn = batailleNavale(12, 12)
        self.assertIsNot(None, bn)

    # Test d'initialisation d'une grille vide
    def test_CreateGrille(self):
        bn = batailleNavale(10, 50)
        grille = bn.grille()
        self.assertEqual(50, len(grille))
        for row in grille:
            self.assertEqual(10, len(row))
            for cel in row:
                self.assertEqual(0, cel)

    # Test grille trop grande (maximum maxX;maxY)
    def test_TooBigGrille(self):
        bn = batailleNavale(500, 101)
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
        bn = batailleNavale(3, 2)
        grille = bn.grille()
        self.assertNotEqual(2, len(grille))
        self.assertEqual(minY, len(grille))
        for row in grille:
            self.assertNotEqual(3, len(row))
            self.assertEqual(minX, len(row))
            for cel in row:
                self.assertEqual(0, cel)

    # Test grille négative
    def test_NegativeGrille(self):
        bn = batailleNavale(-30, -12000)
        grille = bn.grille()
        self.assertNotEqual(-12000, len(grille))
        self.assertEqual(minY, len(grille))
        for row in grille:
            self.assertNotEqual(-30, len(row))
            self.assertEqual(minX, len(row))

    # Test initialisation type bateau
    def test_CreateTypeBateau(self):
        bn = batailleNavale(10, 10)
        i = bn.createTypeBateau(5, 1, 1)
        typeBateau = bn.typeBateau(i)
        self.assertEqual(5, typeBateau[0])
        self.assertEqual(1, typeBateau[1])

    # Test initialisation bateau
    def test_CreateBateau(self):
        bn = batailleNavale(10, 10)
        i = bn.createTypeBateau(1, 4, 1)
        idBateau = bn.createBateau(0, 0, i)
        bateau = bn.bateau(idBateau)
        self.assertEqual(0, bateau[0])
        self.assertEqual(0, bateau[1])
        self.assertEqual(idBateau, bateau[2])

    # Test bateau trop grand
    def test_TooBigBateau(self):
        bn = batailleNavale(10, 10)
        i = bn.createTypeBateau(11, 6, 1)
        self.assertIsNone(i)

    # Test bateau avec dimensions négatives
    def test_NegativeBateau(self):
        bn = batailleNavale(10, 10)
        i = bn.createTypeBateau(-1000, -12, 1)
        self.assertIsNone(i)

    # Test positionnement invalide
    def test_InvalidePlaceBateau(self):
        bn = batailleNavale(10, 10)
        i = bn.createTypeBateau(4, 1, 1)
        idBateau = bn.createBateau(8, 8, i)
        self.assertIsNone(idBateau)

    # Test de positionnement valide 1
    def test_ValidPlaceBateau1(self):
        bn = batailleNavale(15, 15)
        grille = bn.grille()
        i = bn.createTypeBateau(4, 1, 1)
        bn.createBateau(2, 2, i)
        row = grille[2]
        for j in range(2, 5):
            self.assertEqual(row[j], i)

    # Test de positionnement valide 2
    def test_ValidPlaceBateau2(self):
        bn = batailleNavale(15, 15)
        grille = bn.grille()
        i = bn.createTypeBateau(4, 8, 1)
        idBateau = bn.createBateau(2, 2, i)
        for k in range(2, 10):
            row = grille[k]
            for j in range(2, 5):
                self.assertEqual(row[j], i)

    # Test de postitionnement combiné
    def test_ValidPlaceCombineBateau(self):
        bn = batailleNavale(10, 10)
        grilleTest = [
            [0, 1, 1, 1, 0, 2, 2, 0, 0, 3],
            [0, 1, 1, 1, 0, 2, 2, 0, 0, 3],
            [0, 1, 1, 1, 0, 2, 2, 4, 4, 4],
            [0, 0, 0, 0, 0, 2, 2, 4, 4, 4],
            [0, 0, 7, 0, 0, 2, 2, 0, 0, 0],
            [0, 0, 7, 0, 0, 2, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 2, 2, 0, 0, 0],
            [0, 5, 5, 5, 0, 2, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 6, 6, 6, 0],
            [0, 0, 0, 0, 0, 0, 6, 6, 6, 0]
        ]
        tb1 = bn.createTypeBateau(3, 3, 1)
        tb2 = bn.createTypeBateau(2, 8, 1)
        tb3 = bn.createTypeBateau(1, 2, 2)
        tb4 = bn.createTypeBateau(3, 2, 2)
        tb5 = bn.createTypeBateau(3, 1, 1)
        bn.createBateau(1, 0, tb1)
        bn.createBateau(5, 0, tb2)
        bn.createBateau(9, 0, tb3)
        bn.createBateau(7, 2, tb4)
        bn.createBateau(1, 7, tb5)
        bn.createBateau(6, 8, tb4)
        bn.createBateau(2, 4, tb3)
        grille = bn.grille()
        self.assertEqual(grille, grilleTest)

    # Test de chevauchement bateaux
    def test_OverlapPlaceBateaux(self):
        bn = batailleNavale(10, 10)
        i = bn.createTypeBateau(4, 8, 2)
        b1 = bn.createBateau(2, 2, i)
        b2 = bn.createBateau(2, 2, i)
        self.assertIsNotNone(b1)
        self.assertIsNone(b2)


class batailleNavale():
    def __init__(self, x, y):
        self._createGrille(x, y)
        self._bateaux = []
        self._typeBateaux = []

    # Fonction grille

    # Intialise une grille de taille x par y remplie de 0
    def _createGrille(self, x, y):
        if x > maxX: x = maxX
        if y > maxY: y = maxY
        if x < minX: x = minX
        if y < minY: y = minY
        self._grille = [[0] * x for _ in range(y)]

    def grille(self):
        return self._grille

    # Fonction bateaux

    def createTypeBateau(self, x, y, nbBateaux):
        if x > len(self._grille) or y > len(self._grille[0]) or x < 0 or y < 0:
            return None
        self._typeBateaux.append([x, y, nbBateaux])
        # return 1 pour 1 bateau (même si id 0)
        return len(self._typeBateaux)

    def createBateau(self, x, y, z):
        if (x + self._typeBateaux[z - 1][0
        ]) > len(self._grille) or (y + self._typeBateaux[z - 1][1]) > len(
            self._grille[0]) or x < 0 or y < 0:
            return None
        else:
            self._bateaux.append([x, y, z])
            for iy in range(y, y + self._typeBateaux[z - 1][1]):
                for ix in range(x, x + self._typeBateaux[z - 1][0]):
                    if self._grille[iy][ix] == 0:
                        self._grille[iy][ix] = len(self._bateaux)
                    else:
                        return None
            return len(self._bateaux)

    def bateau(self, i):
        return self._bateaux[i - 1]

    def typeBateau(self, i):
        return self._typeBateaux[i - 1]


if __name__ == '__main__':
    unittest.main()
