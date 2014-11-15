__author__ = 'Kevin Carbone'

from neural.utilities import *


class Layer(object):
    """Base class for different types of layers."""
    def __init__(self, num_neurons, weight_f=zeros):
        super(self.__class__, self).__init__()
        self.num_neurons = num_neurons
        self.input = weight_f(num_neurons)
        self.output = zeros(num_neurons)
        self.in_error = zeros(num_neurons)
        self.out_error = zeros(num_neurons)

    def forward(self):
        abstractMethod()

    def backward(self):
        abstractMethod()
