from finalAPSK import *

map = {
0:complex(-0.8383,0.5452),1:complex(-0.683,0.6787),2:complex(-0.4278,0.9039),3:complex(-0.1602,0.9871),
4:complex(0.1514,0.9885),5:complex(0.3392,0.9010),6:complex(0.6333,0.7739),7:complex(0.8591,0.5117),
8:complex(-0.8383,-0.5452),9:complex(-0.683,-0.6787),10:complex(-0.4278,-0.9039),11:complex(-0.1602,-0.9871),
12:complex(0.1514,-0.9885),13:complex(0.3392,-0.9010),14:complex(0.6333,-0.7739),15:complex(0.8591,-0.5117)
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
