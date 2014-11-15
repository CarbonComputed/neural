
import unittest
from neural.layers.sigmoid import SigmoidLayer



class SigmoidLayerTest(unittest.TestCase):
    """Unit tests for SigmoidLayer"""

    def setUp(self):
        self.sigmoid_layer = SigmoidLayer(5)

    def test_iterate(self):
        """Test Iteration"""
        for neuron in self.sigmoid_layer:
            print neuron

    def test_getneuron(self):
        """Testing getting a neuron"""
        print self.sigmoid_layer[2]

    def test_backward(self):
        """Test the connections backward connection"""
        pass     

if __name__ == "__main__":
    unittest.main()