from collections import namedtuple

MoonPosition = namedtuple('MoonPosition', 'x y z moonName')
MoonVelocity = namedtuple ('MoonVelocity', 'x y z moonName')
MoonInfo = namedtuple('MoonInfo', 'moonPosition moonVelocity moonName')
VelocityChange = namedtuple('VelocityChange', 'x y z moonName')


class DataFixture:

    energySeries = [
        (0,
        [
        MoonInfo(MoonPosition(-8,-10,0,'Io'), MoonVelocity(0,0,0,'Io'),'Io'),
        MoonInfo(MoonPosition(5,5,10,'Europa'), MoonVelocity(0,0,0,'Europa'),'Europa'),
        MoonInfo(MoonPosition(2,-7,3,'Ganymede'), MoonVelocity(0,0,0,'Ganymede'),'Ganymede'),
        MoonInfo(MoonPosition(9,-8,-3,'Callisto'), MoonVelocity(0,0,0,'Callisto'),'Callisto')
        ]
        )
    ]

    testSeries1 = [
        (0,
        [
        MoonInfo(MoonPosition(-1,0,2,'Io'), MoonVelocity(0,0,0,'Io'),'Io'),
        MoonInfo(MoonPosition(2,-10,-7,'Europa'), MoonVelocity(0,0,0,'Europa'),'Europa'),
        MoonInfo(MoonPosition(4,-8,8,'Ganymede'), MoonVelocity(0,0,0,'Ganymede'),'Ganymede'),
        MoonInfo(MoonPosition(3,5,-1,'Callisto'), MoonVelocity(0,0,0,'Callisto'),'Callisto')
        ]
        )
        ,
        (1,
        [
        MoonInfo(MoonPosition(2,-1,1,'Io'), MoonVelocity(3,-1,-1,'Io'),'Io'),
        MoonInfo(MoonPosition(3,-7,-4,'Europa'), MoonVelocity(1,3,3,'Europa'),'Europa'),
        MoonInfo(MoonPosition(1,-7,5,'Ganymede'), MoonVelocity(-3,1,-3,'Ganymede'),'Ganymede'),
        MoonInfo(MoonPosition(2,2,0,'Callisto'), MoonVelocity(-1,-3,1,'Callisto'),'Callisto')
        ]
        ),
        (2,
        [
        MoonInfo(MoonPosition(5,-3,-1,'Io'), MoonVelocity(3,-2,-2,'Io'),'Io'),
        MoonInfo(MoonPosition(1,-2,2,'Europa'), MoonVelocity(-2,5,6,'Europa'),'Europa'),
        MoonInfo(MoonPosition(1,-4,-1,'Ganymede'), MoonVelocity(0,3,-6,'Ganymede'),'Ganymede'),
        MoonInfo(MoonPosition(1,-4,2,'Callisto'), MoonVelocity(-1,-6,2,'Callisto'),'Callisto')
        ]
        ),
        (3,
        [
        MoonInfo(MoonPosition(5,-6,-1,'Io'), MoonVelocity(0,-3,0,'Io'),'Io'),
        MoonInfo(MoonPosition(0,0,6,'Europa'), MoonVelocity(-1,2,4,'Europa'),'Europa'),
        MoonInfo(MoonPosition(2,1,-5,'Ganymede'), MoonVelocity(1,5,-4,'Ganymede'),'Ganymede'),
        MoonInfo(MoonPosition(1,-8,2,'Callisto'), MoonVelocity(0,-4,0,'Callisto'),'Callisto')
        ]
        ),
        (4,
        [
        MoonInfo(MoonPosition(2,-8,0,'Io'), MoonVelocity(-3,-2,1,'Io'),'Io'),
        MoonInfo(MoonPosition(2,1,7,'Europa'), MoonVelocity(2,1,1,'Europa'),'Europa'),
        MoonInfo(MoonPosition(2,3,-6,'Ganymede'), MoonVelocity(0,2,-1,'Ganymede'),'Ganymede'),
        MoonInfo(MoonPosition(2,-9,1,'Callisto'), MoonVelocity(1,-1,-1,'Callisto'),'Callisto')
        ]
        ),
        (5,
        [
        MoonInfo(MoonPosition(-1,-9,2,'Io'), MoonVelocity(-3,-1,2,'Io'),'Io'),
        MoonInfo(MoonPosition(4,1,5,'Europa'), MoonVelocity(2,0,-2,'Europa'),'Europa'),
        MoonInfo(MoonPosition(2,2,-4,'Ganymede'), MoonVelocity(0,-1,2,'Ganymede'),'Ganymede'),
        MoonInfo(MoonPosition(3,-7,-1,'Callisto'), MoonVelocity(1,2,-2,'Callisto'),'Callisto')
        ]
        ),
        (6,
        [
        MoonInfo(MoonPosition(-1,-7,3,'Io'), MoonVelocity(0,2,1,'Io'),'Io'),
        MoonInfo(MoonPosition(3,0,0,'Europa'), MoonVelocity(-1,-1,-5,'Europa'),'Europa'),
        MoonInfo(MoonPosition(3,-2,1,'Ganymede'), MoonVelocity(1,-4,5,'Ganymede'),'Ganymede'),
        MoonInfo(MoonPosition(3,-4,-2,'Callisto'), MoonVelocity(0,3,-1,'Callisto'),'Callisto')
        ]
        ),
        (7,
        [
        MoonInfo(MoonPosition(2,-2,1,'Io'), MoonVelocity(3,5,-2,'Io'),'Io'),
        MoonInfo(MoonPosition(1,-4,-4,'Europa'), MoonVelocity(-2,-4,-4,'Europa'),'Europa'),
        MoonInfo(MoonPosition(3,-7,5,'Ganymede'), MoonVelocity(0,-5,4,'Ganymede'),'Ganymede'),
        MoonInfo(MoonPosition(2,0,0,'Callisto'), MoonVelocity(-1,4,2,'Callisto'),'Callisto')
        ]
        ),
        (8,
        [
        MoonInfo(MoonPosition(5,2,-2,'Io'), MoonVelocity(3,4,-3,'Io'),'Io'),
        MoonInfo(MoonPosition(2,-7,-5,'Europa'), MoonVelocity(1,-3,-1,'Europa'),'Europa'),
        MoonInfo(MoonPosition(0,-9,6,'Ganymede'), MoonVelocity(-3,-2,1,'Ganymede'),'Ganymede'),
        MoonInfo(MoonPosition(1,1,3,'Callisto'), MoonVelocity(-1,1,3,'Callisto'),'Callisto')
        ]
        ),
        (9,
        [
        MoonInfo(MoonPosition(5,3,-4,'Io'), MoonVelocity(0,1,-2,'Io'),'Io'),
        MoonInfo(MoonPosition(2,-9,-3,'Europa'), MoonVelocity(0,-2,2,'Europa'),'Europa'),
        MoonInfo(MoonPosition(0,-8,4,'Ganymede'), MoonVelocity(0,1,-2,'Ganymede'),'Ganymede'),
        MoonInfo(MoonPosition(1,1,5,'Callisto'), MoonVelocity(0,0,2,'Callisto'),'Callisto')
        ]
        ),
        (10,
        [
        MoonInfo(MoonPosition(2,1,-3,'Io'), MoonVelocity(-3,-2,1,'Io'),'Io'),
        MoonInfo(MoonPosition(1,-8,0,'Europa'), MoonVelocity(-1,1,3,'Europa'),'Europa'),
        MoonInfo(MoonPosition(3,-6,1,'Ganymede'), MoonVelocity(3,2,-3,'Ganymede'),'Ganymede'),
        MoonInfo(MoonPosition(2,0,4,'Callisto'), MoonVelocity(1,-1,-1,'Callisto'),'Callisto')
        ]
        )
    ]