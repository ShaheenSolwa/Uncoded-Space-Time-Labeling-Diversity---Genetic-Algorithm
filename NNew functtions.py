import random

def tournament(mapper1, candidates):
    result = 0
    ind1, ind2, ind3 = random.randint(0, len(candidates)-1), random.randint(0, len(candidates)-1), random.randint(0, len(candidates)-1)
    x = fitness(mapper1, candidates[ind1], map)
    y = fitness(mapper1, candidates[ind2], map)
    z = fitness(mapper1, candidates[ind3], map)
    if x>y and x>z: result = ind1
    elif y>x and y>z: result = ind2
    elif z>x and z>y: result = ind3

    return result

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

def ranker(mapper1, candidates, map):
    Fitness = []
    ind = []
    for i in range(len(candidates)):
        f = fitness(mapper1, candidates[i], map)
        Fitness.append([i,f])
    Fitness.sort(reverse=True)
    return [Fitness[0], Fitness[1]]


map = {
    0:complex(-3,-3), 1:complex(-3,-1), 2:complex(-3,3), 3:complex(-3,1),
    4:complex(-1,-3), 5:complex(-1,-1), 6:complex(-1,3), 7:complex(-1,1),
    8:complex(3,-3), 9:complex(3,-1), 10:complex(3,3), 11:complex(3,1),
    12:complex(1,-3), 13:complex(1,-1), 14:complex(1,3), 15:complex(1,1),
}
mapper1 = 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15#gray
mapper2 = 13,11,15,9,6,0,4,2,12,10,14,8,7,1,5,3#samra
mapper3 = 15,1,2,12,4,10,9,7,8,6,5,11,3,13,14,0#xu
mapper4 = 7,4,5,6,11,8,9,10,15,12,13,14,3,0,1,2#seddik
""""""

maps = [mapper2, mapper3, mapper4]

print(ranker(mapper1, maps, map))






"""
def crossover(mapper1, candidates, map):
    ind1 = tournament(mapper1, candidates)
    ind2 = tournament(mapper1, candidates)
    p1 = list(candidates[ind1])
    p2 = list(candidates[ind2])
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

def crossoverPopulation(mapper1, population, map):
    crossed = []
    for i in range(len(population)):
        for j in range(len(population)):
            crossed.append(crossover(mapper1, population, map))

"""
