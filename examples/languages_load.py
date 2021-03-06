
from neural.connections.full import FullConnection
from neural.connections.output import OutputConnection
from neural.layers.sigmoid import SigmoidLayer
from neural.layers.linear import LinearLayer
from neural.networks.feedforward import FeedForwardNetwork
from neural.datasets.language import LanguageDataset
import neural.utilities
import sys
import os


class LanguageLoadNetwork():
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
        dataset = LanguageDataset(ndocuments=20)
        dataset.save()

        self.network.train(dataset, threshold=0.1, alpha = 0.1, momentum=0.0,max_epoch=10000)
        # print self.network


        test_data = LanguageDataset(ndocuments=12)
        # print(str(self.network))
        # for n in self.network.layers[-1]:
        #     print n
        self.network.test(test_data,debug=True)
        self.network.save()
        # print "TEST"
        # print self.network
        print neural.utilities.seed
        # for n in self.network.layers[-1]:
        #     print n

        # print(self.output)

    def test_test(self):
        """Test the networks training"""

        self.network = self.network.load(os.path.join(os.path.dirname(__file__), '..', 'neural/data/networks/default_sent.network'))

        text = " "
        while text != "":
            text = raw_input("Enter a string to test or hit return to end the program:")
            if text == "":
                break
            test_data = LanguageDataset(ndocuments=0)
            test_data.add_text(text)
            self.network.test(test_data)
            languages = ["English", "Italian", "Dutch"]
            for i, n in enumerate(self.network.layers[-1]):
                print n.activate, "sure it's", languages[i]


if __name__ == "__main__":
    l = LanguageLoadNetwork()
    l.setUp()
    if len(sys.argv) > 1 and sys.argv[1] == "train":
        l.test_train()
    else:
        l.test_test()