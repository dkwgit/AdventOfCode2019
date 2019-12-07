import math

    # see https://adventofcode.com/2019/day/1

class FuelCalculator:
    @staticmethod
    def GetFuelNaive(mass : int) -> int:
        fuel = math.floor(mass / 3) - 2
        if (fuel > 0):
            return fuel
        else:
            return 0

    @staticmethod
    def GetFuel(mass : int) -> int:
        fuel : int = FuelCalculator.GetFuelNaive(mass)
        if (fuel > 0):
            return fuel + FuelCalculator.GetFuel(fuel)
        else: 
            return 0
            

assert(FuelCalculator.GetFuelNaive(12)==2)
assert(FuelCalculator.GetFuelNaive(14)==2)
assert(FuelCalculator.GetFuelNaive(15)==3)
assert(FuelCalculator.GetFuel(100756) == 50346)

modules = [88062,147838,73346,80732,89182,86798,145656,53825,79515,78250,143033,53680,89366,123255,74974,65373,107733,118266,50726,87810,104355,85331,109624,54282,107472,119291,128702,81132,94609,105929,63918,113360,66932,145080,132130,63858,104334,140635,67642,111552,93446,59263,133164,119788,97327,77379,144054,110747,89394,123533,86026,124422,108855,125000,99270,55789,146945,103156,141044,94238,136833,54370,69178,142349,72239,149992,50901,112759,105467,90841,55693,52532,92343,134889,143351,123359,134972,59986,85415,136521,81581,131078,131201,56194,142135,69982,140667,110013,67772,108135,92591,87200,78189,73407,145395,131869,143480,82068,82423,110819]
fuelForAllModulesNaive = sum(map(lambda x: FuelCalculator.GetFuelNaive(x), modules))
fuelForAllModules = sum(map(lambda x: FuelCalculator.GetFuel(x), modules))


print(f"Fuel needed for all modules, using naive method (does not provide fuel for fuel) {fuelForAllModulesNaive}")
print(f"Fuel needed for all modules {fuelForAllModules}")