__author__ = 'Kevin Carbone'

from neural.connections.connection import Connection
from neural.utilities import *
from neural.neurons.neuron import NormalEdge, BiasEdge


class FullConnection(Connection):
    """Normal Neural Net behaviour the output of one layer feeds into the input of the next"""

    def __init__(self, layer1, layer2):
        Connection.__init__(self, layer1, layer2)
        for neuron in self.layer1:
            for neuron2 in self.layer2:
                NormalEdge(neuron, neuron2)
        for neuron2 in self.layer2:
            BiasEdge(self.layer1.bias, neuron2)

    def forward(self):
        for j, neuron2 in enumerate(self.layer2):
            neuron2.forward(self.layer1.bias.forward_edges[j])


    def backward(self):
        """
        Propagates the neurons error backwards
        :param alpha: Learning Rate
        """
        for neuron in self.layer1:
            neuron.backward()
        self.layer1.bias.backward()

    def update(self, alpha=0.01, momentum=0.9):
        for neuron in self.layer1:
            neuron.update(alpha, momentum)
        self.layer1.bias.update(alpha,momentum)