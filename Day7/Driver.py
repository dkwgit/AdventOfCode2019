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
                value, output = testItem
                print(f"\t\tRunning subtest {idx + 1}")
                c = Computer(testData, True, [value])
                result = c.Run()
                print(f"\t\t\tTest produce {result} with expected {output}")
                assert(result == output)

        self.RunAmplifierTests()

    def RunAmplifierTests(self):
        testInputs = [
            DataFixture.testData1Day7,
            DataFixture.testData2Day7,
            DataFixture.testData3Day7
            ]
        for index, test in enumerate(testInputs):
            print(f"Running amplifier test {index + 1}")
            program, settings, output = test
            result = self.RunAmplifierSetup(program,settings)
            print(f"\tsettings {settings} produced result {result}, with expected output {output}")
            assert(result == output)

    def RunAmplifierSetup(self, programData, settings):
        nextInput = 0
        output = None
        assert(len(settings)==5)
        for index,setting in enumerate(settings):
            c = Computer(programData, True, [setting, nextInput])
            nextInput = c.Run()
        output = nextInput
        return output

    def FindMaxOutput(self, programData):
        allResults = []
        for item in permutations([0, 1, 2, 3, 4]):
            allResults.append(self.RunAmplifierSetup(programData, item))
        allResults.sort()
        return allResults[-1]

d = Driver()
d.DoTests()
maxOutput = d.FindMaxOutput(DataFixture.mainDataDay7)
print(f"Max possible output is {maxOutput}")

        


