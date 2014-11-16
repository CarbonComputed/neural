__author__ = 'Kevin Carbone'

from neural.neurons.neuron import Neuron


class BiasNeuron(Neuron):
    """Bias Neuron, dot(input,weights)"""
    def __init__(self, activate=1):
        Neuron.__init__(self)
        self.input = activate
        self.activate = activate

    def update(self, alpha, momentum):
        for edge in self.forwardEdges:
            edge.weight += (self.delta * alpha * 10)

    def backward(self):
        r = 0
        for edge in self.forwardEdges:
            r += (edge.target.delta * (self.activate * edge.weight))
        self.prev_delta = self.delta
        self.delta = self.g_prime(self.input) * r

    def g(self, x):
        return self.activate

    def g_prime(self, x):
        return self.activate