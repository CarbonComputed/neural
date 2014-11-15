__author__ = 'Kevin Carbone'

from neural.networks.network import Network
from neural.tools.functions import *
import random


class FeedForwardNetwork(Network):
    """Base Class for Network"""

    def __init__(self):
        Network.__init__(self)


    def train(self, dataset, alpha=0.01):
        for k in range(5000):
            # print '1',dataset.data

            # random.shuffle(dataset.data)
            # print '2',dataset.data
            for example in dataset:
                # bias = self.layers[0][0]
                # for neuron in self.layers[0]:
                # for n, i in enumerate(example[0]):
                #     self.layers[0][n].feed([1, i], 0)
                #     self.layers[0][n].activation()
                # for conn in self.connections:
                #     conn.forward()
                for n, i in enumerate(example[0]):
                    self.layers[0][n].activate = i
                for i in range(len(self.layers) - 1):
                    for j in range(len(self.layers[i+1])):
                        self.layers[i+1][j]._in = 0
                    for j in range(len(self.layers[i])):
                        for x in range(len(self.layers[i][j].weights)):
                            self.layers[i+1][x]._in += self.layers[i][j].activate * self.layers[i][j].weights[x]
                            self.layers[i+1][x].bias = self.layers[i].bias.weights[x]
                    for j in range(len(self.layers[i+1])):
                        self.layers[i+1][j].activate = self.layers[i+1][j].g(self.layers[i+1][j]._in + self.layers[i+1][j].bias)


                for neuron in self.layers[-1]:
                    neuron.delta = neuron.g_prime(neuron._in) * (example[1] - neuron.activate)
                for i in range(len(self.layers) - 2,-1,-1):
                    for j in range(len(self.layers[i])):
                        sum = 0
                        for x in range(len(self.layers[i][j].weights)):
                            sum += self.layers[i+1][x].delta * self.layers[i][j].weights[x]
                        self.layers[i][j].delta = self.layers[i][j].g_prime(self.layers[i][j]._in) * sum
                for i in range(len(self.layers) - 1):
                    for j in range(len(self.layers[i])):
                        for x in range(len(self.layers[i][j].weights)):
                            self.layers[i][j].weights[x] += alpha * self.layers[i][j].activate * self.layers[i+1][x].delta
                # for i, neuron in enumerate(self.layers[-1]):
                #     # print (example[1] - neuron.activate),neuron.activate,neuron.dot
                #     neuron.forward()
                #     assert isinstance(neuron, object)
                #     neuron.delta = neuron.g_prime(neuron._in) * (example[1]- neuron.activate)
                # # print "Delta",neuron.delta
                # for conn in reversed(self.connections):
                #     conn.backward(alpha)

    def test(self, dataset):
        for example in dataset:
            # for k, i in enumerate(example[0]):
            #     self.layers[0][k].feed([1, i], 0)
            #     self.layers[0][k].activation()
            for n, i in enumerate(example[0]):
                self.layers[0][n].activate = i
            for i in range(len(self.layers) - 1):
                for j in range(len(self.layers[i+1])):
                    self.layers[i+1][j]._in = 0
                for j in range(len(self.layers[i])):
                    for x in range(len(self.layers[i][j].weights)):
                        self.layers[i+1][x]._in += self.layers[i][j].activate * self.layers[i][j].weights[x]
                        self.layers[i+1][x].bias = self.layers[i].bias.weights[x]
                for j in range(len(self.layers[i+1])):
                    self.layers[i+1][j].activate= self.layers[i+1][j].g(self.layers[i+1][j]._in + self.layers[i+1][j].bias)

            # for conn in self.connections:
            #     conn.forward()

        