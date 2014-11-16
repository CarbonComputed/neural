__author__ = 'Kevin Carbone'

from neural.neurons.neuron import Neuron


class LinearNeuron(Neuron):
    """Linear Neuron, dot(input,weights)"""

    def __init__(self):
        Neuron.__init__(self)

    def g(self, x):
        return x

    def g_prime(self, x):
        return x
