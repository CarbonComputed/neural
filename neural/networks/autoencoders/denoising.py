__author__ = 'kmcarbone16'

from neural.networks.autoencoders.autoencoder import Autoencoder
import random
import math

class DenoisingAutoencoder(Autoencoder):

    def __init__(self, output_conn, dataset, noise=0.25):
        Autoencoder.__init__(self, output_conn, dataset)
        self.noise = noise


    def train(self, threshold=0.1, alpha=0.01, momentum=0.9, max_epoch=5000):
        epoch = 0
        error_sum = 0
        error = 1
        n = 0
        dataset = self.dataset
        while error > threshold:
            random.shuffle(dataset.data)
            for example in dataset:
                for k, i in enumerate(example[0]):
                    if random.random() > self.noise:
                        self.layers[0][k].activate = i
                        self.layers[0][k].input = i
                    else:
                        self.layers[0][k].activate = i
                        self.layers[0][k].input = i
                for conn in self.connections:
                    conn.forward()
                self.output_conn.forward()
                errors = self.output_conn.backward(example[1])
                error_sum += sum(errors)
                n += len(errors)
                error = error_sum/n
                print epoch, error
                for conn in reversed(self.connections):
                    conn.backward()
                for conn in self.connections:
                    conn.update(alpha, momentum)
            epoch += 1
            if epoch > max_epoch:
                return

    def get_features(self):
        inputs = []
        for j, neuron2 in enumerate(self.layers[1]):
            sum = 0
            for edge in neuron2.backward_edges:
                sum += (edge.weight*edge.weight)
            sum = float(math.sqrt(sum))
            input = []
            for edge in neuron2.backward_edges:
                input.append(edge.weight/sum)
            inputs.append(input)
        return inputs



