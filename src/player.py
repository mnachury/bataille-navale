from src.constants import *

class player():
    def __init__(self, bn, grille, i):
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
            if bateau[2] == idType - 1:
                btx += 1
        if btx > self._typeBateaux[idType - 1][2]:
            return None
        if (x + self._typeBateaux[idType - 1][0
        ]) > len(self._grille) or (y + self._typeBateaux[idType - 1][1]) > len(
            self._grille[0]) or x < 0 or y < 0:
            return None
        else:
            self._bateaux.append([x, y, idType, self._typeBateaux[idType - 1][3]])
            for iy in range(y, y + self._typeBateaux[idType - 1][1]):
                for ix in range(x, x + self._typeBateaux[idType - 1][0]):
                    if self._grille[iy][ix] == 0:
                        self._grille[iy][ix] = len(self._bateaux)
                    else:
                        return None
            return len(self._bateaux)

    def bateau(self, i):
        return self._bateaux[i - 1]

    def tirer(self, iCible, x, y):
        return self._bn._tirer(self._i, iCible, x, y)
