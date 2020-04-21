from finalAPSK import *

map = {
0:complex(0.7071,0.7071), 1:complex(-0.7071,0.7071), 2:complex(0.7071,-0.7071), 3:complex(-0.7071,-0.7071),
4:complex(2.8978,0.7765), 5:complex(-2.8978,0.7765), 6:complex(2.8978,-0.7765), 7:complex(-2.8978,-0.7765),
8:complex(0.7765,2.8978), 9:complex(-0.7765,2.8978), 10:complex(0.7765,-2.8978), 11:complex(-0.7765,-2.8978),
12:complex(2.1213,2.1213), 13:complex(-2.1213,2.1213), 14:complex(2.1213,-2.1213), 15:complex(-2.1213,-2.1213),

16:complex(2.7239,5.3460), 17:complex(-2.7239,5.3460), 18:complex(2.7239,-5.3460), 19:complex(-2.7239,-5.3460),
20:complex(4.2426,4.2426), 21:complex(-4.2426,4.2426), 22:complex(4.2426,-4.2426), 23:complex(-4.2426,-4.2426),
24:complex(5.9261,0.9386), 25:complex(-5.9261,0.9386), 26:complex(5.9261,-0.9386), 27:complex(-5.9261,-0.9386),
28:complex(5.3460,2.7239), 29:complex(-5.3460,2.7239), 30:complex(5.3460,-2.7239), 31:complex(-5.3460,-2.7239),

32:complex(1.1196,9.9371), 33:complex(-1.1196,9.9371), 34:complex(1.1196,-9.9371), 35:complex(-1.1196,-9.9371),
36:complex(3.3028,9.4388), 37:complex(-3.3028,9.4388), 38:complex(3.3028,-9.4388), 39:complex(-3.3028,-9.4388),
40:complex(7.0711,7.0711), 41:complex(-7.0711,7.0711), 42:complex(7.0711,-7.0711), 43:complex(-7.0711,-7.0711),
44:complex(5.3203,8.4672), 45:complex(-5.3203,8.4672), 46:complex(5.3203,-8.4672), 47:complex(-5.3203,-8.4672),

48:complex(0.9386,5.9261), 49:complex(-0.9386,5.9261), 50:complex(0.9386,-5.9261), 51:complex(-0.9386,-5.9261),
52:complex(9.9371,1.1196), 53:complex(-9.9371,1.1196), 54:complex(9.9371,-1.1196), 55:complex(-9.9371,-1.1196),
56:complex(8.4672,5.3203), 57:complex(-8.4672,5.3203), 58:complex(8.4672,-5.3203), 59:complex(-8.4672,-5.3203),
60:complex(9.4388,3.3028), 61:complex(-9.4388,3.3028), 62:complex(9.4388,-3.3028), 63:complex(-9.4388,-3.3028),
}

mapper = 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,\
         32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63

mapper2 = 46,63,14,10,9,25,3,35,43,38,54,60,2,51,11,24,31,34,16,18,21,40,61,37,53,30,6,41,4,8,49,62,22,17,\
    39,56,48,44,1,32,47,12,29,58,27,5,19,13,36,20,42,28,55,33,7,50,0,45,52,59,57,26,15,23


maps = [mapper]
print(fitness(mapper, mapper, map))
print(fitness(mapper, mapper2, map))
Maps = []
for i in range(10):
    ind = random.randint(0, len(maps)-1)
    Maps.append(maps[ind])
Maps = tuple(Maps)
A = []
#print(Maps)
for j in range(10000):
    C = crossoverPopulation(Maps, map)
    M = mutatePopulation(C, 0.15)
    A = AddToPopulation(Maps, M, A)
    #A = AddToPopulation(M, A)
    Maps = nextGeneration(mapper, A, 10, map)
    print(rank_fitness(mapper, Maps, map))
    A = []
print(Maps[0])