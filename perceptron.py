import random
import math
from neuron import *

class Perceptron:

    def __init__(self,
                 num_input: int,
                 num_hidden: list,
                 ):
        self.num_input = num_input
        self.num_hidden = num_hidden
        self.inputNeuron = [10, 20, 10, 5, 1]
        self.victory = [
		    [0, 4, 8],
		    [2, 4, 6],
		    [0, 1, 2],
		    [3, 4, 5],
		    [6, 7, 8],
		    [0, 3, 6],
		    [1, 4, 7],
		    [2, 5, 8],
        ]
        self.createPerceptron = []

        for i in (self.num_hidden):
            temp = []
            for j in range(i):
                temp.append()
            self.createPerceptron.append()

        self.init()

    def createNeuron(self, temp):
        for i in range(temp):
            pass


