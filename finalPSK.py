import random, operator

M = 512
k = int(M/6)
R = 1
#AddedPop = []

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
    return min(list3)

def rank_fitness(gray, population, map):
    rFit = {}
    for i in range(len(population)):
        rFit[i] = fitness(gray, population[i], map)
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
    rank = rank_fitness(gray, population, map)
    for i in range(popSize):
        newPop.append(population[rank[i][0]])
    return newPop
