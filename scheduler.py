from evolve import *
import time

population_size = 40
mutation_rate = .07
generations = 200



'''
steps:
create_population -> make and mutate new population (make pop_size new children) -> get average fitness -> repeat '''

# initialize population

start_time = time.time()

pop = create_population(population_size)

pop_data = pop_max_min(pop)
print("Generation: {}\tAvg Fitness: {}\tBest Fitness: {:.2f}".format(0,pop_data[4], pop_data[0]))
best_schedule = pop[pop_data[2]]
best = 0
for gen in range(generations):
    pop = make_new_generation(pop, population_size, mutation_rate)
    pop_data = pop_max_min(pop)

    # elitism optimization
    # preserves the fittest
    if pop_data[0] < best:
        # remove lowest from pop
        del pop[pop_data[3]]
        pop.append(best_schedule)

    total_time = time.time() - start_time
    print("Generation: {}\tAvg Fitness: {}\tBest Fitness: {}\tAvg Gen Speed: {:.2f}".format(gen+1,pop_data[4], pop_data[0],total_time/(gen+1)))
    if pop_data[0] > best:
        best_schedule = pop[pop_data[2]]
        best = pop_data[0]

print(best, best_schedule)

total_time = time.time() - start_time
print("Total Time:\t{:.2f} seconds".format(total_time))
print("Avg Time per Generation:\t{:.2f} seconds".format(total_time/(gen+1)))

