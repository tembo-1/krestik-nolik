from perceptron import Perceptron
from population import *

neuron = Population ()

game = neuron.Selection()



for i in neuron.krestik:
    print(i.score)

print('================')

for i in neuron.nolik:
    print(i.score)
    


# print(
#     f"{game[0]}|{game[1]}|{game[2]}\n"\
#     f"{game[3]}|{game[4]}|{game[5]}\n"\
#     f"{game[6]}|{game[7]}|{game[8]}\n"
# )

