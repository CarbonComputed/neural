
__author__ = 'Kevin Carbone'

from neural.utilities import *
from neural.datasets.dataset import Dataset

class XORDataset(Dataset):
    """docstring for Dataset"""
    def __init__(self):
        Dataset.__init__(self)
        self.addData([0,0],1)
        self.addData([0,1],0)
        self.addData([1,0],0)
        self.addData([1,1],1)