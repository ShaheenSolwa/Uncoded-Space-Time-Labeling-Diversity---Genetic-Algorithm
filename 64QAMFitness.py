from finalQAM import *

map = {
    0:complex(-7,7), 1:complex(-7,5), 2:complex(-7,1), 3:complex(-7,3), 4:complex(-7,-7), 5:complex(-7,-5), 6:complex(-7,-1), 7:complex(-7,-3),
    8:complex(-5,7), 9:complex(-5,5), 10:complex(-5,1), 11:complex(-5,3), 12:complex(-5,-7), 13:complex(-5,-5), 14:complex(-5,-1), 15:complex(-5,-3),
    16:complex(-1,7), 17:complex(-1,5), 18:complex(-1,1), 19:complex(-1,3), 20:complex(-1,-7), 21:complex(-1,-5), 22:complex(-1,-1), 23:complex(-1,-3),
    24:complex(-3,7), 25:complex(-3,5), 26:complex(-3,1), 27:complex(-3,3), 28:complex(-3,-7), 29:complex(-3,-5), 30:complex(-3,-1), 31:complex(-3,-3),
    32:complex(7,7), 33:complex(7,5), 34:complex(7,1), 35:complex(7,3), 36:complex(7,-7), 37:complex(7,-5), 38:complex(7,-1), 39:complex(7,-3),
    40:complex(5,7), 41:complex(5,5), 42:complex(5,1), 43:complex(5,3), 44:complex(5,-7), 45:complex(5,-5), 46:complex(5,-1), 47:complex(5,-3),
    48:complex(1,7), 49:complex(1,5), 50:complex(1,1), 51:complex(1,3), 52:complex(1,-7), 53:complex(1,-5), 54:complex(1,-1), 55:complex(1,-3),
    56:complex(3,7), 57:complex(3,5), 58:complex(3,1), 59:complex(3,3), 60:complex(3,-7), 61:complex(3,-5), 62:complex(3,-1), 63:complex(3,-3)
}


mapper1 = 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20, \
          21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40, \
          41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60, \
          61,62,63

mapper2 = 0,55,52,3,50,5,6,49,62,9,10,61,12,59,56,15,38,17,18,37,20,35,32,23,24,47,44,27,42,29,30,41, \
    22,33,34,21,36,19,16,39,40,31,28,43,26,45,46,25,48,7,51,4,2,53,54,1,14,57,58,13,60,11,8,63

mapper3 = 18,21,16,19,22,17,20,23,42,45,40,43,46,41,44,47,2,5,0,3,6,8,4,7,26,29,24,27,30,25,28,31, \
          50,53,48,51,54,49,52,55,10,13,1,11,14,9,12,15,34,37,32,35,38,33,36,39,58,61,56,59,62,57,60,63

print(fitness(mapper1,mapper2, map))
print(fitness(mapper1,mapper3, map))
maps = [mapper1, mapper2, mapper3]
Maps = []
for i in range(10):
    ind = random.randint(0, len(maps)-1)
    Maps.append(maps[ind])
Maps = tuple(Maps)
A = []
#print(Maps)
for j in range(10000):
    C = crossoverPopulation(Maps, map)
    M = mutatePopulation(C, 0.15)
    A = AddToPopulation(Maps, M, A)
    #A = AddToPopulation(M, A)
    Maps = nextGeneration(mapper1, A, 10, map)
    print(rank_fitness(mapper1, Maps, map))
    A = []
print(Maps[0])