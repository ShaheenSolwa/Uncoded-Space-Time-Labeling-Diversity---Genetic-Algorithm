from finalAPSK import *

map = {
    0:complex(0.3138,0),1:complex(0,0.3138),2:complex(-0.3138,0),3:complex(0,-0.3138),
    4:complex(0.7875,0),5:complex(0.6625,0.4258),6:complex(0.3271,0.7164),7:complex(-0.1122,0.7795),
    8:complex(-0.5175,0.5952),9:complex(-0.756,0.2219),10:complex(-0.756,-0.2219),11:complex(-0.5157,-0.5952),
    12:complex(-0.1121,-0.7795),13:complex(0.3271,-0.7163),14:complex(0.6625,-0.4257),15:complex(1.2074,0),
    16:complex(1.1259,0.4362),17:complex(0.8923,0.8134),18:complex(0.5382,1.0808),19:complex(0.1114,1.2022),
    20:complex(-0.3304,1.1613),21:complex(-0.7276,0.9635),22:complex(-1.0266,0.6356),23:complex(-1.1868,0.2219),
    24:complex(-1.1868,-0.2219),25:complex(-1.0265,-0.6356),26:complex(-0.7276,-0.9635),27:complex(-0.3304,-1.1613),
    28:complex(0.1114,-1.2022),29:complex(0.5382,-1.0808),30:complex(0.8923,-0.8134),31:complex(1.1259,-0.4361)
}

rev_dict = {}

for key, value in map.items():
        rev_dict.setdefault(value, set()).add(key)

result = [key for key, values in rev_dict.items()
              if len(values) > 1]

    # printing result
print("duplicate values", str(result))

mapper = 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31
#mapper2 = [12,10,13,9,15,11,8,14,6,5,7,3,1,4,0,2]

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
    M = mutatePopulation(C, 0.12)
    A = AddToPopulation(Maps, M, A)
    #A = AddToPopulation(M, A)
    Maps = nextGeneration(mapper, A, 12, map)
    print(rank_fitness(mapper, Maps, map))
    A = []
print(Maps[0])