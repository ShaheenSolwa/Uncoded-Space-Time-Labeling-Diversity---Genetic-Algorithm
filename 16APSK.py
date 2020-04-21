from finalAPSK import *

map = {
0:complex(0.4619,0.1913), 1:complex(0.1913,0.4619), 2:complex(-0.4619,0.1913),3:complex(-0.1913,0.4619),
4:complex(0.4619,-0.1913), 5:complex(0.1913,-0.4619), 6:complex(-0.4619,-0.1913), 7:complex(-0.1913,-0.4619),
8:complex(0.9239,0.3827), 9:complex(0.3827,0.9239), 10:complex(-0.9239,0.3827), 11:complex(-0.3827,0.9239),
12:complex(0.9239,-0.3827), 13:complex(0.3827,-0.9239), 14:complex(-0.9239,-0.38227), 15:complex(-0.3827,-0.9239)
}

mapper = 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
mapper2 = [12,10,13,9,15,11,8,14,6,5,7,3,1,4,0,2]

maps = [mapper,mapper2]
print(fitness(mapper, mapper2, map))
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