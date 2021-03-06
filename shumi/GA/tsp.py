import GA
import numpy as np
import math
import copy
import matplotlib.pyplot as plt

i = np.arange(0, 1, 0.05)
x = list(np.cos(2*np.pi*i))
y = list(np.sin(2*np.pi*i))

save_path = 'image'

def distance(i, j):
    return math.sqrt(math.pow(x[i]-x[j], 2) + pow(y[i]-y[j], 2))
def all_distance(l):
    return sum([distance(l[i], l[i+1]) for i in range(len(l)-1)])

ga = GA.GA(list(range(20)), 20, 20, 0.03, True)
for j in range(1, 501):
    for i in range(20):
        ga.one_point_crossover()
    
    ga.mutation()
    ga.fitness = [all_distance(g) for g in ga.children_gene]
    
    # 優性保存
    fitness = [all_distance(g) for g in ga.gene]
    print(min(fitness), ga.gene[fitness.index(min(fitness))])
    if (j % 100 == 0 or j == 1):
        plt.xlim(-1.1, 1.1)
        plt.ylim(-1.1, 1.1)
        plt.plot([x[g] for g in ga.gene[fitness.index(min(fitness))]], [y[g] for g in ga.gene[fitness.index(min(fitness))]])
        plt.savefig(save_path + '/tsp20_{0:03}'.format(j))
        plt.close()
    gene = copy.deepcopy(ga.gene)
    ga.gene = []
    for i in range(2):
        ga.gene.append(gene[fitness.index(min(fitness))])
        del gene[fitness.index(min(fitness))]
        del fitness[fitness.index(min(fitness))]
    ga.roulette_method(18)
    ga.fitness = []