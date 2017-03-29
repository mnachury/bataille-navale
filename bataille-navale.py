import unittest

class TestBn(unittest.TestCase):
    def testbnBase(self):
        Bn = batailleNavale()
        
class  batailleNavale():
    def __init__(self):
        pass
    
    #Intialise une grille de taille x par y remplie de 0 test2
    def  createGrille(self, x, y):
        self._grille = [[0] * x for _ in range(y)]
    
    def grille(self):
        return self._grille

unittest.main()
