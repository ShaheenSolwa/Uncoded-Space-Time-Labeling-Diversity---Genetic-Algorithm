import random, operator

M = 32
k = int((M-4)/2)
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

def biterrors(a,b):
    count = 0
    for i in range(0,32):
        if (((a >> i) & 1) != (b >> i) & 1):
            count = count + 1
    return count

def fitness(list1, list2, map):
    list3 = []
    list1, list2 = mappoints(map, list1), mappoints(map, list2)
    for i in range(len(list1)):
        for j in range(len(list2)):
            if i != j:
                fit = abs(list1[i]-list1[j]) * abs(list2[i]-list2[j])
                list3.append(fit)
    return round(min(list3),4)

def fitness2(list1, list2, map):
    list3 = []
    list1, list2 = mappoints(map, list1), mappoints(map, list2)
    for i in range(len(list1)):
        for j in range(len(list2)):
            if i != j:
                errors = biterrors(i,j)
                fit = (1/errors) * (abs(list1[i] - list1[j]) * abs(list2[i] - list2[j]))
                list3.append(fit)
    return round(min(list3), 6)

def fitness3(list1, list2, map):
    list3 = []
    sum = 0
    list1, list2 = mappoints(map, list1), mappoints(map, list2)
    for i in range(len(list1)):
        for j in range(len(list2)):
                fit = (abs(list1[i] - list1[j]) * abs(list2[i] - list2[j]))
                sum = sum + fit
        list3.append(sum)
        sum = 0
    return round(min(list3), 4)

def fitness4(list1, list2, map):
    list3 = []
    sum = 0
    list1, list2 = mappoints(map, list1), mappoints(map, list2)
    for i in range(len(list1)):
        for j in range(len(list2)):
            if i != j:
                errors = biterrors(i, j)
                fit = (1/errors)*(abs(list1[i] - list1[j]) * abs(list2[i] - list2[j]))
                sum = sum + fit
        list3.append(sum)
        sum = 0
    return round(min(list3), 4)

def rank_fitness(gray, population, map):
    rFit = {}
    for i in range(len(population)):
        rFit[i] = fitness4(gray, population[i], map)
    return sorted(rFit.items(), key=operator.itemgetter(1), reverse=True)


def neighbours(parent, point, map):
    neighbours = []
    points = mappoints(map, parent)
    x = points[point]
    for i in range(len(points)):
        y = points[i]
        dist = abs(x - y)
        if dist <= R-0.5:
            neighbours.append(i)
    return neighbours

def crossover(parent1, parent2, map):
    p1 = list(parent1)
    p2 = list(parent2)
    for i in range(k):
        ind = random.randint(0, len(parent1)-1)
        n1 = neighbours(p1, ind, map)
        n2 = neighbours(p2, ind, map)

        ind2 = random.randint(0, len(parent2)-1)
        while ind2 in n1 or ind2 in n2:
            ind2 = random.randint(0, len(parent2)-1)

        p1[ind], p1[ind2] = p1[ind2], p1[ind]
        p2[ind], p2[ind2] = p2[ind2], p2[ind]
    return p1, p2

def crossoverPopulation(population, map):
    crossed = []
    for i in range(len(population)):
        for j in range(len(population)):
            crossed.append(crossover(list(population[i]), list(population[j]), map))
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


def nextGeneration(gray, population, popSize, map):
    newPop = []
    rank1 = rank_fitness(gray, population, map)
    for i in range(popSize):
            newPop.append(population[rank1[i][0]])
    return newPop



map = {
0:complex(0.0707,0.0707), 1:complex(-0.0707,0.0707), 2:complex(0.0707,-0.0707),3:complex(-0.0707,-0.0707),
4:complex(0.3696,0.1531), 5:complex(-0.3696,0.1531), 6:complex(0.3696,-0.1531), 7:complex(-0.3696,-0.1531),
8:complex(0.3536,0.3536), 9:complex(-0.3536,0.3536), 10:complex(0.3536,-0.3536), 11:complex(-0.3536,-0.3536),
12:complex(0.1531,0.3696), 13:complex(-0.1531,0.3696), 14:complex(0.1531,-0.3696), 15:complex(-0.1531,-0.3696),
16:complex(0.1951,0.9808), 17:complex(-0.1951,0.9808), 18:complex(0.1951,-0.9808), 19:complex(-0.1951,-0.9808),
20:complex(0.5556,0.8315), 21:complex(-0.5556,0.8315), 22:complex(0.5556,-0.8315), 23:complex(-0.5556,-0.8315),
24:complex(0.9808,0.1951), 25:complex(-0.9808,0.1951), 26:complex(0.9808,-0.1951), 27:complex(-0.9808,-0.1951),
28:complex(0.8315,0.5556), 29:complex(-0.8315,0.5556), 30:complex(0.8315,-0.5556), 31:complex(-0.8315,-0.5556)
}

mapper1 = 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31

mapper2 = 29,17,19,3,23,6,16,24,1,18,15,7,26,31,13,0,11,10,14,2,5,25,21,28,30,4,9,20,12,8,22,27

maps = [mapper1,mapper2]
Maps = []
for i in range(8):
    ind = random.randint(0, len(maps)-1)
    Maps.append(maps[ind])
Maps = tuple(Maps)
A = []
#print(Maps)
for j in range(10000):
    C = crossoverPopulation(Maps, map)
    M = mutatePopulation(C, 0.10)
    A = AddToPopulation(Maps, M, A)
    Maps = nextGeneration(mapper1, A, 8, map)
    print(rank_fitness(mapper1, Maps, map))
    A = []
    print(j)