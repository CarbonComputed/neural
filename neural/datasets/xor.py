
__author__ = 'Kevin Carbone'

from neural.datasets.dataset import Dataset


class XORDataset(Dataset):
    """Default dataset for XOR"""
    def __init__(self):
        Dataset.__init__(self)
        self.add([0, 0], [1])
        self.add([0, 1], [0])
        self.add([1, 0], [0])
        self.add([1, 1], [1])