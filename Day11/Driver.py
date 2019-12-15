import sys
import threading
sys.path.append('C:\\users\\dkwrig\\repos\\AdventOfCode2019\\IntCodeComputer')

from Computer import Computer as Computer
from DataFixture import DataFixture as DataFixture
from Robot import Robot as Robot
from itertools import permutations 
import threading

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
            DataFixture.testData2Day9,
            DataFixture.testData3Day9,
            DataFixture.testData1Day9,
        ]
        for index,testTuple in enumerate(testInputs):
            print(f"Running test {index + 1}") 
            testData = testTuple[0]  
            testDescription = testTuple[1]
            testIO = testTuple[2]
            print(f"\t{testDescription}")
            for idx, inputOutputTuple in enumerate(testIO):
                value, output = inputOutputTuple
                print(f"\t\tRunning subtest {idx + 1}")
                c = Computer(True, None if value is None else [value])
                bootInfo = c.Boot()
                result = c.RunProgram(testData)
                if (not isinstance(output, list)):
                    print(f"\t\t\tTest produced {result} with expected {output}")
                    assert(result == output)
                else:
                    print(f"\t\t\tTest produced {c._outputs} with expected {output}")
                    assert(c._outputs == output)

        self.RunAmplifierTests()
        self.RunAmplifierFeedbackTests()

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

    def RunAmplifierFeedbackTests(self):
        testInputs = [
            DataFixture.testData4Day7,
            DataFixture.testData5Day7
        ]
        for index, test in enumerate(testInputs):
            print(f"Running amplifier feedback test {index + 1}")
            program, settings, output = test
            result = self.RunAmplifierFeedbackSetup(program,settings)
            print(f"\tsettings {settings} produced result {result}, with expected output {output}")
            assert(result == output)

    def RunAmplifierSetup(self, programData, settings):
        nextInput = 0
        output = None
        assert(len(settings)==5)
        for index,setting in enumerate(settings):
            c = Computer(True, [setting, nextInput])
            bootInfo = c.Boot()
            nextInput = c.RunProgram(programData)
        output = nextInput
        return output

    def FindMaxOutput(self, programData):
        allResults = []
        for item in permutations([0, 1, 2, 3, 4]):
            allResults.append(self.RunAmplifierSetup(programData, item))
        allResults.sort()
        return allResults[-1]

    def RunAmplifierFeedbackSetup(self, programData, amplifierSettings):
        runningComputers = []
        computers = []
        nextValue = 0
        for index,setting in enumerate(amplifierSettings):
            c = Computer(True, [setting, nextValue])
            bootInfo = c.Boot(True)
            c.RunProgram(programData)
            computers.append(c)
            runningComputers.append(c)
            nextValue = c.GetHighestOutput()
        loop = 5
        while(loop > 0):
            for index in range(len(runningComputers)):
                c= runningComputers[index]
                if (c is None):
                    # in theory each amplifier stops in linear succession
                    assert(0==1)
                    continue
                c.AddInput(nextValue)
                if (c.GetState() == 0):
                    nextValue = c.GetLastOutput()
                    runningComputers[index] = None
                    loop = loop - 1
                else:
                    nextValue = c.GetHighestOutput()
        return nextValue

    def FindMaxOutputWithFeedback(self, programData):
        allResults = []
        for item in permutations([5, 6, 7, 8, 9]):
            allResults.append(self.RunAmplifierFeedbackSetup(programData, item))
        allResults.sort()
        return allResults[-1]

    def RunDay5(self):
        c = Computer(True, [1])
        bootInfo = c.Boot()
        result = c.RunProgram(DataFixture.mainDataDay5)
        print(f"Day 5-1, result is {result}, expected 3122865")
        c = Computer(True, [5])
        bootInfo = c.Boot()
        result = c.RunProgram(DataFixture.mainDataDay5)
        print(f"Day 5-2, result is {result}, expected 773660")

    def RunDay7(self):
        maxOutput = self.FindMaxOutput(DataFixture.mainDataDay7)
        print(f"Max possible output is {maxOutput}") #437860
        maxFeedbackOutput = self.FindMaxOutputWithFeedback(DataFixture.mainDataDay7)
        print(f"Max possible output with feedback is {maxFeedbackOutput}") #49810599

    def RunDay9(self):
        c1 = Computer(True,[1])
        val1 = c1.RunProgram(DataFixture.mainDay9)
        print(f"Run of Day 9-1 with input 1 produces {val1}") #3533056970
        c2 = Computer(True,[2])
        val2 = c2.RunProgram(DataFixture.mainDay9)
        print(f"Run of Day 9-2 with input 2 produces {val2}") #72852

    def RunDay11(self):
        c = Computer(True)
        bootInfo = c.Boot(True)
        retVal = c.RunProgram(DataFixture.mainDay11)
        robot = Robot(c)
        robot.Run()
     
    def Run(self):
        #self.DoTests()
        #self.RunDay5()
        #self.RunDay7()
        #self.RunDay9()
        self.RunDay11()

d = Driver()
d.Run()










