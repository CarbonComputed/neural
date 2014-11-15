__author__ = 'Kevin Carbone'

from neural.utilities import *
from neural.neurons.bias import BiasNeuron


class Layer(object):
    """Base class for different types of layers."""
    def __init__(self, num_neurons, bias=True):
        self.num_neurons = num_neurons
        self.neurons = []
        self.bias = BiasNeuron(int(bias))

    def __iter__(self):
        for neuron in self.neurons:
                yield neuron

    def __getitem__(self, key):
        return self.neurons[key]

    def __setitem__(self, key, value):
        self.neurons[key] = value

    def __len__(self):
        return len(self.neurons)

    def __repr__(self):
        return str(self.neurons)


    def __str__(self):
        return str(self.neurons)
