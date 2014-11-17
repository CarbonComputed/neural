__author__ = 'Kevin Carbone'

from neural.neurons.neuron import Neuron


class BiasNeuron(Neuron):
    """Bias Neuron, dot(input,weights)"""
    def __init__(self, activate=1):
        Neuron.__init__(self)
        self.input = activate
        self.activate = activate

    def forward(self, bias_edge=None):
        self.activate = 1
        self.input = 1
        return self.activate

    def update(self, alpha, momentum):
        for edge in self.forwardEdges:
            edge.weight += (edge.target.delta * alpha)

    def backward(self):
        r = 0
        for edge in self.forwardEdges:
            r += (edge.target.delta * (self.activate * edge.weight))
        self.prev_delta = self.delta
        self.delta = 1 * r

    def g(self, x):
        return self.activate

    def g_prime(self, x):
        return self.activate