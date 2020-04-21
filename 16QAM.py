from finalQAM import *


map = {
    0:complex(-3,-3), 1:complex(-3,-1), 2:complex(-3,3), 3:complex(-3,1),
    4:complex(-1,-3), 5:complex(-1,-1), 6:complex(-1,3), 7:complex(-1,1),
    8:complex(3,-3), 9:complex(3,-1), 10:complex(3,3), 11:complex(3,1),
    12:complex(1,-3), 13:complex(1,-1), 14:complex(1,3), 15:complex(1,1),
}
mapper1 = 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15#gray
mapper2 = 13,11,15,9,6,0,4,2,12,10,14,8,7,1,5,3#samra
mapper3 = 15,1,2,12,4,10,9,7,8,6,5,11,3,13,14,0#xu
mapper4 = 7,4,5,6,11,8,9,10,15,12,13,14,3,0,1,2#seddik
mapper5 = 0,10,7,13,9,3,14,4,12,5,11,2,6,15,1,8#huang
mapper6 = 6,10,0,5,3,15,12,9,13,1,11,14,8,4,7,2#krasicki 1
mapper7 = 4,7,2,8,14,13,1,11,9,10,15,5,3,0,12,6#krasicki 2

maps = [mapper2, mapper3, mapper4, mapper5, mapper6, mapper7]
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
    Maps = nextGeneration(mapper1, A, 8, map)
    print(rank_fitness(mapper1, Maps, map))
    A = []
print(Maps[-1])