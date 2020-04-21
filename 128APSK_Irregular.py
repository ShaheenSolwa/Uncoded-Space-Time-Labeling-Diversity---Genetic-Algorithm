from finalAPSK import *

map = {
0:complex(0.3567,0),1:complex(0.3,0.1928),2:complex(0.1482,0.3245),3:complex(-0.0508,0.3531),4:complex(-0.2336,0.2696),5:complex(-0.3423,0.1005),6:complex(-0.3426,-0.1005),7:complex(-0.2336,-0.2696),8:complex(-0.0508,-0.3531),9:complex(0.1482,-0.3245),10:complex(0.3,-0.1928),
11:complex(0.5787,0),12:complex(0.5438,0.1979),13:complex(0.4433,0.3720),14:complex(0.2893,0.5012),15:complex(0.1005,0.5699),16:complex(-0.1005,0.5699),17:complex(-0.2894,0.5012),18:complex(-0.4433,0.372),19:complex(-0.5438,0.1979),20:complex(-0.5787,0),
21:complex(-0.5438,-0.1979),22:complex(-0.4433,-0.372),23:complex(-0.2893,-0.5012),24:complex(-0.1005,-0.5699),25:complex(0.1005,-0.5699),26:complex(0.2894,-0.5012),27:complex(0.4433,-0.372),28:complex(0.5438,-0.1979),29:complex(0.8337,0),30:complex(0.8095,0.1995),
31:complex(0.7363,0.3911),32:complex(0.624,0.5529),33:complex(0.4736,0.6861),34:complex(0.2956,0.7795),35:complex(0.1005,0.8276),36:complex(-0.1005,0.8276),37:complex(-0.2956,0.7795),38:complex(-0.4736,0.6861),39:complex(-0.624,0.5529),40:complex(-0.7382,0.3874),
41:complex(-0.8095,0.1995),42:complex(-0.8337,0),43:complex(-0.8095,-0.1996),44:complex(-0.7382,-0.3874),45:complex(-0.624,-0.5529),46:complex(-0.4736,-0.6861),47:complex(-0.2956,-0.7796),48:complex(-0.1005,-0.8276),49:complex(0.1005,-0.8276),50:complex(0.2956,-0.7795),
51:complex(0.4736,-0.6861),52:complex(0.624,-0.5528),53:complex(0.7382,-0.3874),54:complex(0.8095,-0.1995),55:complex(0.10572,0),56:complex(1.038,0.20001),57:complex(0.9815,0.3929),58:complex(0.8894,0.5717),59:complex(0.7651,0.7296),
60:complex(0.6132,0.8612),61:complex(0.4392,0.9617),62:complex(0.2492,1.0274),63:complex(0.0503,1.056),64:complex(-0.1505,1.0464),65:complex(-0.3458,0.9991),66:complex(-0.5286,0.9156),67:complex(-0.6923,0.799),68:complex(-0.831,0.6535),69:complex(-0.9397,0.4844),
70:complex(-1.014,0.2978),71:complex(-1.0524,0.1005),72:complex(-1.0524,-0.1005),73:complex(-1.0144,-0.2979),74:complex(-0.9397,-0.4844),75:complex(-0.831,-0.6535),76:complex(-0.6923,-0.799),77:complex(-0.5293,-0.9151),78:complex(-0.3458,-0.9991),79:complex(-0.1504,-1.046),
80:complex(0.0503,-1.056),81:complex(0.2493,-1.0274),82:complex(0.4392,-0.9617),83:complex(0.6132,-0.8612),84:complex(0.7651,-0.7295),85:complex(0.8894,-0.5716),86:complex(0.9815,-0.3929),87:complex(1.0381,-0.20001),88:complex(1.2808,0),89:complex(1.265,0.20004),
90:complex(1.2181,0.3958),91:complex(1.1412,0.5814),92:complex(1.0362,0.7528),93:complex(0.9057,0.9057),94:complex(0.7528,1.0362),95:complex(0.5814,1.1412),96:complex(0.3958,1.2181),97:complex(0.2004,1.265),98:complex(0,1.2808),99:complex(-0.2004,1.265),
100:complex(-0.3958,1.2181),101:complex(-0.5814,1.1412),102:complex(-0.7528,1.0362),103:complex(-0.9057,0.9057),104:complex(-1.0362,0.7528),105:complex(-1.1412,0.5814),106:complex(-1.2181,0.3958),107:complex(-1.265,0.2004),108:complex(-1.2808,0),
109:complex(-1.265,-0.2004),110:complex(-1.2181,-0.3958),111:complex(-1.1412,-0.5814),112:complex(-1.0362,-0.7528),113:complex(-0.9057,-0.9057),114:complex(-0.7528,-1.0362),115:complex(-0.5814,-1.1412),116:complex(-0.3958,-1.2181),117:complex(-0.2004,-1.265),
118:complex(0,-1.2808),119:complex(0.2004,-1.265),120:complex(0.3957,-1.2181),121:complex(0.5814,-1.1412),122:complex(0.7528,-1.0362),123:complex(0.9057,-0.9057),124:complex(1.0362,-0.7528),125:complex(1.1412,-0.5815),126:complex(1.2181,-0.3958),
127:complex(1.265,-0.2004),
}

mapper = tuple(x for x in range(0,128))

#mapper2 = 46,63,14,10,9,25,3,35,43,38,54,60,2,51,11,24,31,34,16,18,21,40,61,37,53,30,6,41,4,8,49,62,22,17,39,56,48,44,1,32,47,12,29,58,27,5,19,13,36,20,42,28,55,33,7,50,0,45,52,59,57,26,15,23


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
for j in range(100000):
    C = crossoverPopulation(Maps, map)
    M = mutatePopulation(C, 0.30)
    A = AddToPopulation(Maps, M, A)
    #A = AddToPopulation(M, A)
    Maps = nextGeneration(mapper, A, 12, map)
    print(rank_fitness(mapper, Maps, map))
    A = []
print(Maps[0])