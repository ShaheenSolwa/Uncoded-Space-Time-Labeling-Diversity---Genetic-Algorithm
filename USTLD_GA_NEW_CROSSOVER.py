import random, operator, math

M = 128
R = 1

def initialPopulation(population, popSize):
    pop = []
    for i in range(popSize):
        pop.append(random.choice(population))
    return list(tuple(pop))


def mappoints(map, mapper):
    mapped = {}
    for i in range(len(mapper)):
        for j in map.keys():
            if j == mapper[i]:
                #print(mapper[i], map.get(i))
                mapped[j] = map.get(i)
    return mapped


def fitness(list1, list2, map):
    list3 = []
    list1, list2 = mappoints(map, list1), mappoints(map, list2)
    for i in range(len(list1)):
        for j in range(len(list2)):
            if i != j:
                fit = abs(list1[i]-list1[j]) * abs(list2[i]-list2[j])
                list3.append(fit)
    return round(min(list3),4)


def rank_fitness(gray, population, map):
    rFit = {}
    for i in range(len(population)):
        rFit[i] = fitness(gray, population[i], map)
    return sorted(rFit.items(), key=operator.itemgetter(1), reverse=True)


def crossover(parent1, parent2):
    p1 = list(parent1)
    p2 = list(parent2)

    newP1 = p1[:int(M/2)] + p2[int(M/2):]
    newP2 = p2[:int(M/2)] + p1[int(M/2):]

    return [newP1, newP2]

def crossoverPopulation(population):
    crossed = []
    #population = list(population)
    for i in range(len(population)):
        for j in range(len(population)):
            #if i != j:
                crossed.append(crossover(population[i],population[j]))
    return crossed


def mutation(child, rate):
    if random.random() < rate:
        i = random.randint(0, len(child)-1)
        j = random.randint(0, len(child)-1)

        child[i], child[j] = child[j], child[i]
    return child


def mutatePopulation(children, rate):
    mutated = []
    for i in range(len(children)):
        for j in range(len(children[i])):
            mutated.append(mutation(children[i][j], rate))
    return mutated


def AddToPopulation(parents, children, AddedPop):
    for i in range(len(parents)):
        AddedPop.append(parents[i])
    for i in range(len(children)):
        AddedPop.append(children[i])
    return AddedPop


def checkIfDuplicates_2(listOfElems):
    setOfElems = set()
    for elem in listOfElems:
        if elem in setOfElems:
            return True
        else:
            setOfElems.add(elem)
    return False


def filter(mapper1, population):
    pop = []
    fake = []
    for i in range(len(population)):
        if checkIfDuplicates_2(list(population[i])) == False:
            pop.append(population[i])
        else:
            fake.append(population[i])
    #print(fake)
    return pop


def nextGeneration(gray, population, popSize, map):
    newPop,Pop = [],[]
    pop = filter(mapper1,population)
    if len(pop) != 0:
        #rank1 = BER_values(gray, pop, map, n, Nr, SNR)
        #for i in range(popSize):
         #      newPop.append(population[rank1[i][0]])
        rank2 = rank_fitness(gray, pop, map)
        for i in range(popSize):
                Pop.append(pop[rank2[i][0]])
        return Pop
    else:
        return False

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
mapper2 = 96,1,99,2,102,7,101,4,108,13,111,14,106,11,105,8,120,25,\
    123,26,126,31,125,28,116,21,119,22,114,19,113,16,80,49,\
    83,50,86,55,85,52,92,61,95,62,90,59,89,56,72,41,\
    75,42,78,47,77,44,68,37,71,38,66,35,65,32,\
    0,97,3,98,6,103,5,100,12,109,15,110,10,107,9,104,\
    24,121,27,122,30,127,29,124,20,117,23,118,18,115,17,112,\
    48,81,51,82,54,87,53,84,60,93,63,94,58,91,57,88,\
    40,73,43,74,46,79,45,76,36,69,39,70,34,67,33,64
mapper3 = 59, 83, 99, 16, 29, 33, 95, 26, 114, 10, 70, 125, 120, 48, 23, 4, 27, 90, 115, 96, 28, 34, 8, 0, 77, 106, 62, 117, 60, 47, 86, 121, 61, 68, 6, 15, 73, 55, 65, 104, 36, 31, 94, 45, 5, 74, 9, 32, 39, 98, 107, 66, 127, 20, 46, 54, 110, 25, 72, 123, 2, 41, 79, 111, 102, 76, 40, 105, 13, 50, 35, 30, 53, 93, 112, 71, 81, 7, 49, 119, 42, 108, 113, 122, 85, 37, 38, 92, 43, 21, 124, 97, 126, 58, 18, 75, 89, 64, 103, 84, 63, 22, 78, 118, 44, 80, 109, 11, 19, 88, 52, 67, 101, 51, 1, 12, 17, 82, 87, 56, 24, 3, 91, 57, 14, 69, 116, 100
maps = [mapper2]
Maps = []
for i in range(8):
    ind = random.randint(0, len(maps)-1)
    Maps.append(maps[ind])
Maps = tuple(Maps)
A = []

for j in range(10000):
    C = crossoverPopulation(Maps)
    m = mutatePopulation(C, 0.1)
    A = AddToPopulation(Maps, m, A)
    Maps = nextGeneration(mapper1, A, 8, map)
    print(rank_fitness(mapper1, Maps, map))
    A = []
    print(j)
    if maps == False:
        break