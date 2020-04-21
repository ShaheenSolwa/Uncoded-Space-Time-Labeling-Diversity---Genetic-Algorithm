from finalAPSK import *

map = {
0:complex(0.3646,0),1:complex(0.2273,0.2851),2:complex(-0.0811,0.3555),3:complex(-0.3285,0.1582),
4:complex(-0.3285,-0.1582),5:complex(-0.0811,-0.3555),6:complex(0.2273,-0.2851),7:complex(0.6611,0),
8:complex(0.5854,0.3072),9:complex(0.3756,0.5441),10:complex(0.0797,0.6563),11:complex(-0.2344,0.6182),
12:complex(-0.4948,0.4384),13:complex(-0.6419,0.1583),14:complex(-0.6419,-0.1583),15:complex(-0.4949,-0.4383),
16:complex(-0.2346,-0.6181),17:complex(0.0795,-0.6563),18:complex(0.3754,-0.5442),19:complex(0.5853,-0.3074),
20:complex(0.9612,0),21:complex(0.3128,0.1074),22:complex(0.261,0.2031),23:complex(0.1809,0.2769),
24:complex(0.08117,0.3206),25:complex(-0.0273,0.3296),26:complex(-0.1329,0.3028),27:complex(-0.224,0.2433),
28:complex(-0.2908,0.1574),29:complex(-0.3262,0.05441),30:complex(-0.3262,-0.05441),31:complex(-0.2908,-0.1574),
32:complex(-0.2248,-0.2425),33:complex(-0.1353,-0.3018),34:complex(-0.0273,-0.3296),35:complex(0.0812,-0.3206),
36:complex(0.181,-0.2768),37:complex(0.2604,-0.2038),38:complex(0.3128,-0.1073),39:complex(1.2623,0),
40:complex(1.2223,0.3139),41:complex(1.1062,0.6081),42:complex(0.9202,0.864),43:complex(0.6765,1.0657),
44:complex(0.3902,1.2005),45:complex(0.0795,1.2598),46:complex(-0.2363,1.24),47:complex(-0.5372,1.1423),
48:complex(-0.8044,0.9728),49:complex(-1.021,0.742),50:complex(-1.1735,0.465),51:complex(-1.2523,0.1586),
52:complex(-1.2524,-0.1578),53:complex(-1.1738,-0.4642),54:complex(-1.0215,-0.7415),55:complex(-0.805,-0.9723),
56:complex(-0.538,-1.1419),57:complex(-0.2371,-1.2398),58:complex(0.0786,-1.2599),59:complex(0.3894,-1.2007),
60:complex(0.6758,-1.0662),61:complex(0.9197,-0.8647),62:complex(1.1058,-0.6088),63:complex(1.2224,-0.3147),
}

mapper = 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,\
         32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63

#mapper2 = 46,63,14,10,9,25,3,35,43,38,54,60,2,51,11,24,31,34,16,18,21,40,61,37,53,30,6,41,4,8,49,62,22,17,39,56,48,44,1,32,47,12,29,58,27,5,19,13,36,20,42,28,55,33,7,50,0,45,52,59,57,26,15,23


maps = [mapper]
print(fitness(mapper, mapper, map))
#print(fitness(mapper, mapper2, map))
Maps = []
for i in range(10):
    ind = random.randint(0, len(maps)-1)
    Maps.append(maps[ind])
Maps = tuple(Maps)
A = []
#print(Maps)
for j in range(100000):
    C = crossoverPopulation(Maps, map)
    M = mutatePopulation(C, 0.20)
    A = AddToPopulation(Maps, M, A)
    #A = AddToPopulation(M, A)
    Maps = nextGeneration(mapper, A, 10, map)
    print(rank_fitness(mapper, Maps, map))
    A = []
print(Maps[0])