
__author__ = 'Kevin Carbone'

import pickle
import datetime

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

    def save(self, filename=None):
        if not filename:
            filename = "dataset " + str(datetime.datetime.now())
        print self.data
        with open(filename,"wb") as handle:
            pickle.dump(self.data, handle, pickle.HIGHEST_PROTOCOL)