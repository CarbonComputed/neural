__author__ = 'Kevin Carbone'

from neural.layers.layer import Layer
from neural.neurons.linear import LinearNeuron


class LinearLayer(Layer):
    """Base class for different types of layers."""
    def __init__(self, num_neurons,bias=True):
        Layer.__init__(self,num_neurons, LinearNeuron, bias)

