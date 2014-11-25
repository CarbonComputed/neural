
__author__ = 'Kevin Carbone'

from neural.utilities import *


class Neuron(object):
    """Neuron Base Class"""
    def __init__(self):
        self.forward_edges = []
        self.backward_edges = []
        self.input = 0
        self.activate = 0
        self.delta = 0
        self.prev_delta = 0

    def forward(self, bias_edge=None):
        self.input = 0
        bias_edge_w = 0
        bias_edge_a = 0
        if bias_edge:
            bias_edge_w = bias_edge.weight
            bias_edge_a = bias_edge.source.activate

        for edge in self.backward_edges:
            self.input += (edge.weight * edge.source.activate)
        self.input += (bias_edge_w * bias_edge_a)
        self.activate = self.g(self.input)
        return self.activate

    def backward(self):
        r = 0
        for edge in self.forward_edges:
            r += (edge.target.delta * edge.weight)
        self.prev_delta = self.delta
        self.delta = self.g_prime(self.input) * r

    def update(self, alpha, momentum):
        for edge in self.forward_edges:
            edge.weight += (alpha * self.activate * edge.target.delta) + (self.prev_delta * momentum)

    def g(self, x):
        abstractMethod()

    def g_prime(self, x):
        abstractMethod()

    @property
    def __repr__(self):
        return str(self.__class__.__name__) + "\nactivate " + str(self.activate) + "\noutput" + str("") + " \nweights " + str(self.forward_edges) + "\n"

    def __str__(self):
        return str(self.__class__.__name__) + "\nactivate " + str(self.activate) + "\noutput" + str("") + " \nweights " + str(self.forward_edges) + "\n"


class Edge:
    def __init__(self, source, target, weight_f=random_weight):
        self.weight = weight_f()
        self.source = source
        self.target = target

    def __str__(self):
        return str(self.weight)


class NormalEdge(Edge):
    def __init__(self, source, target, weight_f=random_weight):
        Edge.__init__(self,source,target,weight_f)
        source.forward_edges.append(self)
        target.backward_edges.append(self)


class BiasEdge(Edge):
    def __init__(self, source, target, weight_f=random_weight):
        Edge.__init__(self,source,target,weight_f)
        source.forward_edges.append(self)