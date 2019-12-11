from Computer import Computer as Computer
from DataFixture import DataFixture as DataFixture
from itertools import permutations 

class Driver:
    def DoTests(self):
        testInputs = [
            DataFixture.test1,
            DataFixture.test2,
            DataFixture.test3,
            DataFixture.test4,
            DataFixture.test5,
            DataFixture.test6,
            DataFixture.test7,
            ]
        for index,testTuple in enumerate(testInputs):
            print(f"Running test {index + 1}") 
            testData = testTuple[0]  
            testDescription = testTuple[1]
            testIO = testTuple[2]
            print(f"\t{testDescription}")
            for idx, testItem in enumerate(testIO):
                print(f"\t\tRunning subtest {idx + 1}")
                c = Computer(testData, True, [testItem[0]], True, [testItem])
                c.Run()

        self.RunAmplifierTests()

    def RunAmplifierTests(self):
        testInputs = [
            DataFixture.testData1Day7,
            DataFixture.testData2Day7,
            DataFixture.testData3Day7
            ]
        for index, test in enumerate(testInputs):
            program, settings, output = test
            result = self.RunAmplifierSetup(program,settings)
            assert(result == output)

    def RunAmplifierSetup(self, programData, settings):
        nextInput = -1
        output = None
        assert(len(settings)==5)
        for index,setting in enumerate(settings):
            if (index == 0):
                c = Computer(programData, True, [setting,0])
                c.Run()
                nextInput = c._outputs[-1]
            else:
                c = Computer(programData, True, [setting,nextInput])
                c.Run()
                if (index == 4):
                    output = c._outputs[-1]
        return output

    def FindMaxOutput(self, programData):
        allResults = []
        for item in permutations([0, 1, 2, 3, 4]):
            allResults.append(self.RunAmplifierSetup(programData, item))
        allResults.sort()
        return allResults[-1]

d = Driver()
d.DoTests()
        


