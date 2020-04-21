from finalPSK import *

map = {
    0:complex(1,0), 1:complex(0.707,0.707), 2:complex(-0.707,0.707), 3:complex(0,1),
    4:complex(0.707,-0.707), 5:complex(0,-1), 6:complex(-1,0), 7:complex(-0.707,-0.707)
}

mapper = [0,1,2,3,4,5,6,7]
mapper2 = [0,7,3,4,6,1,5,2]

maps = [mapper, mapper2]
print(fitness(mapper, mapper, map))
print(fitness(mapper, mapper2, map))
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