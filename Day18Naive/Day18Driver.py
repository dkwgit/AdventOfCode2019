from Day18DataFixture import Day18DataFixture
from Maze import Maze
from World import World
from Universe import Universe

class Day18Driver:

    def __init__(self):
        self._maze = None
        self._universe = None
    
    def Run(self):
        self._universe = Universe()
        w = World(self._universe, 0, self._maze._entrance, self._maze, "", {}, "")
        self._universe.AddWorldsForEvaluation([w])
        solutionWorld = self._universe.Run()
        print(f"Short path to solution is {solutionWorld._generation}.")
        return solutionWorld._generation

    def LoadMaze(self,mazeData):
        highestKey = 0
        mazeData = mazeData.strip()
        mazeLines = mazeData.split("\n")
        totalY = len(mazeLines)
        totalX = max(map(lambda line : len(line), mazeLines))
        self._maze = maze = Maze(totalY, totalX)
        for y,line in enumerate(mazeLines):
            for x,val in enumerate(list(line)):
                if maze._lowKey <= ord(val) <= maze._highKey:
                    if (ord(val)> highestKey):
                        highestKey = ord(val)
                pos = (y,x)
                if (val=="@"):
                    self._start = pos
                maze.AddPoint(pos,val)
        maze._highKey = highestKey
        maze._highDoor = highestKey - 32

    def DoTest(self, numberOfMovesExpected,mazeData):
        d.LoadMaze(mazeData)
        steps = d.Run()
        assert(steps==numberOfMovesExpected)

d = Day18Driver()
for steps,data in [Day18DataFixture.test1, Day18DataFixture.test2, Day18DataFixture.test3]: #Day18DataFixture.test4, Day18DataFixture.test5]:
#for steps,data in [Day18DataFixture.test4]:
    d.DoTest(steps,data)

