__author__ = 'Kevin Carbone'

from neural.utilities import *
from neural.neurons.neuron import Neuron
from neural.tools.functions import *

class BiasNeuron(Neuron):
    """Bias Neuron, dot(input,weights)"""
    def __init__(self,val=1):
        Neuron.__init__(self)
        self.val = 1

    def g(self,x):
        return self.val

    def g_prime(self,x):
        return self.val