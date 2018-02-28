from evolve import *

population_size = 150
mutation_rate = .05
generations = 150

'''
steps:
create_population -> make and mutate new population (make pop_size new children) -> get average fitness -> repeat '''

# initialize population
pop = create_population(population_size)
print(pop)

pop_data = pop_max_min(pop)
print("Generation: {}\tAvg Fitness: {}\tBest Fitness: {}".format(0,pop_data[4], pop_data[0]))
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


    print("Generation: {}\tAvg Fitness: {}\tBest Fitness: {}".format(gen+1,pop_data[4], pop_data[0]))
    if pop_data[0] > best:
        best_schedule = pop[pop_data[2]]
        best = pop_data[0]

print(best, best_schedule)

