from evolve import *

pop = create_population(100)

top = 0
for x, y in enumerate(pop):
    if y[0] > top:
        top = y[0]
        best = x
    #print("{}".format(y[0]),end = '\t')

print("Best Fitness: {}".format(pop[best][0]))