
import unittest
from neural.connections.full import FullConnection
from neural.connections.output import OutputConnection

from neural.layers.sigmoid import SigmoidLayer
from neural.layers.linear import LinearLayer
from neural.networks.feedforward import FeedForwardNetwork
from neural.datasets.dataset import Dataset
from neural.datasets.language import LanguageDataset

import neural.utilities


class FeedForwardNetworkTest(unittest.TestCase):
    """Unit tests for a FeedForwardNetwork"""

    def setUp(self):
        self.input = LinearLayer(52,True)
        self.hidden = SigmoidLayer(9,True)
        self.output = SigmoidLayer(3,False)
        self.output2 = LinearLayer(3,False)
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
        dataset = LanguageDataset()
        dataset.save()

        self.network.train(dataset, threshold=0.1, alpha = 0.06, momentum=0.9,max_epoch=500)
        # print self.network


        test_data = LanguageDataset()
        # print(str(self.network))
        # for n in self.network.layers[-1]:
        #     print n
        self.network.test(test_data)
        self.network.save()
        # print "TEST"
        # print self.network
        print neural.utilities.seed
        # for n in self.network.layers[-1]:
        #     print n

        # print(self.output)

if __name__ == "__main__":
    unittest.main()