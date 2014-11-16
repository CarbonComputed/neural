__author__ = 'Kevin Carbone'

from neural.networks.layered import LayeredNetwork
from neural.tools.functions import *
import random


class FeedForwardNetwork(LayeredNetwork):
    """Base Class for Network"""

    def __init__(self, output_conn):
        LayeredNetwork.__init__(self, output_conn)


    def train(self, dataset, alpha=0.01, momentum=0.4):
        for k in range(5000):
            # random.shuffle(dataset.data)
            for example in dataset:
                for k, i in enumerate(example[0]):
                    self.layers[0][k].activate = i
                    self.layers[0][k].input = i
                for conn in self.connections:
                    conn.forward()
                self.output_conn.forward()
                self.output_conn.backward(example[1])
                for conn in reversed(self.connections):
                    conn.backward()
                for conn in self.connections:
                    conn.update(alpha, momentum)

    def test(self, dataset):
        for example in dataset:
            for k, i in enumerate(example[0]):
                self.layers[0][k].activate = i
                self.layers[0][k].input = i
            for conn in self.connections:
                conn.forward()
            self.output_conn.forward()

