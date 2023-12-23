from perceptron import Perceptron
from population import *

population = Population ()

evolution = 100

for i in range(evolution):
    population.Selection()
    population.Reproduction()
    population.Mutate()



