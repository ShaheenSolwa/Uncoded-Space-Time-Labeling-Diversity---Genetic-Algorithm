from finalQAM import *

map = {
    0:complex(-15,15),1:complex(-15,13),2:complex(-15,9),3:complex(-15,11),4:complex(-15,1),5:complex(-15,3),6:complex(-15,7),7:complex(-15,5),8:complex(-15,-15),9:complex(-15,-13),10:complex(-15,-9),11:complex(-15,-11),12:complex(-15,-1),13:complex(-15,-3),14:complex(-15,-7),15:complex(-15,-5),
    16:complex(-13,15),17:complex(-13,13),18:complex(-13,9),19:complex(-13,11),20:complex(-13,1),21:complex(-13,3),22:complex(-13,7),23:complex(-13,5),24:complex(-13,-15),25:complex(-13,-13),26:complex(-13,-9),27:complex(-13,-11),28:complex(-13,-1),29:complex(-13,-3),30:complex(-13,-7),31:complex(-13,-5),
    32:complex(-9,15),33:complex(-9,13),34:complex(-9,9),35:complex(-9,11),36:complex(-9,1),37:complex(-9,3),38:complex(-9,7),39:complex(-9,5),40:complex(-9,-15),41:complex(-9,-13),42:complex(-9,-9),43:complex(-9,-11),44:complex(-9,-1),45:complex(-9,-3),46:complex(-9,-7),47:complex(-9,-5),
    48:complex(-11,15),49:complex(-11,13),50:complex(-11,9),51:complex(-11,11),52:complex(-11,1),53:complex(-11,3),54:complex(-11,7),55:complex(-11,5),56:complex(-11,-15),57:complex(-11,-13),58:complex(-11,-9),59:complex(-11,-11),60:complex(-11,-1),61:complex(-11,-3),62:complex(-11,-7),63:complex(-11,-5),
    64:complex(-1,15),65:complex(-1,13),66:complex(-1,9),67:complex(-1,11),68:complex(-1,1),69:complex(-1,3),70:complex(-1,7),71:complex(-1,5),72:complex(-1,-15),73:complex(-1,-13),74:complex(-1,-9),75:complex(-1,-11),76:complex(-1,-1),77:complex(-1,-3),78:complex(-1,-7),79:complex(-1,-5),
    80:complex(-3,15),81:complex(-3,13),82:complex(-3,9),83:complex(-3,11),84:complex(-3,1),85:complex(-3,3),86:complex(-3,7),87:complex(-3,5),88:complex(-3,-15),89:complex(-3,-13),90:complex(-3,-9),91:complex(-3,-11),92:complex(-3,-1),93:complex(-3,-3),94:complex(-3,-7),95:complex(-3,-5),
    96:complex(-7,15),97:complex(-7,13),98:complex(-7,9),99:complex(-7,11),100:complex(-7,1),101:complex(-7,3),102:complex(-7,7),103:complex(-7,5),104:complex(-7,-15),105:complex(-7,-13),106:complex(-7,-9),107:complex(-7,-11),108:complex(-7,-1),109:complex(-7,-3),110:complex(-7,-7),111:complex(-7,-5),
    112:complex(-5,15),113:complex(-5,13),114:complex(-5,9),115:complex(-5,11),116:complex(-5,1),117:complex(-5,3),118:complex(-5,7),119:complex(-5,5),120:complex(-5,-15),121:complex(-5,-13),122:complex(-5,-9),123:complex(-5,-11),124:complex(-5,-1),125:complex(-5,-3),126:complex(-5,-7),127:complex(-5,-5),
    128: complex(15, 15), 129: complex(15, 13), 130: complex(15, 9), 131: complex(15, 11), 132: complex(15, 1),133: complex(15, 3),134: complex(15, 7),135: complex(15, 5), 136: complex(15, -15),137: complex(15, -13),138: complex(15, -9),139: complex(15, -11),140: complex(15, -1),141: complex(15, -3), 142: complex(15, -7),143: complex(15, -5),
    144: complex(13, 15), 145: complex(13, 13), 146: complex(13, 9), 147: complex(13, 11), 148: complex(13, 1),149: complex(13, 3),150: complex(13, 7),151: complex(13, 5), 152: complex(13, -15),153: complex(13, -13),154: complex(13, -9),155: complex(13, -11),156: complex(13, -1),157: complex(13, -3), 158: complex(13, -7),159: complex(13, -5),
    160: complex(9, 15), 161: complex(9, 13), 162: complex(9, 9), 163: complex(9, 11), 164: complex(9, 1),165: complex(9, 3),166: complex(9, 7),167: complex(9, 5), 168: complex(9, -15),169: complex(9, -13),170: complex(9, -9),171: complex(9, -11),172: complex(9, -1),173: complex(9, -3),174: complex(9, -7),175: complex(9, -5),
    176: complex(11, 15),177: complex(11, 13), 178: complex(11, 9), 179: complex(11, 11), 180: complex(11, 1),181: complex(11, 3),182: complex(11, 7),183: complex(11, 5),184: complex(11, -15),185: complex(11, -13),186: complex(11, -9),187: complex(11, -11),188: complex(11, -1),189: complex(11, -3), 190: complex(11, -7), 191: complex(11, -5),
    192: complex(1, 15), 193: complex(1, 13), 194: complex(1, 9), 195: complex(1, 11), 196: complex(1, 1),197: complex(1, 3),198: complex(1, 7),199: complex(1, 5),200: complex(1, -15),201: complex(1, -13),202: complex(1, -9),203: complex(1, -11),204: complex(1, -1),205: complex(1, -3),206: complex(1, -7),207: complex(1, -5),
    208: complex(3, 15), 209: complex(3, 13), 210: complex(3, 9), 211: complex(3, 11), 212: complex(3, 1),213: complex(3, 3),214: complex(3, 7),215: complex(3, 5),216: complex(3, -15),217: complex(3, -13),218: complex(3, -9),219: complex(3, -11),220: complex(3, -1),221: complex(3, -3),222: complex(3, -7),223: complex(3, -5),
    224: complex(7, 15), 225: complex(7, 13), 226: complex(7, 9), 227: complex(7, 11), 228: complex(7, 1),229: complex(7, 3),230: complex(7, 7),231: complex(7, 5),232: complex(7, -15),233: complex(7, -13),234: complex(7, -9),235: complex(7, -11),236: complex(7, -1),237: complex(7, -3),238: complex(7, -7),239: complex(7, -5),
    240: complex(5, 15), 241: complex(5, 13), 242: complex(5, 9), 243: complex(5, 11), 244: complex(5, 1),245: complex(5, 3),246: complex(5, 7),247: complex(5, 5),248: complex(5, -15),249: complex(5, -13),250: complex(5, -9),251: complex(5, -11),252: complex(5, -1),253: complex(5, -3),254: complex(5, -7),255: complex(5, -5)
}

mapper1 = tuple(x for x in range(0,256))
mapper2 = 0,205,3,206,200,5,6,203,196,9,10,199,12,193,194,15,220,17,18,223,20,217,218,23,24,213,214,27,208,29,30,211,236,33,34,239,36,233,234,39,40,229,230,43,224,45,46,227,\
    48,253,254,51,248,53,54,251,244,57,58,247,60,241,242,63,140,65,66,143,68,137,138,71,72,133,134,75,128,77,78,131,80,157,158,83,152,85,86,155,148,89,90,151,92,145,146,95,\
    96,173,174,99,168,101,102,171,164,105,106,167,108,161,162,111,188,113,114,191,116,185,186,119,120,181,182,123,176,125,126,179,76,129,130,79,132,73,74,135,136,69,70,139,\
    64,141,142,67,144,93,94,147,88,149,150,91,84,153,154,87,156,81,82,159,160,109,110,163,104,165,166,107,100,169,170,103,172,97,98,175,124,177,178,127,180,121,122,183,184,\
    117,118,187,112,189,190,115,192,13,14,195,8,197,198,11,4,201,202,7,204,1,2,207,28,209,210,31,212,25,26,215,216,21,22,219,16,221,222,19,44,225,226,47,228,41,42,231,\
    232,37,38,235,32,237,238,35,240,61,62,243,56,245,246,59,52,249,250,55,252,49,50,255
"""
import collections
print([item for item, count in collections.Counter(mapper1).items() if count > 1])
"""
rev_dict = {}

for key, value in map.items():
    rev_dict.setdefault(value, set()).add(key)

result = [key for key, values in rev_dict.items()
          if len(values) > 1]

# printing result
print("duplicate values", str(result))
maps = [mapper1, mapper2]
print(fitness(mapper1, mapper1, map))
print(fitness(mapper1, mapper2, map))
Maps = []
for i in range(10):
    ind = random.randint(0, len(maps)-1)
    Maps.append(maps[ind])
Maps = tuple(Maps)
A = []
#print(Maps)
for j in range(100000):
    C = crossoverPopulation(Maps, map)
    M = mutatePopulation(C, 0.30)
    A = AddToPopulation(Maps, M, A)
    #A = AddToPopulation(M)
    Maps = nextGeneration(mapper1, A, 10, map)
    print(rank_fitness(mapper1, Maps, map))
    A = []
print(Maps[0])