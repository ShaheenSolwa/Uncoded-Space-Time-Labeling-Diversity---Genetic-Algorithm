from finalQAM import *

map = {
    0:complex(-7,9),1:complex(-7,11),2:complex(-1,9),3:complex(-1,11),4:complex(-7,-9),5:complex(-7,-11),6:complex(-1,-9),7:complex(-1,-11),8:complex(-5,9),9:complex(-5,11),10:complex(-3,9),11:complex(-3,11),12:complex(-5,-9),13:complex(-5,-11),14:complex(-3,-9),15:complex(-3,-11),
    16:complex(-9,7),17:complex(-9,5),18:complex(-9,1),19:complex(-9,3),20:complex(-9,-7),21:complex(-9,-5),22:complex(-9,-1),23:complex(-9,-3),24:complex(-11,7),25:complex(-11,5),26:complex(-11,1),27:complex(-11,3),28:complex(-11,-7),29:complex(-11,-5),30:complex(-11,-1),31:complex(-11,-3),
    32:complex(-1,7),33:complex(-1,5),34:complex(-1,1),35:complex(-1,3),36:complex(-1,-7),37:complex(-1,-5),38:complex(-1,-1),39:complex(-1,-3),40:complex(-3,7),41:complex(-3,5),42:complex(-3,1),43:complex(-3,3),44:complex(-3,-7),45:complex(-3,-5),46:complex(-3,-1),47:complex(-3,-3),
    48:complex(-7,7),49:complex(-7,5),50:complex(-7,1),51:complex(-7,3),52:complex(-7,-7),53:complex(-7,-5),54:complex(-7,-1),55:complex(-7,-3),56:complex(-5,7),57:complex(-5,5),58:complex(-5,1),59:complex(-5,3),60:complex(-5,-7),61:complex(-5,-5),62:complex(-5,-1),63:complex(-5,-3),
    64:complex(7,9),65:complex(7,11),66:complex(1,9),67:complex(1,11),68:complex(7,-9),69:complex(7,-11),70:complex(1,-9),71:complex(1,-11),72:complex(5,9),73:complex(5,11),74:complex(3,9),75:complex(3,11),76:complex(5,-9),77:complex(5,-11),78:complex(3,-9),79:complex(3,-11),
    80:complex(9,7),81:complex(9,5),82:complex(9,1),83:complex(9,3),84:complex(9,-7),85:complex(9,-5),86:complex(9,-1),87:complex(9,-3),88:complex(11,7),89:complex(11,5),90:complex(11,1),91:complex(11,3),92:complex(11,-7),93:complex(11,-5),94:complex(11,-1),95:complex(11,-3),
    96:complex(1,7),97:complex(1,5),98:complex(1,1),99:complex(1,3),100:complex(1,-7),101:complex(1,-5),102:complex(1,-1),103:complex(1,-3),104:complex(3,7),105:complex(3,5),106:complex(3,1),107:complex(3,3),108:complex(3,-7),109:complex(3,-5),110:complex(3,-1),111:complex(3,-3),
    112:complex(7,7),113:complex(7,5),114:complex(7,1),115:complex(7,3),116:complex(7,-7),117:complex(7,-5),118:complex(7,-1),119:complex(7,-3),120:complex(5,7),121:complex(5,5),122:complex(5,1),123:complex(5,3),124:complex(5,-7),125:complex(5,-5),126:complex(5,-1),127:complex(5,-3)
}

mapper1 = tuple(x for x in range(0,128))
mapper2 = 84,1,2,94,4,122,91,7,8,93,87,11,115,13,14,82,68,17,18,78,20,104,75,23,24,77,71,27,97,29,30,66,118,33,34,110,36,88,112,39,40,127,103,43,81,45,46,121,48,124,100,51,98,\
    53,54,72,117,57,58,109,60,107,65,63,64,62,31,67,16,69,70,26,55,73,74,22,76,25,19,79,80,44,15,83,0,85,86,10,37,89,90,6,92,9,3,95,96,28,52,99,50,101,102,42,21,105,106,61,108,59,35,111,\
    38,113,114,12,116,56,32,119,120,47,5,123,49,125,126,41

maps = [mapper1, mapper2]
print(fitness(mapper1, mapper1, map))
print(fitness(mapper1, mapper2, map))
Maps = []
for i in range(15):
    ind = random.randint(0, len(maps)-1)
    Maps.append(maps[ind])
Maps = tuple(Maps)
A = []
#print(Maps)
for j in range(10000):
    C = crossoverPopulation(Maps, map)
    M = mutatePopulation(C, 0.25)
    A = AddToPopulation(Maps, M, A)
    #A = AddToPopulation(M)
    Maps = nextGeneration(mapper1, A, 15, map)
    print(rank_fitness(mapper1, Maps, map))
    A = []
print(Maps[0])