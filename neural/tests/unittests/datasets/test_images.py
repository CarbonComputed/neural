__author__ = 'kmcarbone16'


import unittest
from neural.connections.full import FullConnection
from neural.connections.output import OutputConnection

from neural.layers.sigmoid import SigmoidLayer
from neural.layers.linear import LinearLayer
from neural.networks.autoencoders.denoising import DenoisingAutoencoder
from neural.datasets.dataset import Dataset
from neural.datasets.images import ImagesDataset
import Image
import neural.utilities


class ImagesAutoencoderTest(unittest.TestCase):
    """Unit tests for a FeedForwardNetwork"""

    def setUp(self):
        size = (50,50)
        self.dataset = ImagesDataset(size)
        self.input = LinearLayer(size[0]*size[1], True)
        self.hidden = SigmoidLayer(50, True)
        self.output = SigmoidLayer(size[0]*size[1],False)
        self.output2 = LinearLayer(size[0]*size[1],False)
        self.in_hidden = FullConnection(self.input,self.hidden)
        self.hidden_out = FullConnection(self.hidden,self.output)
        self.out_out2 = OutputConnection(self.output,self.output2)
        self.network = DenoisingAutoencoder(self.out_out2, self.dataset, noise=0.30)
        self.network.add_layer(self.input)
        self.network.add_layer(self.hidden)
        self.network.add_layer(self.output)
        self.network.add_layer(self.output2)
        self.network.add_connection(self.in_hidden)
        self.network.add_connection(self.hidden_out)



    def test_train(self):
        """Test the networks training"""
        self.network.train(threshold=0.1, alpha = 0.7, momentum=0.0,max_epoch=30)
        features = self.network.get_features()
        import math
        print int(math.sqrt(len(features)))
        im = Image.new('L', (10000,10000))
        row = 0
        col = 0
        for feature in features:
            print row
            ndataset = Dataset()
            ndataset.add(feature, feature)
            self.network.dataset = ndataset
            self.network.train(threshold=0.1, alpha = 0.1, momentum=0.0,max_epoch=0)
            n = 0
            for i in range(row, row+self.dataset.size[0]):    # for every pixel:
                for j in range(col,col +self.dataset.size[1]):
                    im.putpixel((j, i), self.network.layers[-1][n].activate*255)
                    n += 1
            col += self.dataset.size[0]
            if col >= self.dataset.size[0] * self.dataset.size[1]:
                col = 0
                row += self.dataset.size[1]
        im.show()





if __name__ == "__main__":
    unittest.main()