from evolve import *
import time
import sys

population_size = 60
mutation_rate = .3
generations =50


#not currently using
preserve = 4 # this guarantees that the top X number of DNA will be preserved into the next generation



'''
steps:
create_population -> make and mutate new population (make pop_size new children) -> get average fitness -> repeat '''

# initialize population

start_time = time.time()
print(the_random_seed)
pop = create_population(population_size)

pop_data = pop_max_min(pop)
print("Generation: {}\tAvg Fitness: {}\tBest Fitness: {:.2f}".format(0,pop_data[4], pop_data[0]))
best_schedule = pop[pop_data[2]]
best = 0 # pop_data[0]
# score 1571!
best_ever = {20012: '2018-03-02 09:00:00', 20157: '2018-02-28 13:00:00', 20158: '2018-02-28 09:00:00', 20162: '2018-03-01 10:00:00', 20167: '2018-03-01 07:30:00', 20183: '2018-03-02 14:30:00', 20185: '2018-02-28 08:00:00', 20188: '2018-03-01 09:00:00', 20197: '2018-03-01 13:00:00', 20209: '2018-02-28 15:00:00', 20210: '2018-03-02 15:00:00', 20222: '2018-03-01 08:00:00', 20238: '2018-02-28 07:30:00', 20242: '2018-03-02 08:30:00', 20250: '2018-02-28 15:30:00', 20267: '2018-03-02 11:00:00', 20306: '2018-02-28 12:30:00', 20307: '2018-02-28 08:30:00', 20319: '2018-02-28 08:00:00', 20321: '2018-03-01 11:00:00', 20322: '2018-03-02 13:00:00', 20327: '2018-03-01 14:00:00', 20328: '2018-03-02 14:30:00', 20333: '2018-02-28 09:00:00', 20344: '2018-02-28 14:00:00', 20345: '2018-02-28 13:30:00', 20351: '2018-03-01 12:30:00', 20353: '2018-02-28 07:30:00', 20360: '2018-03-02 10:00:00', 20361: '2018-02-28 08:30:00', 20363: '2018-03-01 07:30:00', 20364: '2018-03-02 14:00:00', 20373: '2018-02-28 10:00:00', 20374: '2018-03-02 11:30:00', 20376: '2018-02-28 07:30:00', 20378: '2018-02-28 11:00:00', 20388: '2018-03-02 14:30:00', 20395: '2018-03-01 14:00:00', 20396: '2018-03-02 10:00:00', 20405: '2018-03-02 14:00:00', 20415: '2018-03-01 08:00:00', 20416: '2018-03-01 08:00:00', 20417: '2018-03-01 15:30:00', 20418: '2018-03-01 07:30:00', 20421: '2018-02-28 08:30:00', 20422: '2018-02-28 08:00:00', 20423: '2018-03-01 15:00:00', 20425: '2018-03-01 15:30:00', 20426: '2018-03-01 11:00:00', 20427: '2018-02-28 08:30:00', 20429: '2018-02-28 13:30:00', 20430: '2018-02-28 15:00:00', 20434: '2018-03-02 08:00:00', 20464: '2018-03-02 11:00:00', 20474: '2018-03-02 14:00:00', 20475: '2018-03-02 13:30:00', 20478: '2018-02-28 07:30:00', 20483: '2018-02-28 12:30:00', 20484: '2018-02-28 13:00:00', 20486: '2018-03-01 12:30:00', 20497: '2018-03-02 07:30:00', 20501: '2018-02-28 09:00:00', 20503: '2018-03-01 07:30:00', 20506: '2018-03-01 14:00:00', 20507: '2018-02-28 16:00:00', 20511: '2018-02-28 08:00:00', 20516: '2018-03-01 13:30:00', 20519: '2018-02-28 10:00:00', 20523: '2018-03-02 07:30:00', 20527: '2018-03-02 10:30:00', 20534: '2018-03-01 15:00:00', 20536: '2018-03-01 10:00:00', 20539: '2018-03-02 11:00:00', 20549: '2018-03-02 15:00:00', 20554: '2018-02-28 09:00:00', 20564: '2018-03-01 13:00:00', 20574: '2018-03-02 11:00:00', 20576: '2018-03-02 08:30:00', 20577: '2018-03-01 12:30:00', 20579: '2018-02-28 15:00:00', 20583: '2018-03-02 11:30:00', 20585: '2018-02-28 14:00:00', 20587: '2018-03-02 13:00:00', 20606: '2018-02-28 15:00:00', 20609: '2018-02-28 15:30:00', 20614: '2018-03-01 13:00:00', 20619: '2018-02-28 14:00:00', 20642: '2018-02-28 15:30:00', 20643: '2018-02-28 15:30:00', 20655: '2018-03-01 08:30:00', 20656: '2018-03-01 10:30:00', 20659: '2018-02-28 08:00:00', 20661: '2018-03-01 13:30:00', 20674: '2018-03-01 14:00:00', 20677: '2018-03-01 07:30:00', 20679: '2018-02-28 13:00:00', 20682: '2018-03-01 10:00:00', 20683: '2018-03-01 14:00:00', 20684: '2018-02-28 09:00:00', 20687: '2018-03-01 10:00:00', 20689: '2018-03-02 10:00:00', 20691: '2018-03-02 13:00:00', 20711: '2018-02-28 10:00:00', 20715: '2018-03-02 14:00:00', 20725: '2018-03-02 11:30:00', 20730: '2018-02-28 11:00:00', 20732: '2018-03-02 07:30:00', 20736: '2018-02-28 10:00:00', 20737: '2018-03-01 08:00:00', 20738: '2018-02-28 12:30:00', 20744: '2018-03-02 07:30:00', 20746: '2018-02-28 16:30:00', 20752: '2018-02-28 10:00:00', 20756: '2018-02-28 11:00:00', 20764: '2018-02-28 07:30:00', 20772: '2018-02-28 16:00:00', 20797: '2018-02-28 16:30:00', 20800: '2018-02-28 14:00:00', 20832: '2018-03-01 10:00:00', 20844: '2018-03-01 15:00:00', 20899: '2018-03-01 08:30:00', 20920: '2018-03-02 13:30:00', 20926: '2018-02-28 10:30:00', 20927: '2018-03-01 12:30:00', 20941: '2018-03-01 15:00:00', 20943: '2018-03-01 13:00:00', 20944: '2018-03-01 09:00:00', 20949: '2018-02-28 13:30:00', 20967: '2018-03-02 11:00:00', 20971: '2018-02-28 12:30:00', 20974: '2018-03-02 08:00:00', 20980: '2018-02-28 10:30:00', 20988: '2018-02-28 13:00:00', 21052: '2018-03-02 13:30:00', 21091: '2018-03-02 14:30:00', 21109: '2018-03-01 08:30:00', 21124: '2018-02-28 11:00:00', 21128: '2018-03-02 15:00:00', 21129: '2018-03-02 14:30:00', 21157: '2018-03-01 10:30:00', 21194: '2018-03-02 10:30:00', 21208: '2018-02-28 14:00:00', 21215: '2018-03-02 08:00:00', 21228: '2018-03-02 13:30:00', 21232: '2018-03-01 13:30:00', 21237: '2018-02-28 12:30:00', 21254: '2018-03-01 10:30:00', 21266: '2018-02-28 10:30:00', 21283: '2018-02-28 15:30:00', 21284: '2018-03-01 16:30:00', 21290: '2018-03-02 13:00:00', 21295: '2018-03-02 08:00:00', 21312: '2018-03-01 16:00:00', 21318: '2018-02-28 16:00:00', 21350: '2018-03-02 08:30:00', 21354: '2018-02-28 13:30:00', 21357: '2018-03-02 09:00:00', 21362: '2018-03-01 13:00:00', 21367: '2018-02-28 16:30:00', 21376: '2018-03-02 08:30:00', 21380: '2018-03-01 09:00:00', 21383: '2018-03-01 15:30:00', 21401: '2018-03-02 09:00:00', 21403: '2018-03-01 15:30:00', 21642: '2018-03-01 09:00:00', 21649: '2018-03-01 11:00:00', 21651: '2018-03-01 08:30:00', 21659: '2018-02-28 16:00:00', 21668: '2018-03-02 10:00:00', 21678: '2018-03-02 15:00:00', 21687: '2018-03-01 08:30:00', 21690: '2018-03-02 13:30:00', 21692: '2018-02-28 16:30:00', 21726: '2018-03-01 09:00:00', 21741: '2018-03-02 10:00:00', 21746: '2018-02-28 10:30:00', 21753: '2018-03-01 16:00:00', 21775: '2018-03-02 08:00:00', 21845: '2018-02-28 11:00:00', 21865: '2018-02-28 15:00:00', 21875: '2018-03-01 16:30:00', 21879: '2018-03-02 13:00:00', 21882: '2018-02-28 08:30:00', 21884: '2018-03-01 13:30:00', 21885: '2018-03-02 10:30:00', 22407: '2018-03-01 15:30:00', 22412: '2018-03-01 16:00:00', 22617: '2018-03-01 11:00:00', 22770: '2018-03-01 16:00:00', 22884: '2018-03-02 10:30:00', 22893: '2018-03-01 10:30:00', 22894: '2018-03-02 15:00:00', 22897: '2018-03-02 08:30:00', 22912: '2018-03-01 12:30:00', 22914: '2018-03-01 08:00:00', 22969: '2018-03-02 11:30:00', 22971: '2018-02-28 13:00:00', 22986: '2018-03-01 16:00:00', 22988: '2018-02-28 13:30:00', 22998: '2018-02-28 10:30:00', 23006: '2018-03-01 16:30:00', 23052: '2018-03-01 10:30:00', 23101: '2018-03-01 16:30:00', 23146: '2018-03-01 16:30:00', 23205: '2018-03-02 14:00:00', 23467: '2018-02-28 16:00:00', 23487: '2018-03-01 13:30:00', 23546: '2018-02-28 16:30:00'}
best_schedule = [fitness(best_ever),best_ever]
best = fitness(best_ever)

for gen in range(generations):
    pop = make_new_generation(pop, population_size, mutation_rate/((1+gen)**.5), gen, preserve)
    pop_data = pop_max_min(pop)

    # elitism optimization
    # preserves the fittest
    if pop_data[0] < best:
        # remove lowest from pop
        del pop[pop_data[3]]
        pop.append(best_schedule)


    total_time = time.time() - start_time
    #print("Generation: {}\tAvg Fitness: {}\tBest Fitness: {}\tAvg Gen Speed: {:.2f}".format(gen+1,pop_data[4], pop_data[0],total_time/(gen+1)))
    print(".", end = ' ')
    if (gen+1)%50 == 0:
        print()
        print("Generation: {}\nAvg Fitness: {:.2f}\nBest Fitness: {:.2f}\nAvg Gen Speed: {:.2f}".format(gen + 1, pop_data[4],
                                                                                                pop_data[0],
                                                                                                total_time / (gen + 1)))
    sys.stdout.flush()
    if pop_data[0] > best:
        # new best schedule
        best_schedule = pop[pop_data[2]]
        best = pop_data[0]
        print()
        print("*****************************")
        print("New Best: ",best)
        print(evaluate_dna(best_schedule[1]))
        print("Generation: {}\tAvg Fitness: {:.2f}\tBest Fitness: {}\tAvg Gen Speed: {:.2f}".format(gen + 1, pop_data[4], pop_data[0], total_time / (gen + 1)))
        print("*****************************")

print(best, best_schedule)

print(evaluate_dna(best_schedule[1]))
total_time = time.time() - start_time
print("Total Time:\t{:.2f} seconds".format(total_time))
print("Avg Time per Generation:\t{:.2f} seconds".format(total_time/(gen+1)))

lisa_dna={20222: '2018-03-01 08:00:00', 22884: '2018-02-28 10:00:00', 20797: '2018-03-02 11:30:00', 20800: '2018-02-28 16:00:00', 21254: '2018-03-01 08:00:00', 22617: '2018-03-01 08:30:00', 21642: '2018-03-02 10:30:00', 20474: '2018-03-02 13:00:00', 20475: '2018-03-02 10:00:00', 20306: '2018-02-28 14:00:00', 20478: '2018-02-28 10:00:00', 20307: '2018-03-02 07:30:00', 21232: '2018-03-01 10:30:00', 22412: '2018-03-01 16:00:00', 21266: '2018-03-02 08:00:00', 23467: '2018-02-28 14:00:00', 20157: '2018-02-28 14:00:00', 20415: '2018-03-01 15:30:00', 22893: '2018-03-01 07:30:00', 22894: '2018-03-02 13:00:00', 20642: '2018-02-28 09:00:00', 21124: '2018-02-28 12:30:00', 20643: '2018-02-28 15:00:00', 20197: '2018-03-01 12:30:00', 20483: '2018-03-01 13:00:00', 20484: '2018-03-01 13:30:00', 20188: '2018-03-01 16:30:00', 21649: '2018-03-01 11:00:00', 20434: '2018-03-02 09:00:00', 20486: '2018-02-28 14:00:00', 22897: '2018-03-02 08:30:00', 20772: '2018-03-01 14:00:00', 21651: '2018-03-01 09:00:00', 20167: '2018-03-01 08:30:00', 21128: '2018-03-02 13:00:00', 21129: '2018-03-02 13:30:00', 20319: '2018-02-28 08:00:00', 21283: '2018-02-28 15:30:00', 20321: '2018-03-01 13:00:00', 21659: '2018-03-01 16:30:00', 21284: '2018-03-01 15:00:00', 20322: '2018-03-02 14:00:00', 20941: '2018-03-01 16:30:00', 23205: '2018-03-02 14:00:00', 21290: '2018-03-01 13:00:00', 21879: '2018-03-01 11:00:00', 21237: '2018-02-28 12:30:00', 20497: '2018-02-28 07:30:00', 21052: '2018-03-01 08:30:00', 20655: '2018-03-01 10:00:00', 22912: '2018-03-01 12:30:00', 21295: '2018-03-02 10:00:00', 20764: '2018-02-28 08:30:00', 20943: '2018-03-02 10:30:00', 20656: '2018-02-28 13:00:00', 20659: '2018-02-28 07:30:00', 20501: '2018-02-28 09:00:00', 22770: '2018-03-02 10:30:00', 20832: '2018-03-01 08:30:00', 22914: '2018-02-28 11:00:00', 20661: '2018-02-28 08:00:00', 20162: '2018-03-01 07:30:00', 21668: '2018-03-02 11:00:00', 20503: '2018-02-28 09:00:00', 20920: '2018-02-28 12:30:00', 20944: '2018-03-01 08:00:00', 20506: '2018-03-02 14:00:00', 20507: '2018-03-01 16:00:00', 20416: '2018-03-01 10:30:00', 20012: '2018-03-02 11:30:00', 20417: '2018-03-01 16:30:00', 20511: '2018-02-28 13:30:00', 20183: '2018-03-01 09:00:00', 20327: '2018-03-02 11:30:00', 20328: '2018-03-02 11:00:00', 20949: '2018-02-28 14:00:00', 20844: '2018-03-01 14:00:00', 20516: '2018-03-01 13:30:00', 20519: '2018-02-28 08:30:00', 21678: '2018-03-02 13:00:00', 20333: '2018-02-28 13:00:00', 21312: '2018-03-01 13:30:00', 20674: '2018-03-01 15:30:00', 21157: '2018-03-01 09:00:00', 20523: '2018-03-02 09:00:00', 20677: '2018-03-02 07:30:00', 20527: '2018-03-02 08:00:00', 21318: '2018-03-01 15:30:00', 21687: '2018-03-02 10:30:00', 21882: '2018-02-28 11:00:00', 20679: '2018-02-28 12:30:00', 21690: '2018-03-02 11:00:00', 21885: '2018-03-02 14:00:00', 21692: '2018-02-28 10:30:00', 20344: '2018-02-28 15:00:00', 20158: '2018-03-01 07:30:00', 20418: '2018-03-01 08:30:00', 20682: '2018-03-01 15:00:00', 20683: '2018-03-02 10:00:00', 23052: '2018-03-02 07:30:00', 20606: '2018-02-28 16:30:00', 20684: '2018-02-28 15:30:00', 20345: '2018-02-28 14:00:00', 20534: '2018-03-02 08:30:00', 20687: '2018-03-01 07:30:00', 20536: '2018-03-01 08:00:00', 20351: '2018-03-01 10:30:00', 20689: '2018-03-02 08:30:00', 23146: '2018-03-01 15:30:00', 20691: '2018-03-01 13:00:00', 20353: '2018-02-28 13:00:00', 21091: '2018-03-02 11:00:00', 20539: '2018-03-02 14:30:00', 21228: '2018-03-02 11:30:00', 20421: '2018-02-28 10:30:00', 20422: '2018-02-28 11:00:00', 20238: '2018-02-28 13:30:00', 20360: '2018-03-02 08:30:00', 20361: '2018-02-28 12:30:00', 20619: '2018-02-28 07:30:00', 20927: '2018-03-01 12:30:00', 23487: '2018-02-28 10:00:00', 20549: '2018-03-02 13:30:00', 20185: '2018-02-28 07:30:00', 20967: '2018-03-02 07:30:00', 20242: '2018-02-28 09:00:00', 20363: '2018-02-28 11:00:00', 20364: '2018-03-02 13:00:00', 20423: '2018-03-01 15:00:00', 20554: '2018-03-01 08:00:00', 20971: '2018-02-28 13:00:00', 20373: '2018-02-28 13:30:00', 20374: '2018-03-02 11:00:00', 20711: '2018-02-28 10:00:00', 20974: '2018-03-02 09:00:00', 23101: '2018-03-01 16:30:00', 20609: '2018-02-28 13:30:00', 20715: '2018-03-02 13:30:00', 20425: '2018-02-28 15:30:00', 20376: '2018-02-28 08:30:00', 21403: '2018-03-01 16:00:00', 20378: '2018-03-01 10:00:00', 20980: '2018-02-28 09:00:00', 20426: '2018-03-01 12:30:00', 20926: '2018-02-28 08:00:00', 23546: '2018-02-28 13:00:00', 21884: '2018-03-01 12:30:00', 21775: '2018-03-01 14:00:00', 21401: '2018-03-01 08:30:00', 21350: '2018-03-01 09:00:00', 22969: '2018-03-02 14:30:00', 20564: '2018-03-01 13:30:00', 21194: '2018-02-28 09:00:00', 21726: '2018-03-02 10:00:00', 22971: '2018-03-01 10:30:00', 20250: '2018-02-28 16:30:00', 21875: '2018-03-01 16:00:00', 20388: '2018-03-02 14:30:00', 20725: '2018-03-02 13:00:00', 21354: '2018-02-28 10:00:00', 20988: '2018-02-28 13:30:00', 20574: '2018-03-02 13:30:00', 20899: '2018-02-28 15:00:00', 20576: '2018-03-02 08:00:00', 20395: '2018-03-01 15:30:00', 20730: '2018-02-28 10:30:00', 20730: '2018-03-01 11:00:00', 21357: '2018-03-02 13:30:00', 20396: '2018-03-02 10:00:00', 21109: '2018-03-01 07:30:00', 22986: '2018-03-01 15:00:00', 20732: '2018-02-28 07:30:00', 20427: '2018-02-28 08:30:00', 20577: '2018-03-01 10:00:00', 20736: '2018-02-28 11:00:00', 21362: '2018-03-01 11:00:00', 21741: '2018-03-02 08:30:00', 20579: '2018-02-28 08:00:00', 20737: '2018-03-01 11:00:00', 20738: '2018-03-01 10:00:00', 20209: '2018-02-28 16:30:00', 22988: '2018-03-01 10:30:00', 21208: '2018-02-28 15:30:00', 21367: '2018-02-28 16:00:00', 20744: '2018-03-02 08:00:00', 21746: '2018-02-28 10:00:00', 22407: '2018-03-01 10:00:00', 22998: '2018-02-28 10:30:00', 21845: '2018-02-28 11:00:00', 20746: '2018-02-28 16:30:00', 20429: '2018-02-28 15:00:00', 20583: '2018-03-02 11:30:00', 21215: '2018-03-02 08:00:00', 21376: '2018-03-02 08:30:00', 20585: '2018-02-28 16:30:00', 20405: '2018-03-02 14:30:00', 20210: '2018-03-02 09:00:00', 20267: '2018-02-28 10:30:00', 20267: '2018-03-02 10:30:00', 20587: '2018-03-02 14:00:00', 21753: '2018-03-01 15:00:00', 20752: '2018-03-02 07:30:00', 21380: '2018-03-01 12:30:00', 21383: '2018-03-01 14:00:00', 20430: '2018-02-28 08:30:00', 20614: '2018-03-01 07:30:00', 20464: '2018-02-28 15:00:00', 23006: '2018-03-02 09:00:00', 20756: '2018-02-28 16:00:00', 21865: '2018-02-28 16:00:00'}
print(fitness(lisa_dna),evaluate_dna(lisa_dna))

save_best_schedule(best_schedule[1], population_size, the_random_seed, mutation_rate)
print(the_random_seed)