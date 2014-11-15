
__author__ = 'Kevin Carbone'

from neural.utilities import *


class Neuron(object):
    """Neuron Base Class"""
    def __init__(self):
        self.input = []
        self.weights = []
        self.output = []
        self.dot = 0
        self.activate = 0
        self.delta = 0
        self._out = 0
        self._in = 0

    def feed(self, input, bias):
        self.bias = bias
        self.input.append(input)

    def clear(self):
        self.input = []
        self.output = []

    def activation(self):
        result = 0
        for i,j in self.input:
            result += (i * j)
        self._in = result + self.bias
        self.activate = self.g(self._in + self.bias)
        self.input = []
        return self.activate

    def forward(self):
        self.output = []
        a = self.activate
        if len(self.weights) <= 0:
            #Most likely an output neuron
            self.weights = [1]
        for w in self.weights:
            self.output.append([w, a])

        return self.output

    def backward(self, func, deltas):
        r = dot(self.weights,deltas)
        self.delta = func(self._in) * r
        

    def g(self, x):
        abstractMethod()

    def g_prime(self, x):
        abstractMethod()

    @property
    def __repr__(self):
        return str(self.__class__.__name__) + "\nactivate " + str(self.activate)+str(self.input) + "\noutput" + str(self.output) + " \nweights " + str(self.weights) + "\n"

    def __str__(self):
        return str(self.__class__.__name__) + "\nactivate " + str(self.activate)+str(self.input) + "\noutput" + str(self.output) + " \nweights " + str(self.weights) + "\n"

class Edge:
   def __init__(self, source, target):
      self.weight = random.uniform(-1,1)
      self.source = source
      self.target = target
      source.outgoingEdges.append(self)
      target.incomingEdges.append(self)