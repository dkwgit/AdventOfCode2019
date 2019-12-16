from DataFixture import *
from MoonTimeSeries import MoonTimeSeries as MoonTimeSeries

class Day12Driver:

    def TestApplyGravity(self):
        mts = MoonTimeSeries()
        for index, item in enumerate(mts.GetIterator(DataFixture.startInfo,1)):
            print(f"Series step {index}: {item}")

d = Day12Driver()
d.TestApplyGravity()


    