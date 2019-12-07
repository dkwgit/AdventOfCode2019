from typing import Dict, List, Callable
import sys

# Day 2 is at https://adventofcode.com/2019/day/2

input = [
    1,0,0,3,        #0
    1,1,2,3,        #4
    1,3,4,3,        #8
    1,5,0,3,        #12
    2,1,10,19,      #16
    2,9,19,23,      #20
    2,23,10,27,     #24
    1,6,27,31,      #28
    1,31,6,35,      #32
    2,35,10,39,     #36
    1,39,5,43,      #40
    2,6,43,47,      #44
    2,47,10,51,     #48
    1,51,6,55,      #52
    1,55,6,59,      #56
    1,9,59,63,      #60
    1,63,9,67,      #64
    1,67,6,71,      #68
    2,71,13,75,     #72
    1,75,5,79,      #76
    1,79,9,83,      #80
    2,6,83,87,      #84
    1,87,5,91,      #88
    2,6,91,95,      #92
    1,95,9,99,      #96
    2,6,99,103,     #100
    1,5,103,107,    #104
    1,6,107,111,    #108
    1,111,10,115,   #112
    2,115,13,119,   #116
    1,119,6,123,    #120
    1,123,2,127,    #124
    1,127,5,0,      #128
    99,             #132
    2,14,0,0]       #133

class IntCodeComputer:

    def __init__(self, program : List[int]) -> None:
        self.program = program
        self.programIndex = 0
        self.opCodeFunctions = {}
        self.opCodeFunctions[99] = self.Halt
        self.opCodeFunctions[1] = self.Addition
        self.opCodeFunctions[2] = self.Multiplication

    def Write(self, val, position) -> None:
        self.program[position] = val

    def Addition(self) -> None:
        arg1, arg2, dest = self.GetArgs()
        self.Write(arg1 + arg2, dest)

    def Multiplication(self) -> None:
        arg1, arg2, destindex = self.GetArgs()
        self.Write(arg1 * arg2, destindex)
    
    def GetArgs(self) -> List[int]:
        return [
            self.program[self.program[self.programIndex + 1]],
            self.program[self.program[self.programIndex + 2]],
            self.program[self.programIndex + 3]
        ]

    def Halt(self) -> None:
        pass

    def GetOpCode(self) -> int:
        return self.program[self.programIndex]

    def GetOpCodeFunction(self) -> Callable[[],None]:
        return self.opCodeFunctions[self.GetOpCode()]

    def Advance(self) -> None:
        self.programIndex = self.programIndex + 4

    def Run(self) -> None:
        func = self.GetOpCodeFunction()
        while(func != self.Halt):
            func()
            self.Advance()
            func = self.GetOpCodeFunction()

# Test 1
test1 = IntCodeComputer([1,9,10,3,2,3,11,0,99,30,40,50])
test1.Run()
assert(test1.program==[3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50])
# Test 2
test2 = IntCodeComputer([2,3,0,3,99])
test2.Run()
assert(test2.program==[2,3,0,6,99])
# Test 3
test3 = IntCodeComputer([2,4,4,5,99,0])
test3.Run()
assert(test3.program==[2,4,4,5,99,9801])
# Test 4
test4 = IntCodeComputer([1,1,1,4,99,5,6,0,99])
test4.Run()
assert(test4.program==[30,1,1,4,2,5,6,0,99])

print("Day2-1")
input[1] = 12
input[2] = 2
computer = IntCodeComputer(input.copy())
computer.Run()
output = list.copy(computer.program)
print(len(output))
for i in range(0, len(output),4):
    sub = output[i:(i + 4 if i + 4 <= len(output) else len(output))]
    print(f"{i}: {sub}")

print("Day2-2")
input[1] = 64
input[2] = 72
computer2 = IntCodeComputer(input.copy())
computer2.Run()
output2 = list.copy(computer2.program)
print(len(output2))
for i2 in range(0, len(output2),4):
    sub2 = output2[i2:(i2 + 4 if i2 + 4 <= len(output2) else len(output2))]
    print(f"{i2}: {sub2}")
