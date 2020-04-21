from finalQAM import *

map = {
    0:complex(-3,5), 1:complex(-1,5), 2:complex(-3,-5), 3:complex(-1,-5), 4:complex(-5,3), 5:complex(-5,1), 6:complex(-5,-3), 7:complex(-5,-1),
    8:complex(-1,3), 9:complex(-1,1), 10:complex(-1,-3), 11:complex(-1,-1), 12:complex(-3,3), 13:complex(-3,1), 14:complex(-3,-3), 15:complex(-3,-1),
    16:complex(3,5), 17:complex(1,5), 18:complex(3,-5), 19:complex(1,-5), 20:complex(5,3), 21:complex(5,1), 22:complex(5,-3), 23:complex(5,-1),
    24:complex(1,3), 25:complex(1,1), 26:complex(1,-3), 27:complex(1,-1), 28:complex(3,3), 29:complex(3,1), 30:complex(3,-3), 31:complex(3,-1)
}

mapper1 = 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31

mapper2 = 31,1,2,21,26,5,6,17,22,9,10,28,12,18,25,15,16,7,13,19,20,3,8,23,24,14,4,27,11,29,30,0

maps = [mapper1, mapper2]
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
    #A = AddToPopulation(M)
    Maps = nextGeneration(mapper1, A, 12, map)
    print(rank_fitness(mapper1, Maps, map))
    A = []
print(Maps[0])