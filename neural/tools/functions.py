import math


def sigmoid(z):
    """The sigmoid function."""
    return 1.0/(1.0+math.exp(-z))

def sigmoid_prime(z):
    """Derivative of the sigmoid function."""
    return sigmoid(z)*(1-sigmoid(z))