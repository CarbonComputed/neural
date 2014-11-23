__author__ = 'Kevin Carbone'

from neural.utilities import *
import os
import datetime
import pickle


class Network(object):
    """Base Class for Network"""

    def __init__(self):
        object.__init__(self)

    def train(self, data, expected):
        abstractMethod()

    def test(self, data):
        pass

    def __str__(self):
        string = "Network:\n"
        for l in self.layers:
            string += str(l)
        return string

    def save(self, filename=None):
        if not filename:
            filename = "network " + str(datetime.datetime.now())
        with open(filename,"wb") as handle:
            pickle.dump(self, handle)

    def load(self, filename=None):
        if not filename:
            filename = os.path.join(os.path.dirname(__file__), '..', 'data/networks/default_sent.network')
        network = None
        with open(filename, 'rb') as handle:
          network = pickle.load(handle)
        # self = network
        return network