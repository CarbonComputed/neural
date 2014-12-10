__author__ = 'Kevin Carbone'

from neural.datasets.dataset import Dataset
import Image
import os

class ImagesDataset(Dataset):
    """Default dataset for XOR"""
    def __init__(self, size):
        Dataset.__init__(self)
        self.size = size
        fname = os.path.join(os.path.dirname(__file__), '..', 'data/images/', 'test2.jpg')
        fname2 = os.path.join(os.path.dirname(__file__), '..', 'data/images/', 'test.jpg')

        img = Image.open(fname).convert('L')
        img = img.resize(size,Image.ANTIALIAS)

        img.show()
        pixels = list(img.getdata())
        width, height = img.size
        print len(pixels)
        norm_pixels = []
        for p in pixels:
            norm_pixels.append(round(float(p)/255.0,3))
        self.add(norm_pixels,[0])

        img2 = Image.open(fname2).convert('L')
        img2 = img2.resize(size,Image.ANTIALIAS)
        pixels2 = list(img2.getdata())
        width, height = img2.size
        print len(pixels2)
        norm_pixels2 = []
        for p in pixels2:
            norm_pixels2.append(round(float(p)/255.0,3))
        self.add(norm_pixels2,[0])

