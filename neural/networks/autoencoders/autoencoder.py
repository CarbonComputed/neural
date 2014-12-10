__author__ = 'kmcarbone16'

from neural.networks.feedforward import FeedForwardNetwork
from neural.utilities import *

class Autoencoder(FeedForwardNetwork):

    def __init__(self, output_conn, dataset):
        FeedForwardNetwork.__init__(self, output_conn)
        self.dataset = dataset
        self._init_dataset()

    def _init_dataset(self):
        for data in self.dataset:
            data[1] = data[0]

    def train(self, threshold=0.1, alpha=0.01, momentum=0.9, max_epoch=5000):
        abstractMethod()



