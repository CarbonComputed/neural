__author__ = 'Kevin Carbone'

from neural.connections.connection import Connection
from neural.utilities import *
from neural.neurons.neuron import NormalEdge


class OutputConnection(Connection):
    """Normal Neural Net behaviour the output of one layer feeds into the input of the next"""

    def __init__(self, layer1, layer2):
        Connection.__init__(self, layer1, layer2)
        for i, neuron in enumerate(self.layer1):
            NormalEdge(neuron, self.layer2[i], one)

    def forward(self):
        for j, neuron2 in enumerate(self.layer2):
            neuron2.forward()

    def backward(self, outputs):
        """
        Propagates the neurons error backwards
        """
        diffs = []
        for o, neuron in enumerate(self.layer1):
            neuron.delta = neuron.g_prime(neuron.input) * (outputs[o] - neuron.activate)
            diffs.append(squared_error(outputs[o], neuron.activate))
        return diffs


