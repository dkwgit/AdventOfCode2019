from Computer import Computer as Computer
from DataFixture import DataFixture as DataFixture
from itertools import permutations 
import threading

def threadStartFunc(computer, name):
    computer.Run()

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
            for idx, inputOutputTuple in enumerate(testIO):
                value, output = inputOutputTuple
                print(f"\t\tRunning subtest {idx + 1}")
                c = Computer(testData, True, [value])
                result = c.Run()
                print(f"\t\t\tTest produced {result} with expected {output}")
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

    def RunAmplifierFeedbackSetup(self, programData, amplifierSettings):
        runningComputers = []
        computers = []
        nextValue = 0
        for index,setting in enumerate(amplifierSettings):
            inputOutputEvents = (threading.Event(), threading.Event())
            c = Computer(programData, True, [setting, nextValue], inputOutputEvents)
            t = threading.Thread(target=threadStartFunc, args=(c,index,))
            t.start()
            computers.append(c)
            runningComputers.append([c,t])
            nextValue = c.GetHighestOutput()
        loop = 5
        while(loop > 0):
            for index in range(len(runningComputers)):
                c,t = runningComputers[index]
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

    def Run(self):
        d = Driver()
        d.DoTests()
        maxOutput = d.FindMaxOutput(DataFixture.mainDataDay7)
        print(f"Max possible output is {maxOutput}") #437860
        maxFeedbackOutput = d.FindMaxOutputWithFeedback(DataFixture.mainDataDay7)
        print(f"Max possible output with feedback is {maxFeedbackOutput}") #49810599

        


