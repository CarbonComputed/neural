
import unittest
from neural.connections.full import FullConnection
from neural.layers.linear import LinearLayer
from neural.layers.sigmoid import SigmoidLayer



class FullConnectionTest(unittest.TestCase):
    """Unit tests for Connection"""

    def setUp(self):
        self.layer1 = LinearLayer(5)
        self.layer2 = SigmoidLayer(5)
        self.conn = FullConnection(self.layer1,self.layer2)

    def test_forward(self):
        """Test the connections forward connection"""
        self.conn.forward()

    def test_backward(self):
        """Test the connections backward connection"""
        pass     

if __name__ == "__main__":
    unittest.main()