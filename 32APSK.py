from finalAPSK import *

map = {
0:complex(0.707,0.707), 1:complex(-0.707,0.707), 2:complex(0.707,-0.707),3:complex(-0.707,-0.707),
4:complex(3.696,1.531), 5:complex(-3.696,1.531), 6:complex(3.696,-1.531), 7:complex(-3.696,-1.531),
8:complex(3.536,3.536), 9:complex(-3.536,3.536), 10:complex(3.536,-3.536), 11:complex(-3.536,-336),
12:complex(1.531,3.696), 13:complex(-1.531,3.696), 14:complex(1.531,-3.696), 15:complex(-1.531,-396),
16:complex(1.951,9.808), 17:complex(-1.951,9.808), 18:complex(1.951,-9.808), 19:complex(-1.951,-908),
20:complex(5.556,8.315), 21:complex(-5.556,8.315), 22:complex(5.556,-8.315), 23:complex(-5.556,-8.315),
24:complex(9.808,1.951), 25:complex(-9.808,1.951), 26:complex(9.808,-1.951), 27:complex(-9.808,-1.951),
28:complex(8.315,5.556), 29:complex(-8.315,5.556), 30:complex(8.315,-5.556), 31:complex(-8.315,-5.556)
}

mapper = 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31

mapper2 = 29,17,19,3,23,6,16,24,1,18,15,7,26,31,13,0,11,10,14,2,5,25,21,28,30,4,9,20,12,8,22,27

maps = [mapper]
print(fitness(mapper, mapper2, map))
#print(fitness(mapper, mapper2, map))
Maps = []
for i in range(12):
    ind = random.randint(0, len(maps)-1)
    Maps.append(maps[ind])
Maps = tuple(Maps)
A = []
#print(Maps)
for j in range(10000):
    C = crossoverPopulation(Maps, map)
    M = mutatePopulation(C, 0.12)
    A = AddToPopulation(Maps, M, A)
    #A = AddToPopulation(M, A)
    Maps = nextGeneration(mapper, A, 12, map)
    print(rank_fitness(mapper, Maps, map))
    A = []
print(Maps[0])