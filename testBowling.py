import unittest

class TestBowling(unittest.TestCase):
    def testJeuBase(self):
        jeu = Jeu()

    def _lancerTout(self, jeu, n=0):
        if n != 10:
            for i in range(0,21):
                jeu.lancer(n)
        else:
            for i in range(12):
                jeu.lancer(n)

    def testRaterTout(self):
        jeu = Jeu()
        self._lancerTout(jeu, 0)
        self.assertEqual(0, jeu.score())

    def testQueDesUn(self):
        jeu =  Jeu()
        self._lancerTout(jeu, 1)
        self.assertEqual(20, jeu.score())

    def testSpares(self):
        jeu = Jeu()
        self._lancerTout(jeu, 5)
        self.assertEqual(150, jeu.score())

    def testStrikes(self):
        jeu = Jeu()
        self._lancerTout(jeu, 10)
        self.assertEqual(300, jeu.score())

class Jeu:
    def __init__(self):
        self._score = 0
        self._lancers = []
        self._indiceLancer = 0

    def lancer(self, nbQuilles):
        self._lancers.append(nbQuilles)
        if nbQuilles == 10:
            self._lancers.append(0)

    def score(self):
        score = 0
        i = 0
        while i < 20:
            n = self._lancers[i]
            if i%2 == 0 and self._lancers[i] == 10:
                i += 1
                if self._lancers[i+1] != 10:
                    score += self._lancers[i+1]
                    score += self._lancers[i+2]
                else:
                    score += 10
                    score += self._lancers[i+3]
            if i%2 == 1 and self._lancers[i] + self._lancers[i-1] == 10:
                #spare
                score += self._lancers[i+1]
            score += self._lancers[i]
            i += 1
        return score

unittest.main()
