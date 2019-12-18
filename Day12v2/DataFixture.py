from collections import namedtuple

MoonPosition = namedtuple('MoonPosition', 'x y z moonName')
MoonVelocity = namedtuple ('MoonVelocity', 'x y z moonName')
MoonInfo = namedtuple('MoonInfo', 'moonPosition moonVelocity moonName')
VelocityChange = namedtuple('VelocityChange', 'x y z moonName')


class DataFixture:

    day12Series = [
        (0,
        [
        MoonInfo(MoonPosition(3,-6,6,'Io'), MoonVelocity(0,0,0,'Io'),'Io'),
        MoonInfo(MoonPosition(10,7,-9,'Europa'), MoonVelocity(0,0,0,'Europa'),'Europa'),
        MoonInfo(MoonPosition(-3,-7,9,'Ganymede'), MoonVelocity(0,0,0,'Ganymede'),'Ganymede'),
        MoonInfo(MoonPosition(-8,0,4,'Callisto'), MoonVelocity(0,0,0,'Callisto'),'Callisto')
        ]
        )
    ]

    energySeries = [
        (0,
        [
        MoonInfo(MoonPosition(-8,-10,0,'Io'), MoonVelocity(0,0,0,'Io'),'Io'),
        MoonInfo(MoonPosition(5,5,10,'Europa'), MoonVelocity(0,0,0,'Europa'),'Europa'),
        MoonInfo(MoonPosition(2,-7,3,'Ganymede'), MoonVelocity(0,0,0,'Ganymede'),'Ganymede'),
        MoonInfo(MoonPosition(9,-8,-3,'Callisto'), MoonVelocity(0,0,0,'Callisto'),'Callisto')
        ]
        ),
        (10,
        [
        MoonInfo(MoonPosition(-9,-10,1,'Io'), MoonVelocity(-2,-2,-1,'Io'),'Io'),
        MoonInfo(MoonPosition(4,10,9,'Europa'), MoonVelocity(-3,7,-2,'Europa'),'Europa'),
        MoonInfo(MoonPosition(8,-10,-3,'Ganymede'), MoonVelocity(5,-1,-2,'Ganymede'),'Ganymede'),
        MoonInfo(MoonPosition(5,-10,3,'Callisto'), MoonVelocity(0,-4,5,'Callisto'),'Callisto')
        ]
        )
        ,
        (20,
        [
        MoonInfo(MoonPosition(-10,3,-4,'Io'), MoonVelocity(-5,2,0,'Io'),'Io'),
        MoonInfo(MoonPosition(5,-25,6,'Europa'), MoonVelocity(1,1,-4,'Europa'),'Europa'),
        MoonInfo(MoonPosition(13,1,1,'Ganymede'), MoonVelocity(5,-2,2,'Ganymede'),'Ganymede'),
        MoonInfo(MoonPosition(0,1,7,'Callisto'), MoonVelocity(-1,-1,2,'Callisto'),'Callisto')
        ]
        )
        ,
        (30,
        [
        MoonInfo(MoonPosition(15,-6,-9,'Io'), MoonVelocity(-5,4,0,'Io'),'Io'),
        MoonInfo(MoonPosition(-4,-11,3,'Europa'), MoonVelocity(-3,-10,0,'Europa'),'Europa'),
        MoonInfo(MoonPosition(0,-1,11,'Ganymede'), MoonVelocity(7,4,3,'Ganymede'),'Ganymede'),
        MoonInfo(MoonPosition(-3,-2,5,'Callisto'), MoonVelocity(1,2,-3,'Callisto'),'Callisto')
        ]
        )
        ,
        (40,
        [
        MoonInfo(MoonPosition(14,-12,-4,'Io'), MoonVelocity(11,3,0,'Io'),'Io'),
        MoonInfo(MoonPosition(-1,18,8,'Europa'), MoonVelocity(-5,2,3,'Europa'),'Europa'),
        MoonInfo(MoonPosition(-5,-14,8,'Ganymede'), MoonVelocity(1,-2,0,'Ganymede'),'Ganymede'),
        MoonInfo(MoonPosition(0,-12,-2,'Callisto'), MoonVelocity(-7,-3,-3,'Callisto'),'Callisto')
        ]
        )
        ,
        (50,
        [
        MoonInfo(MoonPosition(-23,4,1,'Io'), MoonVelocity(-7,-1,2,'Io'),'Io'),
        MoonInfo(MoonPosition(20,-31,13,'Europa'), MoonVelocity(5,3,4,'Europa'),'Europa'),
        MoonInfo(MoonPosition(-4,6,1,'Ganymede'), MoonVelocity(-1,1,-3,'Ganymede'),'Ganymede'),
        MoonInfo(MoonPosition(15,1,-5,'Callisto'), MoonVelocity(3,-3,-3,'Callisto'),'Callisto')
        ]
        )
        ,
        (60,
        [
        MoonInfo(MoonPosition(36,-10,6,'Io'), MoonVelocity(5,0,3,'Io'),'Io'),
        MoonInfo(MoonPosition(-18,10,9,'Europa'), MoonVelocity(-3,-7,5,'Europa'),'Europa'),
        MoonInfo(MoonPosition(8,-12,-3,'Ganymede'), MoonVelocity(-2,1,-7,'Ganymede'),'Ganymede'),
        MoonInfo(MoonPosition(-18,-8,-2,'Callisto'), MoonVelocity(0,6,-1,'Callisto'),'Callisto')
        ]
        )
        ,
        (70,
        [
        MoonInfo(MoonPosition(-33,-6,5,'Io'), MoonVelocity(-5,-4,7,'Io'),'Io'),
        MoonInfo(MoonPosition(13,-9,2,'Europa'), MoonVelocity(-2,11,3,'Europa'),'Europa'),
        MoonInfo(MoonPosition(11,-8,2,'Ganymede'), MoonVelocity(8,-6,-7,'Ganymede'),'Ganymede'),
        MoonInfo(MoonPosition(17,3,1,'Callisto'), MoonVelocity(-1,-1,-3,'Callisto'),'Callisto')
        ]
        )
        ,
        (80,
        [
        MoonInfo(MoonPosition(30,-8,3,'Io'), MoonVelocity(3,3,0,'Io'),'Io'),
        MoonInfo(MoonPosition(-2,-4,0,'Europa'), MoonVelocity(4,-13,2,'Europa'),'Europa'),
        MoonInfo(MoonPosition(-18,-7,15,'Ganymede'), MoonVelocity(-8,2,-2,'Ganymede'),'Ganymede'),
        MoonInfo(MoonPosition(-2,-1,-8,'Callisto'), MoonVelocity(1,8,0,'Callisto'),'Callisto')
        ]
        )
        ,
        (90,
        [
        MoonInfo(MoonPosition(-25,-1,4,'Io'), MoonVelocity(1,-3,4,'Io'),'Io'),
        MoonInfo(MoonPosition(2,-9,0,'Europa'), MoonVelocity(-3,13,-1,'Europa'),'Europa'),
        MoonInfo(MoonPosition(32,-8,14,'Ganymede'), MoonVelocity(5,-4,6,'Ganymede'),'Ganymede'),
        MoonInfo(MoonPosition(-1,-2,-8,'Callisto'), MoonVelocity(-3,-6,-9,'Callisto'),'Callisto')
        ]
        )
        ,
        (100,
        [
        MoonInfo(MoonPosition(8,-12,-9,'Io'), MoonVelocity(-7,3,0,'Io'),'Io'),
        MoonInfo(MoonPosition(13,16,-3,'Europa'), MoonVelocity(3,-11,-5,'Europa'),'Europa'),
        MoonInfo(MoonPosition(-29,-11,-1,'Ganymede'), MoonVelocity(-3,7,4,'Ganymede'),'Ganymede'),
        MoonInfo(MoonPosition(16,-13,23,'Callisto'), MoonVelocity(7,1,1,'Callisto'),'Callisto')
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