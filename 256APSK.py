from finalAPSK import *

map = {
0:complex(0.1524,0.015),1:complex(0.1465,0.0445),2:complex(0.1184,0.0972),3:complex(0.1351,0.0722),4:complex(0.015,0.1524),5:complex(0.0445,0.1465),6:complex(0.0972,0.1184),7:complex(0.0722,0.1351),8:complex(-0.1524,0.015),9:complex(-0.1465,0.0445),10:complex(-0.1184,0.0972),
    11:complex(-0.1351,0.0722),12:complex(-0.015,0.1524),13:complex(-0.0445,0.1465),14:complex(-0.0972,0.1184),15:complex(-0.0722,0.1351),16:complex(0.1524,-0.015),17:complex(0.1465,-0.0445),18:complex(0.1184,-0.0972),19:complex(0.1351,-0.0722),
    20:complex(0.015,-0.1524),21:complex(0.0445,-0.1465),22:complex(0.0972,-0.1184),23:complex(0.0722,-0.1351),24:complex(-0.1524,-0.015),25:complex(-0.1465,-0.0445),26:complex(-0.1184,-0.0972),27:complex(-0.1351,-0.0722),28:complex(-0.015,-0.1524),
    29:complex(-0.0445,-0.1465),30:complex(-0.0972,-0.1184),31:complex(-0.0722,-0.1351),32:complex(0.273,0.0269),33:complex(0.2625,0.0796),34:complex(0.212,0.174),35:complex(0.2419,0.1293),36:complex(0.0269,0.273),37:complex(0.0796,0.2625),
    38:complex(0.174,0.212),39:complex(0.1293,0.2419),40:complex(-0.273,0.0269),41:complex(-0.2625,0.0796),42:complex(-0.212,0.174),43:complex(-0.2419,0.1293),44:complex(-0.0269,0.273),45:complex(-0.0796,0.2625),46:complex(-0.174,0.212),
    47:complex(-0.1293,0.2419),48:complex(0.273,-0.0269),49:complex(0.2625,-0.0796),50:complex(0.212,-0.174),51:complex(0.2419,-0.1293),52:complex(0.0269,-0.273),53:complex(0.0796,-0.2625),54:complex(0.174,-0.212),55:complex(0.1293,-0.2419),
    56:complex(-0.273,-0.0269),57:complex(-0.2625,-0.0796),58:complex(-0.212,-0.174),59:complex(-0.2419,-0.1293),60:complex(-0.0269,-0.273),61:complex(-0.0796,-0.2625),62:complex(-0.174,-0.212),63:complex(-0.1293,-0.2419),64:complex(0.4542,0.0447),
    65:complex(0.4367,0.1325),66:complex(0.3528,0.2895),67:complex(0.4025,0.2151),68:complex(0.0447,0.4542),69:complex(0.1325,0.4367),70:complex(0.2895,0.3528),71:complex(0.2151,0.4025),72:complex(-0.4025,0.0447),73:complex(-0.4367,0.1325),
    74:complex(-0.3528,0.2895),75:complex(-0.4025,0.2151),76:complex(-0.0447,0.4542),77:complex(-0.1325,0.4367),78:complex(-0.2895,0.3528),79:complex(-0.2151,0.4025),80:complex(0.4542,-0.0447),81:complex(0.4367,-0.1325),82:complex(0.3528,-0.2895),
    83:complex(0.4025,-0.2151),84:complex(0.0447,-0.4542),85:complex(0.1325,-0.4367),86:complex(0.2895,-0.3528),87:complex(0.2151,-0.4025),88:complex(-0.4542,-0.0447),89:complex(-0.4367,-0.1325),90:complex(-0.3528,-0.2895),91:complex(-0.4025,-0.2151),
    92:complex(-0.0447,-0.4542),93:complex(-0.1325,-0.4367),94:complex(-0.2895,-0.3528),95:complex(-0.2151,-0.4025),96:complex(0.3665,0.0361),97:complex(0.3524,0.1069),98:complex(0.2847,0.2336),99:complex(0.3248,0.1736),100:complex(0.0361,0.3665),
    101:complex(0.1069,0.3524),102:complex(0.2336,0.2847),103:complex(0.1736,0.3248),104:complex(-0.3665,0.0361),105:complex(-0.3524,0.1069),106:complex(-0.2847,0.2336),107:complex(-0.3248,0.1736),108:complex(-0.0361,0.3665),
    109:complex(-0.1069,0.3524),110:complex(-0.2336,0.2847),111:complex(-0.1736,0.3248),112:complex(0.3665,-0.0361),113:complex(0.3524,-0.1069),114:complex(0.2847,-0.2336),115:complex(0.3248,-0.1736),116:complex(0.0361,-0.3665),
    117:complex(0.1069,-0.3524),118:complex(0.2336,-0.2847),119:complex(0.1736,-0.3248),120:complex(-0.3665,-0.0361),121:complex(-0.3524,-0.1069),122:complex(-0.2847,-0.2336),123:complex(-0.3248,-0.1736),124:complex(-0.0361,-0.3665),
    125:complex(-0.1069,-0.3524),126:complex(-0.2336,-0.2847),127:complex(-0.1736,-0.3248),

    128:complex(0.9952,0.098),129:complex(0.9569,0.2903),130:complex(0.773,0.6344),131:complex(0.8819,0.4714),132:complex(0.098,0.9952),133:complex(0.2903,0.9569),134:complex(0.6344,0.773),135:complex(0.4714,0.8819),
    136:complex(-0.9952,0.098),137:complex(-0.9569,0.2903),138:complex(-0.773,0.6344),139:complex(-0.8819,0.4714),140:complex(-0.098,0.9952),141:complex(-0.2903,0.9569),142:complex(-0.6344,0.773),143:complex(-0.4714,0.8819),
    144:complex(0.9952,-0.098),145:complex(0.9569,-0.2903),146:complex(0.773,-0.6344),147:complex(0.8819,-0.4714),148:complex(0.098,-0.9952),149:complex(0.2903,-0.9569),150:complex(0.6344,-0.773),151:complex(0.4714,-0.8819),
    152:complex(-0.9952,-0.098),153:complex(-0.9569,-0.2903),154:complex(-0.773,-0.6344),155:complex(-0.8819,-0.4714),156:complex(-0.098,-0.9952),157:complex(-0.2903,-0.9569),158:complex(-0.6344,-0.773),159:complex(-0.4714,-0.8819),
    160:complex(0.7739,0.0762),161:complex(0.7442,0.2257),162:complex(0.6011,0.4933),163:complex(0.6858,0.3666),164:complex(0.0762,0.7739),165:complex(0.2257,0.7442),166:complex(0.4933,0.6011),167:complex(0.3666,0.6858),
    168:complex(-0.7739,0.0762),169:complex(-0.7442,0.2257),170:complex(-0.6011,0.4933),171:complex(-0.6858,0.3666),172:complex(-0.0762,0.7739),173:complex(-0.2257,0.7442),174:complex(-0.4933,0.6011),175:complex(-0.3666,0.6858),
    176:complex(0.7739,-0.0762),177:complex(0.7442,-0.2257),178:complex(0.6011,-0.4933),179:complex(0.6858,-0.3666),180:complex(0.0762,-0.7739),181:complex(0.2257,-0.7442),182:complex(0.4933,-0.6011),183:complex(0.3666,-0.6858),
    184:complex(-0.7739,-0.0762),185:complex(-0.7442,-0.2257),186:complex(-0.6011,-0.4933),187:complex(-0.6858,-0.3666),188:complex(-0.0762,-0.7739),189:complex(-0.2257,-0.7442),190:complex(-0.4933,-0.6011),191:complex(-0.3666,-0.6858),
    192:complex(0.5439,0.0536),193:complex(0.523,0.1587),194:complex(0.4225,0.3467),195:complex(0.482,0.2576),196:complex(0.0536,0.5439),197:complex(0.1587,0.5230),198:complex(0.3467,0.4225),199:complex(0.2576,0.482),
    200:complex(-0.5439,0.0536),201:complex(-0.523,0.1587),202:complex(-0.4225,0.3467),203:complex(-0.482,0.2576),204:complex(-0.0536,0.5439),205:complex(-0.1587,0.523),206:complex(-0.3467,0.4225),207:complex(-0.2576,0.482),
    208:complex(0.5439,-0.0536),209:complex(0.523,-0.1587),210:complex(0.4225,-0.3467),211:complex(0.482,-0.2576),212:complex(0.0536,-0.5439),213:complex(0.1587,-0.523),214:complex(0.3467,-0.4225),215:complex(0.2576,-0.482),
    216:complex(-0.5439,-0.0536),217:complex(-0.523,-0.1587),218:complex(-0.4225,-0.3467),219:complex(-0.482,-0.2576),220:complex(-0.0536,-0.5439),221:complex(-0.1587,-0.523),222:complex(-0.3467,-0.4225),223:complex(-0.2576,-0.482),
    224:complex(0.6454,0.0636),225:complex(0.6206,0.1883),226:complex(0.5013,0.4114),227:complex(0.572,0.3057),228:complex(0.0636,0.6454),229:complex(0.1883,0.6206),230:complex(0.4114,0.5013),231:complex(0.3057,0.572),
    232:complex(-0.6454,0.0636),233:complex(-0.6206,0.1883),234:complex(-0.5013,0.4114),235:complex(-0.572,0.3057),236:complex(-0.0636,0.6454),237:complex(-0.1883,0.6206),238:complex(-0.4114,0.5013),239:complex(-0.3057,0.5720),
    240:complex(0.6454,-0.0636),241:complex(0.6206,-0.1883),242:complex(0.5013,-0.4114),243:complex(0.572,-0.3057),244:complex(0.0636,-0.6454),245:complex(0.1883,-0.6206),246:complex(0.4114,-0.5013),247:complex(0.3057,-0.572),
    248:complex(-0.6454,-0.0636),249:complex(-0.6206,-0.1883),250:complex(-0.5013,-0.4114),251:complex(-0.572,-0.3057),252:complex(-0.0636,-0.6454),253:complex(-0.1883,-0.6206),254:complex(-0.4114,-0.5013),255:complex(-0.3057,-0.572)
}



mapper = tuple(x for x in range(0,256))
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
for j in range(10000):
    C = crossoverPopulation(Maps, map)
    M = mutatePopulation(C, 0.50)
    A = AddToPopulation(Maps, M, A)
    #A = AddToPopulation(M, A)
    Maps = nextGeneration(mapper, A, 10, map)
    print(rank_fitness(mapper, Maps, map))
    A = []
print(Maps[0])