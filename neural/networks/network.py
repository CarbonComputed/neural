__author__ = 'Kevin Carbone'

from neural.utilities import *


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