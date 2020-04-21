from finalPSK import *

map = {
0:complex(1,0),1:complex(0.9988,0.0491),2:complex(0.9892,0.1467),3:complex(0.9952,0.0980),4:complex(0.9415,0.3369),5:complex(0.9569,0.2903),6:complex(0.9808,0.1951),7:complex(0.9700,0.2430),8:complex(0.7410,0.6716),9:complex(0.7730,0.6344),10:complex(0.8315,0.5556),11:complex(0.8032,0.5957),12:complex(0.9239,0.3827),13:complex(0.9040,0.4276),14:complex(0.8577,0.5141),15:complex(0.8819,0.4714),
16:complex(0.0491,0.9988),17:complex(0.0980,0.9952),18:complex(0.1951,0.9808),19:complex(0.1467,0.9892),20:complex(0.3827,0.9239),21:complex(0.3369,0.9415),22:complex(0.2430,0.97),23:complex(0.2903,0.9569),24:complex(0.7071,0.7071),25:complex(0.6716,0.741),26:complex(0.5957,0.8032),27:complex(0.6344,0.773),28:complex(0.4276,0.9040),29:complex(0.4714,0.8819),30:complex(0.5556,0.8315),31:complex(0.5141,0.8577),
32:complex(-0.9988,0.0491),33:complex(-0.9952,0.098),34:complex(-0.9808,0.1951),35:complex(-0.9892,0.1467),36:complex(-0.9239,0.3827),37:complex(-0.9415,0.3369),38:complex(-0.97,0.243),39:complex(-0.9569,0.2903),40:complex(-0.7071,0.7071),41:complex(-0.741,0.6716),42:complex(-0.8032,0.5957),43:complex(-0.773,0.6344),44:complex(-0.904,0.4276),45:complex(-0.8819,0.4714),46:complex(-0.8315,0.5556),47:complex(-0.8577,0.5141),
48:complex(0,1),49:complex(-0.0491,0.9988),50:complex(-0.1467,0.9892),51:complex(-0.098,0.9952),52:complex(-0.3369,0.9415),53:complex(-0.2903,0.9569),54:complex(-0.1951,0.9808),55:complex(-0.243,0.97),56:complex(-0.6716,0.741),57:complex(-0.6344,0.773),58:complex(-0.5556,0.8315),59:complex(-0.5957,0.8032),60:complex(-0.3827,0.9239),61:complex(-0.4276,0.904),62:complex(-0.5141,0.8577),63:complex(-0.4714,0.8819),
64:complex(0.9988,-0.0491),65:complex(0.9952,-0.098),66:complex(0.9808,-0.1951),67:complex(0.9892,-0.1467),68:complex(0.9239,-0.3827),69:complex(0.9415,-0.3369),70:complex(0.97,-0.243),71:complex(0.9569,-0.2903),72:complex(0.7071,-0.7071),73:complex(0.741,-0.6716),74:complex(0.8032,-0.5957),75:complex(0.773,-0.6344),76:complex(0.904,-0.4276),77:complex(0.8819,-0.4714),78:complex(0.8315,-0.5556),79:complex(0.8577,-0.5141),
80:complex(0,-1),81:complex(0.0491,-0.9988),82:complex(0.1467,-0.9892),83:complex(0.098,-0.9952),84:complex(0.3369,-0.9415),85:complex(0.2903,-0.9569),86:complex(0.1951,-0.9808),87:complex(0.2430,-0.97),88:complex(0.6719,-0.7441),89:complex(0.6344,-0.773),90:complex(0.5556,-0.8315),91:complex(0.5957,-0.8032),92:complex(0.3827,-0.9239),93:complex(0.4276,-0.904),94:complex(0.5141,-0.8577),95:complex(0.4714,-0.8819),
96:complex(-1,0),97:complex(-0.9988,-0.0491),98:complex(-0.9892,-0.1467),99:complex(-0.9952,-0.098),100:complex(-0.9415,-0.3369),101:complex(-0.9569,-0.2903),102:complex(-0.9808,-0.1951),103:complex(-0.97,-0.243),104:complex(-0.741,-0.6716),105:complex(-0.773,-0.6344),106:complex(-0.8315,-0.5556),107:complex(-0.8032,-0.5957),108:complex(-0.9239,-0.3827),109:complex(-0.904,-0.4276),110:complex(-0.8577,-0.5141),111:complex(-0.8819,-0.4714),
112:complex(-0.0491,-0.9988),113:complex(-0.098,-0.9952),114:complex(-0.1951,-0.9808),115:complex(-0.1467,-0.9892),116:complex(-0.3827,-0.9239),117:complex(-0.3369,-0.9415),118:complex(-0.243,-0.97),119:complex(-0.2903,-0.9569),120:complex(-0.7071,-0.7071),121:complex(-0.6716,-0.741),122:complex(-0.5957,-0.8032),123:complex(-0.6344,-0.773),124:complex(-0.4276,-0.904),125:complex(-0.4714,-0.8819),126:complex(-0.5556,-0.8315),127:complex(-0.5141,-0.8577)
}

mapper1 = tuple(x for x in range(0,128))
maps = [mapper1]
print(fitness(mapper1, mapper1, map))
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
    M = mutatePopulation(C, 0.20)
    A = AddToPopulation(Maps, M, A)
    #A = AddToPopulation(M, A)
    Maps = nextGeneration(mapper1, A, 12, map)
    print(rank_fitness(mapper1, Maps, map))
    A = []
print(Maps[0])