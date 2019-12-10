from Computer import Computer as Computer
from DataFixture import DataFixture as DataFixture


#do tests
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
    for index, testItem in enumerate(testIO):
        print(f"\t\tRunning subtest {index + 1}")
        c = Computer(testData)
        c.Run(True, testItem)
