
import unittest
from neural.connections.full import FullConnection
from neural.connections.output import OutputConnection
from neural.layers.sigmoid import SigmoidLayer
from neural.layers.linear import LinearLayer
from neural.networks.feedforward import FeedForwardNetwork
from neural.datasets.dataset import Dataset
from neural.datasets.xor import XORDataset
import neural.utilities


class FeedForwardNetworkTest(unittest.TestCase):
    """Unit tests for a FeedForwardNetwork"""

    def setUp(self):
        self.input = LinearLayer(2,True)
        self.hidden = SigmoidLayer(50,True)
        self.output = SigmoidLayer(1,False)
        self.output2 = LinearLayer(1,False)
        self.in_hidden = FullConnection(self.input,self.hidden)
        self.hidden_out = FullConnection(self.hidden,self.output)
        self.out_out2 = OutputConnection(self.output,self.output2)
        self.network = FeedForwardNetwork(self.out_out2)
        self.network.add_layer(self.input)
        self.network.add_layer(self.hidden)
        self.network.add_layer(self.output)
        self.network.add_layer(self.output2)
        self.network.add_connection(self.in_hidden)
        self.network.add_connection(self.hidden_out)



    def test_train(self):
        """Test the networks training"""
        dataset = XORDataset()
        self.network.train(dataset, alpha = 0.7, momentum=0)
        # print self.network
        test_data = Dataset()
        test_data.add([1,0],[0])
        # print(str(self.network))
        # for n in self.network.layers[-1]:
        #     print n
        self.network.test(test_data)
        # print "TEST"
        # print self.network
        print neural.utilities.seed
        for n in self.network.layers[-1]:
            print n
        self.network.save()

        # print(self.output)

if __name__ == "__main__":
    unittest.main()