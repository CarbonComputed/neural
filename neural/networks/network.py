__author__ = 'Kevin Carbone'

from neural.utilities import *


class Network(object):
	"""Base Class for Network"""
	def __init__(self):
		self.layers = []
		self.connections = []
		self.inputLayer = None
		self.outputLayer = None
		self.hiddenLayer = None

	def add_layer(self,layer):
		self.layers.append(layer)

	def add_connection(self, connection):
		self.connections.append(connection)

	def train(self,data,expected):
		abstractMethod()

	def test(self,data):
		pass
	
	def __str__(self):
		string = "Network:\n"
		for l in self.layers:
			string += str(l)
		return string