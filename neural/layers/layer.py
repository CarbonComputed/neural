__author__ = 'Kevin Carbone'

from neural.neurons.bias import BiasNeuron


class Layer(object):
    """Base class for different types of layers."""
    def __init__(self, num_neurons, cls, bias=True):
        self.num_neurons = num_neurons
        self.neurons = []
        self.bias = BiasNeuron(int(bias))
        self.neurons.extend([cls() for x in range(num_neurons)])

    def __getitem__(self, key):
        return self.neurons[key]

    def __setitem__(self, key, value):
        self.neurons[key] = value

    def __iter__(self):
        for neuron in self.neurons:
                yield neuron

    @property
    def __len__(self):
        return len(self.neurons)

    @property
    def __repr__(self):
        return str(self.neurons)

    @property
    def __str__(self):
        return str(self.neurons)
