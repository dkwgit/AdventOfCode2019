import itertools

# see https://adventofcode.com/2019/day/4
inputRange = {
    "Min" : 172851,
    "Max" : 675869
}

class PasswordGenerator:

    def __init__(self, min : int, max: int) -> None:
        self.firstValue = min
        self.lastValue = max
        self.validPWList = []
        self.currentCandidate = self.firstValue
        self.checkFunctionToCall = self.CheckCandidatePart1

    def FindPasswords(self) -> None:
        while(self.currentCandidate <= self.lastValue):
            if (self.checkFunctionToCall(str(self.currentCandidate))):
                self.validPWList.append(self.currentCandidate)
            self.currentCandidate = self.currentCandidate + 1

    def CheckCandidatePart1(self, candidate : str) -> bool:
        i : int = 0
        doubleExists : bool = False
        while(i < len(candidate) -1):
            b = int(candidate[i+1])
            a = int(candidate[i])
            if (b<a):
                #Nodescending
                return False
            if (a==b):
                doubleExists = True
            i = i + 1
        return doubleExists

    def CheckCandidatePart2(self, candidate : str) -> bool:
        i : int = 0
        doubleExists : bool = False
        repeatedDigits = {}
        while(i < len(candidate) -1):
            b = int(candidate[i+1])
            a = int(candidate[i])
            if (b<a):
                #Nodescending
                return False
            if (a==b):
                doubleExists = True
                if (not a in repeatedDigits):
                    repeatedDigits[a] = 2 #a exists twice, so far as a and b
                else:
                    repeatedDigits[a] = repeatedDigits[a] + 1 #subsequently count goes up by 1 at a time
            i = i + 1
        return (doubleExists and (2 in repeatedDigits.values())) #at least one repeat must have only 2 digits

pg = PasswordGenerator(inputRange["Min"],inputRange["Max"])
pg.FindPasswords()
print(f"Number of passwords for part 1 {len(pg.validPWList)}")
pg2 = PasswordGenerator(inputRange["Min"],inputRange["Max"])
pg2.checkFunctionToCall = pg2.CheckCandidatePart2
pg2.FindPasswords()
print(f"Number of passwords for part 2 {len(pg2.validPWList)}")

    

    
