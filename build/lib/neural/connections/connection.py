
__author__ = 'Kevin Carbone'

from neural.utilities import *

class Connection(object):
	"""Base class for connections. Link different layers."""
	def __init__(self, layer1, layer2):
		super(self.__class__, self).__init__()
		self.layer1 = layer1
		self.layer2 = layer2

	def forward(self):
		abstractMethod()

	def backward(self):
		abstractMethod()
		