from finalPSK import *

map = {
0:complex(1,0), 1:complex(0.9239,0.3827), 2:complex(0.3827,0.9239), 3:complex(0.707,0.707),
4:complex(-0.9239,0.3827), 5:complex(-0.707,0.707), 6:complex(0,1), 7:complex(-0.3827,0.9239),
8:complex(0.9239,-0.3827), 9:complex(0.707,-0.707), 10:complex(0,-1), 11:complex(0.3827,-0.9239),
12:complex(-1,0), 13:complex(-0.9239,-0.3827), 14:complex(-0.3827,-0.9239), 15:complex(-0.707,-0.707)
}

mapper = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
mapper2 = [0,13,14,3,8,5,6,11,4,9,10,7,12,1,2,15]

maps = [mapper, mapper2]
print(fitness(mapper, mapper, map))
print(fitness(mapper, mapper2, map))
Maps = []
for i in range(16):
    ind = random.randint(0, len(maps)-1)
    Maps.append(maps[ind])
Maps = tuple(Maps)
A = []
#print(Maps)
for j in range(10000):
    C = crossoverPopulation(Maps, map)
    M = mutatePopulation(C, 0.08)
    A = AddToPopulation(Maps, M, A)
    #A = AddToPopulation(M, A)
    Maps = nextGeneration(mapper, A, 16, map)
    print(rank_fitness(mapper, Maps, map))
    A = []
print(Maps[0])