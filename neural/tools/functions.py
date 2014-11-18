import math

sign = lambda x: x and (1, -1)[x<0]

def sigmoid(z):
    """The sigmoid function."""
    z = sign(z)*min(abs(z),500)
    return 1.0/(1.0+math.exp(-z))

def sigmoid_prime(z):
    """Derivative of the sigmoid function."""
    return sigmoid(z)*(1-sigmoid(z))