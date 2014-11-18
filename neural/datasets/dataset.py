
__author__ = 'Kevin Carbone'

from neural.utilities import *

class Dataset(object):
    """docstring for Dataset"""
    def __init__(self):
        self.data = []
    
    def add(self,input,out,data=None):
        self.data.append([input,out,data])

    def __iter__(self):
        for data in self.data:
                yield data

    def __getitem__(self, key):
        return self.data[key]

    def __len__(self):
        return len(self.neurons)
