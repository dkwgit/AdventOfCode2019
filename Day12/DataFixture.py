from collections import namedtuple

MoonPosition = namedtuple('MoonPosition', 'x y z moonName')
MoonVelocity = namedtuple ('MoonVelocity', 'x y z moonName')
MoonInfo = namedtuple('MoonInfo', 'moonPosition moonVelocity moonName')


class DataFixture:
    startInfo = [
    MoonInfo(MoonPosition(-1,0,2,'Io'), MoonVelocity(0,0,0,'Io'),'Io'),
    MoonInfo(MoonPosition(2,-10,-7,'Europa'), MoonVelocity(0,0,0,'Europa'),'Europa'),
    MoonInfo(MoonPosition(4,-8,8,'Ganymede'), MoonVelocity(0,0,0,'Ganymede'),'Ganymede'),
    MoonInfo(MoonPosition(3,5,-1,'Callisto'), MoonVelocity(0,0,0,'Callisto'),'Callisto'),
]