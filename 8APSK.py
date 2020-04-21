from finalAPSK import *

map = {
0:complex(-0.1471,0), 1:complex(-0.3508,-0.6993), 2:complex(-0.3508,0.6993), 3:complex(-1,0),
4:complex(0.1471,0), 5:complex(0.3508,-0.6993), 6:complex(0.3508,0.6993), 7:complex(1,0),
}

mapper = [0,1,2,3,4,5,6,7]
mapper2 = [5,7,1,0,2,3,6,4]

maps = [mapper]
print(fitness(mapper, mapper2, map))
#print(fitness(mapper, mapper2, map))
Maps = []
for i in range(7):
    ind = random.randint(0, len(maps)-1)
    Maps.append(maps[ind])
Maps = tuple(Maps)
A = []
#print(Maps)
for j in range(200):
    C = crossoverPopulation(Maps, map)
    M = mutatePopulation(C, 0.03)
    A = AddToPopulation(Maps, M, A)
    #A = AddToPopulation(M, A)
    Maps = nextGeneration(mapper, A, 7, map)
    print(rank_fitness(mapper, Maps, map))
    A = []
print(Maps[0])