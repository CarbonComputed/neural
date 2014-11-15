__author__ = 'Kevin Carbone'

class Network(object):
	"""Base Class for Network"""
	def __init__(self):
		super(self.__class__, self).__init__()
		self.layers = []
		self.connections = []

	def add_layer(self,layer):
		pass

	def add_connection(self, connection):
		pass

	def train(self,data,expected):
		pass

	def test(self,data):
		pass
		