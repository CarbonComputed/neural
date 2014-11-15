__author__ = 'Kevin Carbone'

from neural.utilities import *
from neural.neurons.neuron import Neuron
from neural.tools.functions import *

class SigmoidNeuron(Neuron):
    """Uses the sigmoid activation function"""
    def __init__(self):
        Neuron.__init__(self)


    def g(self,x):
        return sigmoid(x)

    def g_prime(self,x):
        return sigmoid_prime(x)