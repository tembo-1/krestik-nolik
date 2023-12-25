import random
import math
from neuron import Neuron
import copy
import json

class Perceptron:

    def __init__(self):
        self.num_gate = 9
        self.in_sloy = [20, 10, 5, 1]
        self.inputNeuron = [9, 20, 10, 5, 1]
        self.num_sloy = 4
        self.score = 0
        self.new_gate = [
            [0.0] * self.num_gate,
            [0.0] * self.in_sloy[0],
            [0.0] * self.in_sloy[1],
            [0.0] * self.in_sloy[2],
            [0.0] * self.in_sloy[3]
        ]
        self.desk = [0.0] * 9
        self.sloy = []

        for i in range( len(self.in_sloy) ):
            my_neyron = []
            for j in range(self.in_sloy[i]):
                my_neyron.append(  Neuron(len(self.new_gate[i])) )
            self.sloy.append(my_neyron)

    def read(self):
        with open('data.json') as file:
            data = json.load(file)

        for i in range(self.num_sloy):
            for j in range(self.in_sloy[i]):
                for n in data:
                    if (n['neuron'] == j and n['sloy'] == i):
                        self.sloy[i][j].porog = n['porog']
                        self.sloy[i][j].weight = n['weight']              

    def GetExit(self, gate):
        betta = 1
        result = 0

        for g in range (len(gate)):
            self.new_gate[0][g] = gate[g]


        for i in range(self.num_sloy):
            for n in range(self.in_sloy[i]):
                work = 0
                for w in range( len(self.new_gate[i]) ):
                    work += self.sloy[i][n].weight[w] * self.new_gate[i][w]
                if (i != self.num_sloy - 1):
                    self.new_gate[i + 1][n] = 1 / (1 + math.exp( -betta * (work - self.sloy[i][n].porog) ))    
                else:
                    result = 1 / (1 + math.exp( -betta * (work - self.sloy[i][n].porog) ))

        return result

    def Crossover(self, parent):
        same = random.uniform(0, 1)
        child = Perceptron()

        for i in range(self.num_sloy):
            for j in range(self.in_sloy[i]):
                child.sloy[i][j].porog = same * self.sloy[i][j].porog + (1 - same) * parent.sloy[i][j].porog
                for k in range(len(self.new_gate[i])):
                    child.sloy[i][j].weight[k] = same * self.sloy[i][j].weight[k] + (1 - same) * parent.sloy[i][j].weight[k]

        return child                
        
    def Mutating(self, mutate):
        for i in range(self.num_sloy):
            for j in range(self.in_sloy[i]):
                self.sloy[i][j].porog *= random.uniform(1 - mutate, 1 + mutate)
                for k in range(len(self.new_gate[i])):
                    self.sloy[i][j].weight[k] *= random.uniform(1 - mutate, 1 + mutate)

    def step(self, desk, number):
        max = -100
        max_i = 0

        for i in range(len(desk)):
            if (desk[i] == 0):

                desk_temp = copy.deepcopy(desk)

                if (number % 2):
                    desk_temp[i] = 1
                else:
                    desk_temp[i] = -1
                    for j in range(len(desk_temp)):
                        desk_temp[j] = -desk_temp[j]

                if (self.GetExit(desk_temp) > max):
                    max = self.GetExit(desk_temp)        
                    max_i = i

        return max_i                