from player import player
from constants import *

class batailleNavale():
    def __init__(self, x, y):
        self.players = []
        self._typeBateaux = []
        self._x = x
        self._y = y
        grille = self._createGrille(x, y)
        for i in range(0, NBPLAYERS):
            self.players.append(player(self, grille, i))

    # Fonction grille

    # Intialise une grille de taille x par y remplie de 0
    def _createGrille(self, x, y):
        if x > MAXX: x = MAXX
        if y > MAXY: y = MAXY
        if x < MINX: x = MINX
        if y < MINY: y = MINY
        return [[0] * x for _ in range(y)]

    # Fonction type bateaux

    def createTypeBateau(self, x, y, nbBateaux):
        if x > self._x or y > self._y or x < 0 or y < 0:
            return None
        self._typeBateaux.append([x, y, nbBateaux, x * y])
        for i in range(0, NBPLAYERS):
            self.players[i].setTypeBateaux(self._typeBateaux)
        # return 1 pour 1 bateau (meme si id 0)
        return len(self._typeBateaux)

    def typeBateau(self, i):
        return self._typeBateaux[i - 1]

    def _tirer(self, iTx, iRx, x, y):
        if iTx == iRx or len(self.players) <= iTx or len(self.players) <= iRx:
            return None
        if x > len(self.players[iRx]._grille) and y > len(self.players[iRx]._grille[0]):
            return None

        btTarget = self.players[iRx]._grille[y][x]

        if btTarget > 0:
            self.players[iRx]._grille[y][x] = 0
            self.players[iRx]._bateaux[btTarget - 1][3] -= 1
            nbVieRestante = 0
            for bateau in self.players[iRx]._bateaux:
                nbVieRestante += bateau[3]
            if nbVieRestante == 0:
                nbPlayerAlive = 0
                for player in self.players:
                    nbVieRestante = 0
                    for bateau in player._bateaux:
                        nbVieRestante += bateau[3]
                    if nbVieRestante > 0:
                        nbPlayerAlive += 1
                if nbPlayerAlive == 1:
                    return 4
                else:
                    return 3
            elif self.players[iRx]._bateaux[btTarget - 1][3] > 0:
                return 1
            else:
                return 2
        else:
            return 0

    def startGame(self):
        tblTypeBateaux = [0] * len(self._typeBateaux)

        if len(self.players) < 2:
            return False
        else:
            for bateau in self.players[0]._bateaux:
                if bateau[2] - 1 >= len(self._typeBateaux):
                    return False
                else:
                    tblTypeBateaux[bateau[2] - 1] += 1

        for player in self.players:
            tmpTblTypeBateaux = [0] * len(self._typeBateaux)
            for bateau in player._bateaux:
                if bateau[2] - 1 >= len(self._typeBateaux):
                    return False
                else:
                    tmpTblTypeBateaux[bateau[2] - 1] += 1
            if tmpTblTypeBateaux != tblTypeBateaux:
                return False
        return True
