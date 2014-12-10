__author__ = 'Kevin Carbone'

from neural.utilities import *
from neural.networks.network import Network
from neural.connections.output import OutputConnection


class LayeredNetwork(Network):
    """Base Class for Network"""

    def __init__(self, output_conn=None):
        Network.__init__(self)
        self.layers = []
        self.connections = []
        self.output_conn = output_conn

    def add_layer(self, layer):
        self.layers.append(layer)

    def add_connection(self, connection):
        self.connections.append(connection)
