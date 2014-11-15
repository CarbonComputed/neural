
__author__ = 'Kevin Carbone'

from neural.utilities import *

class Connection(object):
	"""Base class for connections. Link different layers."""
	def __init__(self, layer1, layer2, weight_f=random_weight):
		self.layer1 = layer1
		self.layer2 = layer2
		self.weight_f = weight_f

	def forward(self):
		abstractMethod()

	def backward(self):
		abstractMethod()
		