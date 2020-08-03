import random

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
mapper5 = 0,10,7,13,9,3,14,4,12,5,11,2,6,15,1,8#huang
mapper6 = 6,10,0,5,3,15,12,9,13,1,11,14,8,4,7,2#krasicki 1
mapper7 = 4,7,2,8,14,13,1,11,9,10,15,5,3,0,12,6#krasicki 2



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

def selection(gray, candidates):
        fit = []
        score = 0
        ind = 0
        for i in range(len(candidates)):
            fit.append(fitness(gray, candidates[i], map))
        S = sum(fit)
        rand1 = random.randint(0, int(S))
        for j in range(len(candidates)):
            score = score + fitness(gray, candidates[j], map)
            if score > rand1:
                ind = j
                break
        return ind


def tournament(candidates):
    result = 0
    ind1, ind2, ind3 = random.randint(0, len(candidates)-1), random.randint(0, len(candidates)-1), random.randint(0, len(candidates)-1)
    x = fitness(mapper1, candidates[ind1], map)
    y = fitness(mapper1, candidates[ind2], map)
    z = fitness(mapper1, candidates[ind3], map)
    if x>y and x>z: result = ind1
    elif y>x and y>z: result = ind2
    elif z>x and z>y: result = ind3

    return result


maps = [mapper2, mapper3, mapper4, mapper5, mapper6, mapper7]

print(tournament(maps))
