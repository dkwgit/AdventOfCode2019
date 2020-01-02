class Day18DataFixture:

    test1 = (8,"""
#########
#b.A.@.a#
#########
""")

    test2 = (86,"""
########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################
""")

    test3 = (132,"""
########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################
""")

    test4 = (136,"""
#################
#i.G..c...e..H.p#
########.########
#j.A..b...f..D.o#
########@########
#k.E..a...g..B.n#
########.########
#l.F..d...h..C.m#
#################
""")

    test5 = (81,"""
########################
#@..............ac.GI.b#
###d#e#f################
###A#B#C################
###g#h#i################
########################
""")

    mainDay18 = """
#################################################################################
#.........#.............#.....#.....R.#.#.....#...............#.#..v............#
#######.#T#.#######.###.#####.#.###.#.#.#.###.#.#.###.#######.#.#.#####.#######.#
#.....#.#.#.#.......#.#.F...#...#...#...#...#.#.#...#.#.....#.#...#...#...#.....#
#.###.#.#.#.#.#######.#####.###.#.#####.#.#.###.###.###.###.#.#.#####.###.###.###
#.#.#...#.#.#..a..#.......#...#.#.#...#.#.#.......#.......#.#.#.#.....#.#...#...#
#L#.#####.#.#####.#.###.#.###.###.#.###.#.#########.#######.#.#.###.#.#.###.###.#
#.#.......#...#...#...#.#...#...#.#.#...#.....#...#.#.....#.#.#.....#.....#...#.#
#.###########.#.#####.#.###.###.#.#.#.#####.###.#.###.###.#.#.#####.#########.#.#
#.............#.#...#.#.#...#...#.#.#...#.#.#...#.....#...#.#...#...#.........#.#
#.#########.###.###.#.#.#####.###.#.###.#.#.#Z#########.###.###.#.###.#########.#
#...#.....#...#...#...#.......#...#.....#...#...#...#.#...#...#.#...#...#.......#
###.#.###.#######.#.###########.#.#.###########.#.#.#.###.#.#.#.#######.#######.#
#.#.#.#...#.......#.....#.......#.#.....#.......#.#.M.#...#.#.#.#.....#.#.....#.#
#.#.#.#.###.###########.#.#######.#######.#######.#####.#####.#.#.###.#.#.###.###
#.#.#.#.....#...#...G.#.#.....#.#.......#...B.#.#.....#.#..s..#...#.#.#.#.#.#...#
#.#.#.#######.###.#.###.#####.#.#######.#.###.#.#.###.#.#.#########.#.#.#.#.###.#
#...#.#...#.....#.#.#...#.......#.....#.#.#i..#...#.#.....#.....#.....#.....#...#
#.###.#.#.#####.#.#.#.###########.###.#.###.#####.#.#######.###X#.###########.#.#
#.#.#...#.#..c..#.#.....#.......#h#.#...#...#...#.....#..x#...#.#.#.........#.#.#
#.#.#####.#.#####.#####.#.#####.#.#.###W#.###.#Y#######D#.#.###.#.#####.###.#Q###
#...#...#.#.#.....#b..#...#.#...#.#...#.#...#.#....n..#.#...#.#.#.#.....#...#...#
###.#.#.#.#.#.#####.#######.#.###.#.#.#.#.#.#.#######.#.#####.#.#.#.#####.#####.#
#.#.#.#.#.#.......#.....#...#.....#.#.#.#.#.#.#.#.....#...#...#.#.#.#.#...#.....#
#.#.#.#.#.#.###########.###.#######.#.#.###.#.#.#N#######.#E###.#.#.#.#.###.###.#
#...#.#...#.#.#.....#...#.........#.#.#.#pI.#...#......d..#....e#...#.#.....#.#.#
#####.#####.#.#.###.#.###.#########.#.#.#.#####.#####################.#######.#.#
#.....#...#.#.#...#...#.......#.....#.#.#.....#y#.....................#.........#
#.#####.###.#.###.#####.#####.#.#####.#.#####.#.#.###########.###.###.#.#########
#...#.......#...#...#.#.#.#...#.#.....#.#...#.#.#...#.#.....#.#...#...#.........#
#.#.#.#########.###.#.#.#.#.#.#.#.###.#.###.#.#.###.#.#.###.###.###.###########.#
#.#.#.#...........#.#...#.#.#.#.#...#.#.#...#.P.#.....#.#.......#.........#...#.#
#.#.#.#.#####.#####.#.###.#.###.###.#.#.#.###########.#.#.#####.#########.#.#.#C#
#.#.#...#.#...#...#.#.....#...#.#.#.#.#.#.#.........#.#.#.#...#.#.....#.#...#.#.#
#.#.#####.#.###.#.#.#####.###.#.#.#.###.#.#.###.###.###.###.#.###.###.#.#.#####.#
#.#.#.......#.#.#.#.#.....#.#.#.#.#...#.#.#...#...#.....#...#.#...#.#.#.#.#.....#
###.#.#######.#.#.#.#.#####.#.#.#.###.#.#.###.###.###.###.###.#.###.#.#.#.#.#####
#...#.........#.#...#.#.....#...#...#.#.#.....#.#.#...#...#...#...#.#.#..o#...#.#
#.#############.#####.#####.#######.#.#.#.#####.#.#####.###.#####.#.#.#######.#.#
#...........U...#...................#...........#.........#.........#...........#
#######################################.@.#######################################
#.....#.O.#.....#.......#...#.....#...........#.....#.............#...#...#..k..#
#####.#.#.#.#.#.###.###.#.###.#.###.###.#.###.###.#.###.#####.###.#.#.#.#.#.#.#.#
#...#...#...#.#...#...#.#.#...#.....#...#...#...#.#...#.#.....#...#.#.#.#...#.#.#
#.#.#.#######.###.###.#.#.#.#########.#.###.###.#.###.#.#.#.#####.#.#.#######.#.#
#.#.#...#.....#.#...#.#...#...#...#...#.#...#...#.#...#.#.#.#...#.#.#..u#.....#.#
#.#.#####.#####.###.#.#######.###.#.###.#.#####.#.#.###.#.###.#.###.###.#.#####.#
#.#.......#.........#.......#...#.#.#...#.....#...#...#.#.#...#.....#.#.#.#.....#
#.#########.###########.###.###.#.#.#.#######.#######H###.#.#########.#.#.#######
#.....#...#...#.......#...#.......#.#.#.#.....#.....#.#...#.#.........#.#.#.....#
#####.#.#.###.#####.#.###.#########.#.#.#.#####.#.###.#.#.#.###.###.#.#.#.#.###.#
#.....#.#...#....r..#.#.....#...#...#..w#.#.....#.......#.#...#.#...#.#.#.....#.#
#.#####.#############.#######.#.#.#####.#.###.###############.#.#.###.#.#######.#
#.#.....#.....#...............#...#.#...#...#.......#.......#.#.#...#.#...#.....#
#.###.###.#.###.###################.#.###.#.#########.#####.#.#####.#####.#.###.#
#..q#.....#.....#...#.......#...#.....#.#.#...........#.#...#.....#.....#.#.#.#.#
###.#.###########.#.#.#####.#.###.#####.#.#############.#.#.#####.#.#.###.#.#.#.#
#.#.#.......#.....#...#...#.#...#.......#.#...#...#.....#.#.....#z#.#...#.#.#.#.#
#.#.#######.#.#########.#.#.#.#.#######.#.#.#.#.#.#####.#.###.###.#####.#.#.#.#.#
#.#.....#...#.....#.#...#...#.#.......#.#.#.#...#.......#.#...#...#.....#.#.#...#
#.#####.#########.#.#.#########.#######.#.#.#######.#####.#.###.###.###.#.#.###.#
#.....#.#...#.....#.#.#.K.......#.......#.#.#.....#.#.....#.#.#.#...#...#.#...#.#
#.#.###.#.#.#.#####.#####.#.#####.#######.#.###.#.#.#.#######.#.#.###.###.#.#.#.#
#.#...#...#.#.#.....#.....#.#.....#.....#.#...#.#...#.#.....#...#...#...#.#.#.#.#
#.###.#####.#.#.###.#.###.###.#####.#.#.#.###.#####.#.#.###.#####.#.###.#.###.#.#
#...#.#...#...#...#...#...#...#...#.#.#.#...#.#...#.#.....#.....#.#...#.#.J...#.#
###.#.#.#.#######.#####.###.###.#.###.#.###.#.#.#.#########.###.#.###.#########.#
#.#.#...#.........#...#...#.#...#...#.#.#.#.#...#...#.....#.#...#...#.#.........#
#.#.#######.#.#######.###.#.#.#####.#.#.#.#.#.#####.#.###.#.#.###.###.#.#########
#.#.#.....#.#.#.....#...#.#.#.#...#...#.#...#.#...#.#.#.#...#.#...#...#.#.......#
#.#.#.#####V#.#.###.#.###.#.#.#.#.#####.#.#####.#.#.#.#.#####.#.###.###.#.###.#.#
#...#...#...#j#...#.#...#.#...#.#.....#.#...#...#...#.#.......#...#.....#...#.#.#
#.#####.#.#######.#.###.#.#####.###.###.###.#.#####.#.###.#######.###########.#.#
#.......#.......#.#...#.#.#.......#.#...#...#...#...#...#.#...#...#...#.....#.#l#
#######.#####.#.#.###.#.#.#.#####.#.#.###.###.#.#.#####.###.#.#.###.#.#.#.#.#.#.#
#.....#.....#.#.#...#.#.#.#...#...#.#...#...#.#.#.....#.#...#...#...#...#.#...#.#
#.###.#####.#.###.###.#.#.###.#.#######.###.#.#.#######.#.#######.#######.#####.#
#.#..m..#...#.....#...#.....#.#.......#f#...#.#...#.....#.#...........#...#..t#.#
#.#.#####.#########.#########.#######.#.#.#######.#.#####.#############.###.###.#
#.#.......S.......#.....A...........#...#g........#.....................#.......#
#################################################################################
"""