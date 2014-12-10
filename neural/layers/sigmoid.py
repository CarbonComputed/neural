__author__ = 'Kevin Carbone'

from neural.layers.layer import Layer
from neural.neurons.sigmoid import SigmoidNeuron


class SigmoidLayer(Layer):
    """Base class for different types of layers."""
    def __init__(self, num_neurons, bias=True):
        Layer.__init__(self, num_neurons, SigmoidNeuron, bias)
