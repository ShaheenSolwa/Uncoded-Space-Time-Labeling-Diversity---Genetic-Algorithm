from finalQAM import *

map = {
0:complex(-15,17),1:complex(-15,19),2:complex(-15,23),3:complex(-15,21),
4:complex(-1,17),5:complex(-1,19),6:complex(-1,23),7:complex(-1,21),
8:complex(-15,-17),9:complex(-15,-19),10:complex(-15,-23),11:complex(-15,-21),
12:complex(-1,-17),13:complex(-1,-19),14:complex(-1,-23),15:complex(-1,-21),
16:complex(-13,17),17:complex(-13,19),18:complex(-13,23),19:complex(-13,21),

20:complex(-3,17),21:complex(-3,19),22:complex(-3,23),23:complex(-3,21),
24:complex(-13,-17),25:complex(-13,-19),26:complex(-13,-23),27:complex(-13,-21),
28:complex(-3,-17),29:complex(-3,-19),30:complex(-3,-23),31:complex(-3,-21),
32:complex(-9,17),33:complex(-9,19),34:complex(-9,23),35:complex(-9,21),
36:complex(-7,17),37:complex(-7,19),38:complex(-7,23),39:complex(-7,21),

40:complex(-9,-17),41:complex(-9,-19),42:complex(-9,-23),43:complex(-9,-21),
44:complex(-7,-17),45:complex(-7,-19),46:complex(-7,-23),47:complex(-7,-21),
48:complex(-11,17),49:complex(-11,19),50:complex(-11,23),51:complex(-11,21),
52:complex(-5,17),53:complex(-5,19),54:complex(-5,23),55:complex(-5,21),
56:complex(-11,-17),57:complex(-11,-19),58:complex(-11,-23),59:complex(-11,-21),

60:complex(-5,-17),61:complex(-5,-19),62:complex(-5,-23),63:complex(-5,-21),
64:complex(-17,15),65:complex(-17,13),66:complex(-17,9),67:complex(-17,11),
68:complex(-17,1),69:complex(-17,3),70:complex(-17,7),71:complex(-17,5),
72:complex(-17,-15),73:complex(-17,-13),74:complex(-17,-9),75:complex(-17,-11),
76:complex(-17,-1),77:complex(-17,-3),78:complex(-17,-7),79:complex(-17,-5),

80:complex(-19,15),81:complex(-19,13),82:complex(-19,9),83:complex(-19,11),
84:complex(-19,1),85:complex(-19,3),86:complex(-19,7),87:complex(-19,5),
88:complex(-19,-15),89:complex(-19,-13),90:complex(-19,-9),91:complex(-19,-11),
92:complex(-19,-1),93:complex(-19,-3),94:complex(-19,-7),95:complex(-19,-5),
96:complex(-23,15),97:complex(-23,13),98:complex(-23,9),99:complex(-23,11),

100:complex(-23,1),101:complex(-23,3),102:complex(-23,7),103:complex(-23,5),
104:complex(-23,-15),105:complex(-23,-13),106:complex(-23,-9),107:complex(-23,-11),
108:complex(-23,-1),109:complex(-23,-3),110:complex(-23,-7),111:complex(-23,-5),
112:complex(-21,15),113:complex(-21,13),114:complex(-21,9),115:complex(-21,11),
116:complex(-21,1),117:complex(-21,3),118:complex(-21,7),119:complex(-21,5),

120:complex(-21,-15),121:complex(-21,-13),122:complex(-21,-9),123:complex(-21,-11),
124:complex(-21,-1),125:complex(-21,-3),126:complex(-21,-7),127:complex(-21,-5),
128:complex(-1,15),129:complex(-1,13),130:complex(-1,9),131:complex(-1,11),
132:complex(-1,1),133:complex(-1,3),134:complex(-1,7),135:complex(-1,5),
136:complex(-1,-15),137:complex(-1,-13),138:complex(-1,-9),139:complex(-1,-11),

140:complex(-1,-1),141:complex(-1,-3),142:complex(-1,-7),143:complex(-1,-5),144:complex(-3,15),
145:complex(-3,13),146:complex(-3,9),147:complex(-3,11),148:complex(-3,1),149:complex(-3,3),
150:complex(-3,7),151:complex(-3,5),152:complex(-3,-15),153:complex(-3,-13),154:complex(-3,-9),
155:complex(-3,-11),156:complex(-3,-1),157:complex(-3,-3),158:complex(-3,-7),159:complex(-3,-5),
160:complex(-7,15),161:complex(-7,13),162:complex(-7,9),163:complex(-7,11),164:complex(-7,1),

165:complex(-7,3),166:complex(-7,7),167:complex(-7,5),168:complex(-7,-15),169:complex(-7,-13),
170:complex(-7,-9),171:complex(-7,-11),172:complex(-7,-1),173:complex(-7,-3),174:complex(-7,-7),175:complex(-7,-5),
176:complex(-5,15),177:complex(-5,13),178:complex(-5,9),179:complex(-5,11),180:complex(-5,1),
181:complex(-5,3),182:complex(-5,7),183:complex(-5,5),184:complex(-5,-15),185:complex(-5,-13),
186:complex(-5,-9),187:complex(-5,-11),188:complex(-5,-1),189:complex(-5,-3),190:complex(-5,-7),

191:complex(-5,-5),192:complex(-15,15),193:complex(-15,13),194:complex(-15,9),195:complex(-15,11),
196:complex(-15,1),197:complex(-15,3),198:complex(-15,7),199:complex(-15,5),200:complex(-15,-15),
201:complex(-15,-13),202:complex(-15,-9),203:complex(-15,-11),204:complex(-15,-1),205:complex(-15,-3),
206:complex(-15,-7),207:complex(-15,-5),208:complex(-13,15),209:complex(-13,13),210:complex(-13,9),
211:complex(-13,11),212:complex(-13,1),213:complex(-13,3),214:complex(-13,7),215:complex(-13,5),
216:complex(-13,-15),217:complex(-13,-13),218:complex(-13,-9),219:complex(-13,-11),220:complex(-13,-1),

221:complex(-13,-3),222:complex(-13,-7),223:complex(-13,-5),224:complex(-9,15),225:complex(-9,13),
226:complex(-9,9),227:complex(-9,11),228:complex(-9,1),229:complex(-9,3),230:complex(-9,7),
231:complex(-9,5),232:complex(-9,-15),233:complex(-9,-13),234:complex(-9,-9),235:complex(-9,-11),
236:complex(-9,-1),237:complex(-9,-3),238:complex(-9,-7),239:complex(-9,-5),240:complex(-11,15),
241:complex(-11,13),242:complex(-11,9),243:complex(-11,11),244:complex(-11,1),245:complex(-11,3),

246:complex(-11,7),247:complex(-11,5),248:complex(-11,-15),249:complex(-11,-13),250:complex(-11,-9),
251:complex(-11,-11),252:complex(-11,-1),253:complex(-11,-3),254:complex(-11,-7),255:complex(-11,-5),

256:complex(15,17),257:complex(15,19),258:complex(15,23),259:complex(15,21),
260:complex(1,17),261:complex(1,19),262:complex(1,23),263:complex(1,21),
264:complex(15,-17),265:complex(15,-19),266:complex(15,-23),267:complex(15,-21),
268:complex(1,-17),269:complex(1,-19),270:complex(1,-23),271:complex(1,-21),
272:complex(13,17),273:complex(13,19),274:complex(13,23),275:complex(13,21),

276:complex(3,17),277:complex(3,19),278:complex(3,23),279:complex(3,21),
280:complex(13,-17),281:complex(13,-19),282:complex(13,-23),283:complex(13,-21),
284:complex(3,-17),285:complex(3,-19),286:complex(3,-23),287:complex(3,-21),
288:complex(9,17),289:complex(9,19),290:complex(9,23),291:complex(9,21),
292:complex(7,17),293:complex(7,19),294:complex(7,23),295:complex(7,21),

296:complex(9,-17),297:complex(9,-19),298:complex(9,-23),299:complex(9,-21),
300:complex(7,-17),301:complex(7,-19),302:complex(7,-23),303:complex(7,-21),
304:complex(11,17),305:complex(11,19),306:complex(11,23),307:complex(11,21),
308:complex(5,17),309:complex(5,19),310:complex(5,23),311:complex(5,21),
312:complex(11,-17),313:complex(11,-19),314:complex(11,-23),315:complex(11,-21),

316:complex(5,-17),317:complex(5,-19),318:complex(5,-23),319:complex(5,-21),
320:complex(17,15),321:complex(17,13),322:complex(17,9),323:complex(17,11),
324:complex(17,1),325:complex(17,3),326:complex(17,7),327:complex(17,5),
328:complex(17,-15),329:complex(17,-13),330:complex(17,-9),331:complex(17,-11),
332:complex(17,-1),333:complex(17,-3),334:complex(17,-7),335:complex(17,-5),

336:complex(19,15),337:complex(19,13),338:complex(19,9),339:complex(19,11),
340:complex(19,1),341:complex(19,3),342:complex(19,7),343:complex(19,5),
344:complex(19,-15),345:complex(19,-13),346:complex(19,-9),347:complex(19,-11),
348:complex(19,-1),349:complex(19,-3),350:complex(19,-7),351:complex(19,-5),
352:complex(23,15),353:complex(23,13),354:complex(23,9),355:complex(23,11),

356:complex(23,1),357:complex(23,3),358:complex(23,7),359:complex(23,5),
360:complex(23,-15),361:complex(23,-13),362:complex(23,-9),363:complex(23,-11),
364:complex(23,-1),365:complex(23,-3),366:complex(23,-7),367:complex(23,-5),
368:complex(21,15),369:complex(21,13),370:complex(21,9),371:complex(21,11),
372:complex(21,1),373:complex(21,3),374:complex(21,7),375:complex(21,5),

376:complex(21,-15),377:complex(21,-13),378:complex(21,-9),379:complex(21,-11),
380:complex(21,-1),381:complex(21,-3),382:complex(21,-7),383:complex(21,-5),
384:complex(1,15),385:complex(1,13),386:complex(1,9),387:complex(1,11),
388:complex(1,1),389:complex(1,3),390:complex(1,7),391:complex(1,5),
392:complex(1,-15),393:complex(1,-13),394:complex(1,-9),395:complex(1,-11),

396:complex(1,-1),397:complex(1,-3),398:complex(1,-7),399:complex(1,-5),400:complex(3,15),
401:complex(3,13),402:complex(3,9),403:complex(3,11),404:complex(3,1),405:complex(3,3),
406:complex(3,7),407:complex(3,5),408:complex(3,-15),409:complex(3,-13),410:complex(3,-9),
411:complex(3,-11),412:complex(3,-1),413:complex(3,-3),414:complex(3,-7),415:complex(3,-5),
416:complex(7,15),417:complex(7,13),418:complex(7,9),419:complex(7,11),420:complex(7,1),

421:complex(7,3),422:complex(7,7),423:complex(7,5),424:complex(7,-15),425:complex(7,-13),
426:complex(7,-9),427:complex(7,-11),428:complex(7,-1),429:complex(7,-3),430:complex(7,-7),431:complex(7,-5),
432:complex(5,15),433:complex(5,13),434:complex(5,9),435:complex(5,11),436:complex(5,1),
437:complex(5,3),438:complex(5,7),439:complex(5,5),440:complex(5,-15),441:complex(5,-13),
442:complex(5,-9),443:complex(5,-11),444:complex(5,-1),445:complex(5,-3),446:complex(5,-7),

447:complex(5,-5),448:complex(15,15),449:complex(15,13),450:complex(15,9),451:complex(15,11),
452:complex(15,1),453:complex(15,3),454:complex(15,7),455:complex(15,5),456:complex(15,-15),
457:complex(15,-13),458:complex(15,-9),459:complex(15,-11),460:complex(15,-1),461:complex(15,-3),
462:complex(15,-7),463:complex(15,-5),464:complex(13,15),465:complex(13,13),466:complex(13,9),
467:complex(13,11),468:complex(13,1),469:complex(13,3),470:complex(13,7),471:complex(13,5),
472:complex(13,-15),473:complex(13,-13),474:complex(13,-9),475:complex(13,-11),476:complex(13,-1),

477:complex(13,-3),478:complex(13,-7),479:complex(13,-5),480:complex(9,15),481:complex(9,13),
482:complex(9,9),483:complex(9,11),484:complex(9,1),485:complex(9,3),486:complex(9,7),
487:complex(9,5),488:complex(9,-15),489:complex(9,-13),490:complex(9,-9),491:complex(9,-11),
492:complex(9,-1),493:complex(9,-3),494:complex(9,-7),495:complex(9,-5),496:complex(11,15),
497:complex(11,13),498:complex(11,9),499:complex(11,11),500:complex(11,1),501:complex(11,3),

502:complex(11,7),503:complex(11,5),504:complex(11,-15),505:complex(11,-13),506:complex(11,-9),
507:complex(11,-11),508:complex(11,-1),509:complex(11,-3),510:complex(11,-7),511:complex(11,-5)
}

def duplicates_in_string(dic):
    rev_dict = {}

    for key, value in dic.items():
        rev_dict.setdefault(value, set()).add(key)

    result = [key for key, values in rev_dict.items()
              if len(values) > 1]

    # printing result
    print("duplicate values", str(result))

mapper1 = tuple(x for x in range(0,512))
mapper2 = 328,1,2,376,4,348,367,7,8,436,484,11,358,13,14,357,16,345,361,19,333,21,22,381,421,25,26,501,28,375,372,31,32,\
          346,362,35,334,37,38,382,454,41,42,453,44,327,324,47,331,49,50,379,52,351,364,55,56,471,468,59,342,61,62,341,\
          264,65,66,312,68,284,300,71,72,406,416,75,294,77,78,293,80,281,297,83,269,85,86,317,391,89,90,433,92,311,308,95,\
          96,282,298,99,270,101,102,318,386,105,106,385,108,263,260,111,267,113,114,315,116,287,303,119,120,403,400,123,\
          278,125,126,277,460,129,130,508,132,412,428,135,136,355,352,139,448,141,142,336,144,477,493,147,397,149,150,445,\
          370,153,154,369,156,465,321,159,160,478,494,163,398,165,166,446,322,169,170,466,172,272,482,175,463,177,178,511,\
          180,415,431,183,184,339,451,187,257,189,190,499,192,472,488,195,392,197,198,440,388,201,202,434,204,291,288,207,\
          457,209,210,505,212,409,425,215,216,405,419,219,306,221,222,305,458,225,226,506,228,410,426,231,232,502,422,235,\
          258,237,238,496,240,475,491,243,395,245,246,443,487,249,250,439,252,275,481,255,256,188,236,259,110,261,262,109,\
          64,265,266,112,268,84,100,271,173,273,274,253,276,127,124,279,280,81,97,283,69,285,286,117,206,289,290,205,\
          292,79,76,295,296,82,98,299,70,301,302,118,304,223,220,307,94,309,310,93,67,313,314,115,316,87,103,319,\
          320,158,168,323,46,325,326,45,0,329,330,48,332,20,36,335,143,337,338,185,340,63,60,343,344,17,33,347,5,349,350,53,\
          138,353,354,137,356,15,12,359,360,18,34,363,6,365,366,54,368,155,152,371,30,373,374,29,3,377,378,51,380,23,39,383,\
          384,107,104,387,200,389,390,88,196,393,394,244,396,148,164,399,122,401,402,121,404,217,73,407,408,213,229,411,133,413,414,181,\
          74,417,418,218,420,24,234,423,424,214,230,427,134,429,430,182,432,91,203,435,9,437,438,251,199,441,442,247,444,151,167,447,\
          140,449,450,186,452,43,40,455,456,208,224,459,128,461,462,176,464,157,171,467,58,469,470,57,193,473,474,241,476,145,161,479,\
          480,254,174,483,10,485,486,248,194,489,490,242,492,146,162,495,239,497,498,191,500,27,233,503,504,211,227,507,131,509,510,179
print(len(mapper2))

maps = [mapper1,mapper2]
print(fitness(mapper1, mapper1, map))
print(fitness(mapper1, mapper2, map))
Maps = []
for i in range(12):
    ind = random.randint(0, len(maps)-1)
    Maps.append(maps[ind])
Maps = tuple(Maps)
A = []
#print(Maps)
for j in range(10000):
    C = crossoverPopulation(Maps, map)
    M = mutatePopulation(C, 0.40)
    A = AddToPopulation(Maps, M, A)
    #A = AddToPopulation(M)
    Maps = nextGeneration(mapper1, A, 12, map)
    print(rank_fitness(mapper1, Maps, map))
    A = []
print(Maps[0])