from Explorer import Explorer
import concurrent.futures
import threading
from math import ceil

class Universe:

    def __init__(self):
        self._worldsToEvaluate = []
        self._generations = 0
        self._solution = None
        self._worldsCounted = {}
        self._longestKeyString = 0

    def RegisterKeyStringLength(self, length):
        if (length > self._longestKeyString):
            self._longestKeyString = length

    def CountWorld(self, w):
        if (w._generation not in self._worldsCounted.keys()):
            self._worldsCounted[w._generation] = 0
        self._worldsCounted[w._generation] += 1

    def AddWorldsForEvaluation(self, worlds):
        self._worldsToEvaluate.extend(worlds)

    def Run(self):
        while (self._solution is None):
            worlds = self._worldsToEvaluate.copy()
            self._worldsToEvaluate = []

            for w in worlds:
                self._solution = w.EvaluateWorld()
                if (self._solution is not None):
                    break

            for w in worlds:
                w.SetupForNextGeneration()

            self._generations += 1
            print(f"Universe generation {self._generations}, next round will look at {len(self._worldsToEvaluate)} worlds")
            print(f"\tTotal worlds considered = {sum(self._worldsCounted.values())}")
            print(f"\tLargest key run found = {self._longestKeyString}")
            if (len(self._worldsToEvaluate) > 0):
                shortestKeyRun = min(map(lambda x: len(x._keyOrder), self._worldsToEvaluate))
                print(f"\tshortest key run extant = {shortestKeyRun}")
        return self._solution