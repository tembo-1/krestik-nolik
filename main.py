from perceptron import Perceptron
from population import *
import json

population = Population ()

# population.Selection()

evolution = 70

for i in range(evolution):
    population.Selection()
    population.Reproduction()
    population.Mutate()

data = population.person

winner:Population
max = 0

for i in data:
    if (i.score > max):
        winner = i

data = []

for i in range(4):
    for j in range(winner.in_sloy[i]):
        data.append({"sloy": i, "porog" : winner.sloy[i][j].porog, "weight" : winner.sloy[i][j].weight})
     

with open('data.json', 'w') as f:
    json.dump(data, f)



