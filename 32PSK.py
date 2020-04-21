from finalPSK import *

map = {
0:complex(1,0), 1:complex(0.9808,0.1951), 2:complex(0.8315,0.5556), 3:complex(0.9239,0.3827),
4:complex(0.1951,0.9809), 5:complex(0.3827,0.9239), 6:complex(0.707,0.707), 7:complex(0.5556,0.8315),
8:complex(-0.9808,0.1951), 9:complex(-0.9239,0.3827), 10:complex(-0.707,0.707), 11:complex(-0.8315,0.5556),
12:complex(0,1), 13:complex(-0.1951,0.9808), 14:complex(-0.5556,0.8315), 15:complex(-0.3827,0.9239),
16:complex(0.9808,-0.1951), 17:complex(0.9239,-0.3827), 18:complex(0.707,-0.707), 19:complex(0.8315,-0.5556),
20:complex(0,-1), 21:complex(0.1951,-0.9808), 22:complex(0.5556,-0.8315), 23:complex(0.3827,-0.9239),
24:complex(-1,0), 25:complex(-0.9808,-0.1951), 26:complex(-0.8315,-0.5556), 27:complex(-0.9239,-0.3827),
28:complex(-0.1951,-0.9808), 29:complex(-0.3827,-0.9239), 30:complex(-0.707,-0.707), 31:complex(-0.5556,-0.8315)
}

mapper = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
mapper2 = [31,1,2,28,27,5,6,24,23,9,10,20,19,13,14,16,15,17,18,12,11,21,22,8,7,25,26,4,3,29,30,0]

maps = [mapper, mapper2]
print(fitness(mapper, mapper, map))
print(fitness(mapper, mapper2, map))
Maps = []
for i in range(12):
    ind = random.randint(0, len(maps)-1)
    Maps.append(maps[ind])
Maps = tuple(Maps)
A = []
#print(Maps)
for j in range(100000):
    C = crossoverPopulation(Maps, map)
    M = mutatePopulation(C, 0.12)
    A = AddToPopulation(Maps, M, A)
    #A = AddToPopulation(M, A)
    Maps = nextGeneration(mapper, A, 12, map)
    print(rank_fitness(mapper, Maps, map))
    A = []
print(Maps[0])