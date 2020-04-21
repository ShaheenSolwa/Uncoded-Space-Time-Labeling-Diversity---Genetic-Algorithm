from finalAPSK import *

map = {
0:complex(0.3661,-0.9306),1:complex(0.0316,-0.9588),2:complex(-0.3638,-0.9315),3:complex(-0.8236,-0.5672),
4:complex(-0.9636,-0.26722),5:complex(-0.9588,0.02944),6:complex(-0.9071,0.421),7:complex(-0.6145,0.7889),
8:complex(-0.3162,0.9487),9:complex(0.02091,0.9591),10:complex(0.309,0.9511),11:complex(0.5029,0.8643),
12:complex(0.7425,0.6698),13:complex(0.8558,0.4333),14:complex(0.9758,0.2187),15:complex(0.9976,0.06984)
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
