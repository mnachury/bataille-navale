import unittest

nbPlayers = 2
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
        grille = bn.players[0].grille()
        self.assertEqual(50, len(grille))
        for row in grille:
            self.assertEqual(10, len(row))
            for cel in row:
                self.assertEqual(0, cel)

    # Test grille trop grande (maximum maxX;maxY)
    def test_TooBigGrille(self):
        bn = batailleNavale(500, 101)
        grille = bn.players[0].grille()
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
        grille = bn.players[0].grille()
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
        grille = bn.players[0].grille()
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
        idBateau = bn.players[0].createBateau(0, 0, i)
        bateau = bn.players[0].bateau(idBateau)
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
        idBateau = bn.players[0].createBateau(8, 8, i)
        self.assertIsNone(idBateau)

    # Test de positionnement valide 1
    def test_ValidPlaceBateau1(self):
        bn = batailleNavale(15, 15)
        grille = bn.players[0].grille()
        i = bn.createTypeBateau(4, 1, 1)
        bn.players[0].createBateau(2, 2, i)
        row = grille[2]
        for j in range(2, 5):
            self.assertEqual(row[j], i)

    # Test de positionnement valide 2
    def test_ValidPlaceBateau2(self):
        bn = batailleNavale(15, 15)
        grille = bn.players[0].grille()
        i = bn.createTypeBateau(4, 8, 1)
        idBateau = bn.players[0].createBateau(2, 2, i)
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
        bn.players[0].createBateau(1, 0, tb1)
        bn.players[0].createBateau(5, 0, tb2)
        bn.players[0].createBateau(9, 0, tb3)
        bn.players[0].createBateau(7, 2, tb4)
        bn.players[0].createBateau(1, 7, tb5)
        bn.players[0].createBateau(6, 8, tb4)
        bn.players[0].createBateau(2, 4, tb3)
        grille = bn.players[0].grille()
        self.assertEqual(grille, grilleTest)

    # Test de chevauchement bateaux
    def test_OverlapPlaceBateaux(self):
        bn = batailleNavale(10, 10)
        i = bn.createTypeBateau(4, 8, 2)
        b1 = bn.players[0].createBateau(2, 2, i)
        b2 = bn.players[0].createBateau(2, 2, i)
        self.assertIsNotNone(b1)
        self.assertIsNone(b2)

    # Test de création de bateaux pour 2 joueurs
    def test_CreateBateaux2Players(self):
        bn = batailleNavale(10, 10)
        tb1 = bn.createTypeBateau(3, 3, 1)
        tb2 = bn.createTypeBateau(2, 1, 1)
        b1 = bn.players[0].createBateau(1, 0, tb1)
        b2 = bn.players[0].createBateau(9, 0, tb1)
        b3 = bn.players[0].createBateau(7, 5, tb2)
        b4 = bn.players[1].createBateau(1, 0, tb1)
        b5 = bn.players[1].createBateau(9, 0, tb1)
        b6 = bn.players[1].createBateau(7, 5, tb2)
        for name in ['b1', 'b2', 'b3', 'b4', 'b5', 'b6']:
            self.assertIsNotNone(name)

    # Test de création de bateaux pour 2 joueurs
    # def test_InvalidCreateBateaux2Players(self):
    #     bn = batailleNavale(10, 10)
    #     tb1 = bn.createTypeBateau(3, 3, 1)
    #     tb2 = bn.createTypeBateau(2, 1, 1)
    #     b1 = bn.players[0].createBateau(1, 0, tb1)
    #     b2 = bn.players[0].createBateau(9, 0, tb1)
    #     b3 = bn.players[0].createBateau(7, 5, tb1)
    #     b4 = bn.players[1].createBateau(1, 0, tb2)
    #     b5 = bn.players[1].createBateau(9, 0, tb2)
    #     b6 = bn.players[1].createBateau(7, 5, tb2)
    #     for name in ['b1', 'b2', 'b3']:
    #         self.assertIsNotNone(name)
    #     for name in ['b4', 'b5', 'b6']:
    #         self.assertIsNone(name)

    # Test tir à la Kim Jong Un
    def test_FireEnemy(self):
        bn = batailleNavale(10, 10)
        b1 = bn.createTypeBateau(3, 3, 1)
        tb1 = bn.createTypeBateau(3, 3, 1)
        tb2 = bn.createTypeBateau(2, 1, 1)
        b1 = bn.players[0].createBateau(1, 0, tb1)
        b2 = bn.players[0].createBateau(9, 0, tb1)
        b3 = bn.players[0].createBateau(7, 5, tb2)
        b4 = bn.players[1].createBateau(1, 0, tb1)
        b5 = bn.players[1].createBateau(9, 0, tb1)
        b6 = bn.players[1].createBateau(7, 5, tb2)
        fire = bn.players[0].tirer(1, 0, 5)
        self.assertFalse(fire)
        fire = bn.players[0].tirer(1, 1, 0)
        self.assertTrue(fire)
        fire = bn.players[1].tirer(0, 1, 0)
        self.assertTrue(fire)
        fire = bn.players[0].tirer(2, 1, 0)
        self.assertIsNone(fire)
        fire = bn.players[0].tirer(1, 100, 1000)
        self.assertIsNone(fire)


class batailleNavale():
    def __init__(self, x, y):
        self.players = []
        self._typeBateaux = []
        self._x = x
        self._y = y
        grille = self._createGrille(x,y)
        for i in range(0, nbPlayers):
            self.players.append(player(self,grille,i))

    # Fonction grille

    # Intialise une grille de taille x par y remplie de 0
    def _createGrille(self, x, y):
        if x > maxX: x = maxX
        if y > maxY: y = maxY
        if x < minX: x = minX
        if y < minY: y = minY
        return [[0] * x for _ in range(y)]

    # Fonction type bateaux

    def createTypeBateau(self, x, y, nbBateaux):
        if x > self._x or y > self._y or x < 0 or y < 0:
            return None
        self._typeBateaux.append([x, y, nbBateaux])
        for i in range(0, nbPlayers):
            self.players[i].setTypeBateaux(self._typeBateaux)
        # return 1 pour 1 bateau (même si id 0)
        return len(self._typeBateaux)

    def typeBateau(self, i):
        return self._typeBateaux[i - 1]

    def _tirer(self,iTx,iRx,x,y):
        if iTx == iRx or self.players[iTx] is None or self.players[iRx] is None:
            return None
        btTarget = self.players[iTx].grille[x][y]
        if btTarget > 0:
            self.players[iTx].grille[x][y] = 0
            self.players[iTx]._bateaux[btTarget-1][3] -= 1
            nbVieRestante = 0
            for bateau in self.players[iTx]._bateaux:
                nbVieRestante += bateau[3]
            if nbVieRestante == 0:
                return 3
            elif self.players[iTx]._bateaux[btTarget-1][3] > 0:
                return 1
            else:
                return 2


class player():
    def __init__(self,bn, grille,i):
        self._bn = bn
        self._i = i
        self._grille = grille
        self._bateaux = []

    def setTypeBateaux(self, typeBateaux):
        self._typeBateaux = typeBateaux

    def grille(self):
        return self._grille

    def createBateau(self, x, y, idType):
        btx = 0
        for bateau in self._bateaux:
            if bateau[2] == idType-1:
                btx += 1
        if btx > self._typeBateaux[idType-1][2]:
            return None
        if (x + self._typeBateaux[idType - 1][0
        ]) > len(self._grille) or (y + self._typeBateaux[idType - 1][1]) > len(
            self._grille[0]) or x < 0 or y < 0:
            return None
        else:
            self._bateaux.append([x, y, idType,x*y])
            for iy in range(y, y + self._typeBateaux[idType - 1][1]):
                for ix in range(x, x + self._typeBateaux[idType - 1][0]):
                    if self._grille[iy][ix] == 0:
                        self._grille[iy][ix] = len(self._bateaux)
                    else:
                        return None
            return len(self._bateaux)

    def bateau(self, i):
        return self._bateaux[i - 1]

    def tirer(self,iCible,x,y):
        return self._bn._tirer(self._i,iCible,x,y)

if __name__ == '__main__':
    unittest.main()
