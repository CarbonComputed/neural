__author__ = 'Kevin Carbone'

from neural.connections.connection import Connection
from neural.utilities import *
from neural.tools.functions import *


class FullConnection(Connection):
    """Normal Neural Net behaviour the output of one layer feeds into the input of the next"""

    def __init__(self, layer1, layer2, weight_f=random_weight):
        Connection.__init__(self, layer1, layer2)
        for neuron in self.layer1:
            for neuron2 in self.layer2:
                neuron.weights.append(weight_f())
        for neuron2 in self.layer2:
            self.layer1.bias.weights.append(weight_f())

    def forward(self):
        # for neuron2 in self.layer2:
        # neuron2.clear()
        bias = self.layer1.bias
        for neuron in self.layer1:
            edges = neuron.forward()
            for i, neuron2 in enumerate(self.layer2):
                neuron2.feed(edges[i], bias.weights[i] * bias.val)
        for neuron2 in self.layer2:
            neuron2.activation()


    def backward(self, alpha=0.01):
        """
        Propagates the neurons error backwards
        :param alpha: Learning Rate
        """
        deltas = []
        for neuron2 in self.layer2:
            deltas.append(neuron2.delta)
        for neuron in self.layer1:
                neuron.backward(neuron2.g_prime, deltas)
        for neuron in self.layer1:
            for j in range(len(neuron.weights)):
                neuron.weights[j] += (alpha * neuron.activate * deltas[j])
        for j in range(len(deltas)):
            self.layer1.bias.weights[j] += deltas[j]
        pass