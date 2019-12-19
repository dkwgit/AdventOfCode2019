import os
import sys
sys.path.append(os.path.abspath('../IntCodeComputer'))

from Computer import Computer as Computer
from DataFixture import DataFixture as DataFixture
from Robot import Robot as Robot
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
                if (not isinstance(output,list)):
                    output = [output]
                print(f"\t\tRunning subtest {idx + 1}")
                c = Computer()
                c.LoadProgram(testData).SetInput([value])
                continueRun = True
                result = []
                while(continueRun):
                    oneResult, continueRun, inputNext =  c.DoNext()
                    assert(inputNext != True) #for these tests, no need for subsequent
                    if (oneResult != None):
                        result.append(oneResult)
                assert(result == output)

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
        nextValue = 0
        output = None
        assert(len(settings)==5)
        for index,setting in enumerate(settings):
            c = Computer()
            c.LoadProgram(programData).SetInput([setting, nextValue])
            continueRun = True
            while(continueRun):
                oneResult, continueRun, inputNext = c.DoNext()
                assert(inputNext != True) #for the non-feedback amplifier no need for subsequent.
                if (oneResult != None):
                   nextValue = oneResult
        output = nextValue
        return output

    def FindMaxOutput(self, programData):
        allResults = []
        for item in permutations([0, 1, 2, 3, 4]):
            allResults.append(self.RunAmplifierSetup(programData, item))
        allResults.sort()
        return allResults[-1]

    def RunAmplifierFeedbackSetup(self, programData, amplifierSettings):
        computers = []
        finishedComputers = []
        nextValue = 0
        for index,setting in enumerate(amplifierSettings):
            c = Computer()
            computers.append(c)
            finishedComputers.append(None)
            c.LoadProgram(programData).SetInput([setting, nextValue])
            inputNext = False
            while(inputNext != True):
                oneResult, continueRun, inputNext = c.DoNext()
                if (oneResult != None):
                   nextValue = oneResult
        loop = 5
        while(loop > 0):
            for index in range(len(computers)):
                c= computers[index]
                if (c is None):
                    # in theory each amplifier stops in linear succession
                    assert(0==1)
                    continue
                c.SetInput([nextValue])
                inputNext = False
                continueRun = True
                while(inputNext != True and continueRun):
                    oneResult, continueRun, inputNext = c.DoNext()
                    if (oneResult != None):
                        nextValue = oneResult
                if (continueRun == False):
                    computers[index] = None
                    finishedComputers[index] = c
                    loop = loop - 1
        return nextValue

    def FindMaxOutputWithFeedback(self, programData):
        allResults = []
        for item in permutations([5, 6, 7, 8, 9]):
            allResults.append(self.RunAmplifierFeedbackSetup(programData, item))
        allResults.sort()
        return allResults[-1]

    def RunDay5(self):
        c = Computer()
        c.LoadProgram(DataFixture.mainDataDay5).SetInput([1])
        continueRun = True
        result = None
        while(continueRun):
            oneResult, continueRun, inputNext =  c.DoNext()
            assert(inputNext != True) #for these tests, no need for subsequent
            if (oneResult != None):
                result = oneResult
        print(f"Day 5-1, result is {result}, expected 3122865")
        c = Computer()
        c.LoadProgram(DataFixture.mainDataDay5).SetInput([5])
        continueRun = True
        result = None
        while(continueRun):
            oneResult, continueRun, inputNext =  c.DoNext()
            assert(inputNext != True) #for these tests, no need for subsequent
            if (oneResult != None):
                result = oneResult
        print(f"Day 5-2, result is {result}, expected 773660")

    def RunDay7(self):
        maxOutput = self.FindMaxOutput(DataFixture.mainDataDay7)
        print(f"Max possible output is {maxOutput}, expected 437860") #437860
        maxFeedbackOutput = self.FindMaxOutputWithFeedback(DataFixture.mainDataDay7)
        print(f"Max possible output with feedback is {maxFeedbackOutput}, expected 49810599") #49810599

    def RunDay9(self):
        c = Computer()
        c.LoadProgram(DataFixture.mainDay9).SetInput([1])
        continueRun = True
        val1 = None
        while(continueRun):
            oneResult, continueRun, inputNext =  c.DoNext()
            assert(inputNext != True) #for these tests, no need for subsequent
            if (oneResult != None):
                val1 = oneResult
        print(f"Run of Day 9-1 with input 1 produces {val1}, expected 3533056970") #3533056970
        c = Computer()
        c.LoadProgram(DataFixture.mainDay9).SetInput([2])
        continueRun = True
        val2 = None
        while(continueRun):
            oneResult, continueRun, inputNext =  c.DoNext()
            assert(inputNext != True) #for these tests, no need for subsequent
            if (oneResult != None):
                val2 = oneResult
        print(f"Run of Day 9-2 with input 2 produces {val2}, expected 72852") #72852

    def RunDay11(self):
        c = Computer()
        c.LoadProgram(DataFixture.mainDay11)
        robot = Robot(c)
        robot.Run(1)  #pass 0 for Day11-1, and 1 for Day11-2
     
    def Run(self):
        #self.DoTests()
        #self.RunDay5()
        #self.RunDay7()
        #self.RunDay9()
        self.RunDay11()

d = Driver()
d.Run()










