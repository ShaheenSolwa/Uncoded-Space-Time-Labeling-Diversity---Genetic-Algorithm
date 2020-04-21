from finalAPSK import *

map = {
0:complex(0.2563,0.0538),1:complex(0.9463,0.3232),2:complex(0.9976,0.0691),3:complex(0.9789,0.2043),4:complex(0.444,0.0675),5:complex(0.5362,0.1415),6:complex(0.7176,0.0596),7:complex(0.6773,0.1847),8:complex(0.2193,0.143),9:complex(0.8977,0.4406),10:complex(0.7543,0.6565),
11:complex(0.837,0.5473),12:complex(0.3618,0.266),13:complex(0.4794,0.2788),14:complex(0.5499,0.4649),15:complex(0.6093,0.3487),16:complex(0.0540,0.2562),17:complex(0.3226,0.9465),18:complex(0.0698,0.9976),19:complex(0.2043,0.9789),20:complex(0.0675,0.444),
21:complex(0.1415,0.5362),22:complex(0.0596,0.7176),23:complex(0.1842,0.6774),24:complex(0.143,0.2193),25:complex(0.4401,0.898),26:complex(0.6561,0.7547),27:complex(0.5478,0.8366),28:complex(0.266,0.3618),29:complex(0.2794,0.4791),30:complex(0.4653,0.5496),
31:complex(0.3487,0.6093),32:complex(-0.2563,0.0538),33:complex(-0.9463,0.3232),34:complex(-0.9976,0.0691),35:complex(-0.9789,0.2043),36:complex(-0.444,0.0675),37:complex(-0.5362,0.1415),38:complex(-0.7176,0.0596),39:complex(-0.6773,0.1847),40:complex(-0.2193,0.143),
41:complex(-0.8977,0.4406),42:complex(-0.7543,0.6565),43:complex(-0.837,0.5473),44:complex(-0.3618,0.266),45:complex(-0.4794,0.2788),46:complex(-0.5499,0.4649),47:complex(-0.6093,0.3487),48:complex(-0.054,0.2562),49:complex(-0.3226,0.9465),50:complex(-0.0698,0.9976),
51:complex(-0.2043,0.9789),52:complex(-0.0675,0.444),53:complex(-0.1415,0.5362),54:complex(-0.0596,0.7176),55:complex(-0.1842,0.6774),56:complex(-0.143,0.2193),57:complex(-0.4401,0.898),58:complex(-0.6561,0.7547),59:complex(-0.5478,0.8366),
60:complex(-0.266,0.3618),61:complex(-0.2794,0.4791),62:complex(-0.4653,0.5496),63:complex(-0.3487,0.6093),64:complex(0.2563,-0.0538),65:complex(0.9463,-0.3232),66:complex(0.9976,-0.0691),67:complex(0.9789,-0.2043),68:complex(0.444,-0.0675),69:complex(0.5362,-0.1415),
70:complex(0.7176,-0.0596),71:complex(0.6773,-0.1847),72:complex(0.2193,-0.143),73:complex(0.8977,-0.4406),74:complex(0.7543,-0.6565),75:complex(0.837,-0.5473),76:complex(0.3618,-0.266),77:complex(0.4794,-0.2788),78:complex(0.5499,-0.4649),79:complex(0.6093,-0.3487),
80:complex(0.0540,-0.2562),81:complex(0.3226,-0.9465),82:complex(0.0698,-0.9976),83:complex(0.2043,-0.9789),84:complex(0.0675,-0.444),85:complex(0.1415,-0.5362),86:complex(0.0596,-0.7176),87:complex(0.1842,-0.6774),88:complex(0.143,-0.2193),89:complex(0.4401,-0.898),
90:complex(0.6561,-0.7547),91:complex(0.5478,-0.8366),92:complex(0.266,-0.3618),93:complex(0.2794,-0.4791),94:complex(0.4653,-0.5496),95:complex(0.3487,-0.6093),96:complex(-0.2563,-0.0538),97:complex(-0.9463,-0.3232),98:complex(-0.9976,-0.0691),99:complex(-0.9789,-0.2043),
100:complex(-0.444,-0.0675),101:complex(-0.5362,-0.1415),102:complex(-0.7176,-0.0596),103:complex(-0.6773,-0.1847),104:complex(-0.2193,-0.143),105:complex(-0.8977,-0.4406),106:complex(-0.7543,-0.6565),107:complex(-0.837,-0.5473),108:complex(-0.3618,-0.266),
109:complex(-0.4794,-0.2788),110:complex(-0.5499,-0.4649),111:complex(-0.6093,-0.3487),112:complex(-0.054,-0.2562),113:complex(-0.3226,-0.9465),114:complex(-0.0698,-0.9976),115:complex(-0.2043,-0.9789),116:complex(-0.0675,-0.444),117:complex(-0.1415,-0.5362),
118:complex(-0.0596,-0.7176),119:complex(-0.1842,-0.6774),120:complex(-0.143,-0.2193),121:complex(-0.4401,-0.898),122:complex(-0.6561,-0.7547),123:complex(-0.5478,-0.8366),124:complex(-0.266,-0.3618),125:complex(-0.2794,-0.4791),126:complex(-0.4653,-0.5496),
127:complex(-0.3487,-0.6093),
}

mapper = tuple(x for x in range(0,128))
maps = [mapper]
print(fitness(mapper, mapper, map))
#print(fitness(mapper, mapper2, map))
Maps = []
for i in range(12):
    ind = random.randint(0, len(maps)-1)
    Maps.append(maps[ind])
Maps = tuple(Maps)
A = []
#print(Maps)
for j in range(10000):
    C = crossoverPopulation(Maps, map)
    M = mutatePopulation(C, 0.25)
    A = AddToPopulation(Maps, M, A)
    #A = AddToPopulation(M, A)
    Maps = nextGeneration(mapper, A, 12, map)
    print(rank_fitness(mapper, Maps, map))
    A = []
print(Maps[0])