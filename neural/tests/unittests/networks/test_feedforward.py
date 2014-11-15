
import unittest
from neural.connections.full import FullConnection
from neural.layers.sigmoid import SigmoidLayer
from neural.layers.linear import LinearLayer
from neural.networks.feedforward import FeedForwardNetwork
from neural.datasets.dataset import Dataset
from neural.datasets.xor import XORDataset


class FeedForwardNetworkTest(unittest.TestCase):
    """Unit tests for a FeedForwardNetwork"""

    def setUp(self):
        self.input = LinearLayer(2,True)
        self.hidden = SigmoidLayer(5,False)
        self.output = SigmoidLayer(1,False)
        self.in_hidden = FullConnection(self.input,self.hidden)
        self.hidden_out = FullConnection(self.hidden,self.output)
        self.network = FeedForwardNetwork()
        self.network.add_layer(self.input)
        self.network.add_layer(self.hidden)
        self.network.add_layer(self.output)
        self.network.add_connection(self.in_hidden)
        self.network.add_connection(self.hidden_out)


    def test_train(self):
        """Test the networks training"""
        dataset = XORDataset()
        self.network.train(dataset,alpha = 0.5)
        # print self.network
        test_data = Dataset()
        test_data.addData([1,0],0)
        # print(str(self.network))
        # for n in self.network.layers[-1]:
        #     print n
        self.network.test(test_data)
        # print "TEST"
        # print self.network
        for n in self.network.layers[-1]:
            print n

        # print(self.output)

if __name__ == "__main__":
    unittest.main()