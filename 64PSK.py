from finalPSK import *

map = {
0:complex(1,0), 1:complex(0.9952,0.0980), 2:complex(0.9569,0.2903), 3:complex(0.9808,0.1951),
4:complex(0.7730,0.6344), 5:complex(0.8315,0.5556), 6:complex(0.9239,0.3827), 7:complex(0.8819,0.4714),
8:complex(0.0980,0.9952), 9:complex(0.1951,0.9808), 10:complex(0.3827,0.9239), 11:complex(0.2903,0.9569),
12:complex(0.7071,0.7071), 13:complex(0.6344,0.7730), 14:complex(0.4714,0.8819), 15:complex(0.5556,0.8315),

16:complex(-0.9952,0.0980), 17:complex(-0.9808,0.1951), 18:complex(-0.9239,0.3827), 19:complex(-0.9569,0.2903),
20:complex(-0.7071,0.7071), 21:complex(-0.7730,0.6344), 22:complex(-0.8819,0.4714), 23:complex(-0.8315,0.5556),
24:complex(0,1), 25:complex(-0.0980,0.9952), 26:complex(-0.2903,0.9569), 27:complex(-0.1951,0.9808),
28:complex(-0.6344,0.7730), 29:complex(-0.5556,0.8315), 30:complex(-0.3827,0.9239), 31:complex(-0.4714,0.8819),

32:complex(0.9952,-0.0980), 33:complex(0.9808,-0.1951), 34:complex(0.9239,-0.3827), 35:complex(0.9569,-0.2903),
36:complex(0.7071,-0.7071), 37:complex(0.7730,-0.6344), 38:complex(0.8819,-0.4714), 39:complex(0.8315,-0.5556),
40:complex(0,-1), 41:complex(0.0980,-0.9952), 42:complex(0.2903,-0.9569), 43:complex(0.1951,-0.9808),
44:complex(0.6344,-0.7730), 45:complex(0.5556,-0.8315), 46:complex(0.3827,-0.9239), 47:complex(0.4714,-0.8819),

48:complex(-1,0), 49:complex(-0.9952,-0.0980), 50:complex(-0.9569,-0.2903), 51:complex(-0.9808,-0.1951),
52:complex(-0.7730,-0.6344), 53:complex(-0.8315,-0.5556), 54:complex(-0.9239,-0.3827), 55:complex(-0.8819,-0.4714),
56:complex(-0.0980,-0.9952), 57:complex(-0.1951,-0.9808), 58:complex(-0.3827,-0.9239), 59:complex(-0.2903,-0.9569),
60:complex(-0.7071,-0.7071), 61:complex(-0.6344,-0.7730), 62:complex(-0.4714,-0.8819), 63:complex(-0.5556,-0.8315),
}

mapper = 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,\
         32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63

maps = [mapper]
print(fitness(mapper, mapper, map))
#print(fitness(mapper, mapper2, map))
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