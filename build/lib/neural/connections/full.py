__author__ = 'Kevin Carbone'

from neural.connections.connection import Connection
from neural.utilities import *

class FullConnection(Connection):
	"""Normal Neural Net behaviour the output of one layer feeds into the input of the next"""
	def __init__(self, layer1, layer2):
		super(self.__class__, self).__init__(layer1,layer2)

	def forward(self):
		pass

	def backward(self):
		pass