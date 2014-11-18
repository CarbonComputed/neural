__author__ = 'Kevin Carbone'

from neural.networks.layered import LayeredNetwork
from neural.tools.functions import *
import random


class FeedForwardNetwork(LayeredNetwork):
    """Base Class for Network"""

    def __init__(self, output_conn):
        LayeredNetwork.__init__(self, output_conn)


    def train(self, dataset, threshold=0.1, alpha=0.01, momentum=0.9, max_epoch=5000):
        epoch = 0
        error_sum = 0
        error = 1
        n = 0
        while error > threshold:
            random.shuffle(dataset.data)
            for example in dataset:
                for k, i in enumerate(example[0]):
                    self.layers[0][k].activate = i
                    self.layers[0][k].input = i
                for conn in self.connections:
                    conn.forward()
                self.output_conn.forward()
                errors = self.output_conn.backward(example[1])
                error_sum += sum(errors)
                n += len(errors)
                error = error_sum/n
                print epoch,error
                for conn in reversed(self.connections):
                    conn.backward()
                for conn in self.connections:
                    conn.update(alpha, momentum)
            epoch += 1
            if epoch > max_epoch:
                return

    def test(self, dataset):
        random.shuffle(dataset.data)
        for example in dataset:
            for k, i in enumerate(example[0]):
                self.layers[0][k].activate = i
                self.layers[0][k].input = i
            for conn in self.connections:
                conn.forward()
            self.output_conn.forward()
            print example
            for n in self.layers[-1]:
                print n

