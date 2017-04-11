import unittest
import batailleNavale
import player

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

    # Test grille negative
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

    # Test bateau avec dimensions negatives
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

    # Test de postitionnement combine
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

    # Test de creation de bateaux pour 2 joueurs
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

    # Test de creation de bateaux pour 2 joueurs
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

    # Test tir a la Kim Jong Un
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
        self.assertEqual(0, fire)
        # Tir touche
        fire = bn.players[0].tirer(1, 1, 0)
        self.assertEqual(1, fire)
        # Tir touche
        fire = bn.players[1].tirer(0, 7, 5)
        self.assertEqual(1, fire)
        # Tir sur joueur inexistant
        fire = bn.players[0].tirer(2, 1, 0)
        self.assertIsNone(fire)
        fire = bn.players[0].tirer(1, 100, 1000)
        self.assertIsNone(fire)
        # Tir touche-coule
        fire = bn.players[1].tirer(0, 8, 5)
        self.assertEqual(2, fire)

    # Test start THE GAME
    def test_StartGame(self):
        bn = batailleNavale(10, 10)
        tb1 = bn.createTypeBateau(3, 3, 1)
        tb2 = bn.createTypeBateau(2, 1, 1)
        b1 = bn.players[0].createBateau(1, 0, tb1)
        b2 = bn.players[0].createBateau(9, 0, tb1)
        b3 = bn.players[0].createBateau(7, 5, tb2)
        b4 = bn.players[1].createBateau(1, 0, tb1)
        b5 = bn.players[1].createBateau(9, 0, tb1)
        b6 = bn.players[1].createBateau(7, 5, tb2)
        jeu = bn.startGame()
        self.assertTrue(jeu)

    # Test start THE GAME invalide
    def test_InvalidStartGame(self):
        bn = batailleNavale(10, 10)
        tb1 = bn.createTypeBateau(3, 3, 1)
        tb2 = bn.createTypeBateau(2, 1, 1)
        b1 = bn.players[0].createBateau(1, 0, tb1)
        b2 = bn.players[1].createBateau(1, 0, tb2)
        jeu = bn.startGame()
        self.assertFalse(jeu)

    # Test full GAME
    def test_FullGame(self):
        bn = batailleNavale(10, 10)
        tb1 = bn.createTypeBateau(2, 1, 1)
        p1 = bn.players[0]
        p2 = bn.players[1]
        #p3 = bn.players[2]
        b1 = p1.createBateau(0, 0, tb1)
        b2 = p2.createBateau(0, 0, tb1)
        #b3 = p3.createBateau(0, 0, tb1)
        jeu = bn.startGame()
        p1.tirer(1, 0, 0)
        fire = p1.tirer(1, 1, 0)
        self.assertEqual(4, fire)
