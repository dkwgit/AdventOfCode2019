from typing import Dict, List, Callable
import sys

# Day 2 is at https://adventofcode.com/2019/day/2

inputData = [
    3,225,                  #0
    1,225,6,6,              #2
    1100,1,238,225,         #6
    104,0,                  #10
    1002,36,25,224,         #12
    1001,224,-2100,224,     #16
    4,224,                  #20
    1002,223,8,223,         #22
    101,1,224,224,          #26
    1,223,224,223,          #30
    1102,31,84,225,         #34
    1102,29,77,225,         #38
    1,176,188,224,          #42
    101,-42,224,224,        #46
    4,224,                  #50
    102,8,223,223,
    101,3,224,224,
    1,223,224,223,
    2,196,183,224,
    1001,224,-990,224,
    4,224,
    1002,223,8,223,
    101,7,224,224,
    1,224,223,223,
    102,14,40,224,
    101,-1078,224,224,
    4,224,
    1002,223,8,223,
    1001,224,2,224,
    1,224,223,223,
    1001,180,64,224,
    101,-128,224,224,
    4,224,
    102,8,223,223,
    101,3,224,224,
    1,223,224,223,
    1102,24,17,224,
    1001,224,-408,224,
    4,224,
    1002,223,8,223,
    101,2,224,224,
    1,223,224,223,
    1101,9,66,224,
    1001,224,-75,224,
    4,224,
    1002,223,8,223,
    1001,224,6,224,
    1,223,224,223,
    1102,18,33,225,
    1101,57,64,225,
    1102,45,11,225,
    1101,45,9,225,
    1101,11,34,225,
    1102,59,22,225,
    101,89,191,224,
    1001,224,-100,224,
    4,224,
    1002,223,8,223,
    1001,224,1,224,
    1,223,224,223,
    4,223,
    99,
    0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,8,226,677,224,1002,223,2,223,1006,224,329,1001,223,1,223,108,226,226,224,1002,223,2,223,1006,224,344,1001,223,1,223,7,677,226,224,102,2,223,223,1005,224,359,101,1,223,223,7,226,677,224,102,2,223,223,1006,224,374,101,1,223,223,1008,677,226,224,1002,223,2,223,1006,224,389,101,1,223,223,8,677,677,224,1002,223,2,223,1005,224,404,101,1,223,223,8,677,226,224,102,2,223,223,1005,224,419,1001,223,1,223,1107,677,226,224,102,2,223,223,1005,224,434,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,449,1001,223,1,223,107,677,226,224,1002,223,2,223,1005,224,464,1001,223,1,223,1008,677,677,224,1002,223,2,223,1006,224,479,1001,223,1,223,1108,677,226,224,1002,223,2,223,1006,224,494,1001,223,1,223,1108,677,677,224,1002,223,2,223,1006,224,509,1001,223,1,223,107,677,677,224,1002,223,2,223,1005,224,524,101,1,223,223,1007,677,226,224,102,2,223,223,1005,224,539,1001,223,1,223,1107,226,226,224,1002,223,2,223,1006,224,554,1001,223,1,223,1008,226,226,224,1002,223,2,223,1006,224,569,101,1,223,223,1108,226,677,224,1002,223,2,223,1006,224,584,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,599,1001,223,1,223,1007,677,677,224,102,2,223,223,1006,224,614,101,1,223,223,107,226,226,224,102,2,223,223,1006,224,629,101,1,223,223,1007,226,226,224,102,2,223,223,1005,224,644,1001,223,1,223,108,226,677,224,102,2,223,223,1005,224,659,1001,223,1,223,7,677,677,224,102,2,223,223,1006,224,674,1001,223,1,223,4,223,99,226]

class IntCodeComputer:

    def __init__(self, program : List[int]) -> None:
        self.program = program
        self.programIndex = 0
        self.OpCodeInfo = {}
        self.OpCodeInfo[99] = (99,self.Halt, 0, False)
        self.OpCodeInfo[1] = (1,self.Addition, 3, True)
        self.OpCodeInfo[2] = (2,self.Multiplication, 3, True)
        self.OpCodeInfo[3] = (3,self.Input, 1, True)
        self.OpCodeInfo[4] = (4,self.Output, 1, False)
        self.OpCodeParameterCount = -1
        self.OpCodeParameterModes = ''
        self.OpCodeFunction = None
        self.OpCodeWrites = True
        self.OpCode = -1

    def Output(self) -> None:
        parameter,  = self.GetArgs()
        print(f"Output value {parameter}")

    def Input(self) -> None:
        position,  = self.GetArgs()
        val = input("Input a value: ")
        self.Write(int(val), int(position))
        
    def Write(self, val, position) -> None:
        self.program[position] = val

    def Addition(self) -> None:
        arg1, arg2, dest = self.GetArgs()
        self.Write(arg1 + arg2, dest)

    def Multiplication(self) -> None:
        arg1, arg2, destindex = self.GetArgs()
        self.Write(arg1 * arg2, destindex)
    
    def GetArgs(self) -> List[int]:
        parameters = []
        for i in range(0, self.OpCodeParameterCount):
            if (self.OpCodeParameterModes[i]=='1'):
                #immediate parameter
                parameters.append(self.program[self.programIndex + i + 1])
            else:
                if (i+1==self.OpCodeParameterCount and self.OpCodeWrites):
                    # for op codes that write, the last parameter is never a dereference
                    parameters.append(self.program[self.programIndex + i + 1])
                else:
                    # true positional parameter, dereference
                    parameters.append(self.program[self.program[self.programIndex + i + 1]])
        return parameters

    def Halt(self) -> None:
        pass

    def GetOpCode(self) -> int:
        return self.program[self.programIndex]

    def GetOpCodeInfo(self) -> None:
        opString = str(self.GetOpCode())

        if (len(opString)<=2):
            opCode = int(opString)
            opString = ''
        else: 
            assert(len(opString)>=3)
            opCode = int(opString[-2:])
            opString = opString[:len(opString)-2]

        self.OpCodeParameterModes = opString

        (self.OpCode, self.OpCodeFunction, self.OpCodeParameterCount, self.OpCodeWrites) = self.OpCodeInfo[opCode]

        while len(self.OpCodeParameterModes) < self.OpCodeParameterCount:
            self.OpCodeParameterModes  = '0' + self.OpCodeParameterModes
        self.OpCodeParameterModes = self.OpCodeParameterModes[::-1]
        #print(f"Opcode {self.OpCode}: {self.OpCodeParameterModes}")
        
    def Advance(self) -> None:
        self.programIndex = self.programIndex + 1 + self.OpCodeParameterCount #+1 for the opcode itself

    def Run(self) -> None:
        self.GetOpCodeInfo()
        while(self.OpCodeFunction != self.Halt):
            self.OpCodeFunction()
            self.Advance()
            self.GetOpCodeInfo()



print("Day5-1")
computer = IntCodeComputer(inputData.copy())
computer.Run()
print("Done")

