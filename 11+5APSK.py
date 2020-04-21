from finalAPSK import *

map = {
0:complex(-1.1011,0.3233),1:complex(-0.1633,-1.1359),2:complex(0.9654,-0.6204),3:complex(0.9654,0.6204),4:complex(-0.1633,1.1359),
5:complex(0.4767,1.0439),6:complex(-0.445,-0.3233),7:complex(1.1476,0),
8:complex(0.16999,-0.5232),9:complex(-1.1011,-0.3233),10:complex(0.5516,0),11:complex(-0.7515,0.8673),
12:complex(0.4767,-1.0439),13:complex(0.16999,0.5232),14:complex(-0.7515,-0.8673),15:complex(-0.445,0.3233)
}


mapper = 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
#mapper2 = [12,10,13,9,15,11,8,14,6,5,7,3,1,4,0,2]

maps = [mapper]
print(fitness(mapper, mapper, map))
#print(fitness(mapper, mapper2, map))
Maps = []
for i in range(8):
    ind = random.randint(0, len(maps)-1)
    Maps.append(maps[ind])
Maps = tuple(Maps)
A = []
#print(Maps)
for j in range(10000):
    C = crossoverPopulation(Maps, map)
    M = mutatePopulation(C, 0.10)
    A = AddToPopulation(Maps, M, A)
    #A = AddToPopulation(M, A)
    Maps = nextGeneration(mapper, A, 8, map)
    print(rank_fitness(mapper, Maps, map))
    A = []
print(Maps[0])
