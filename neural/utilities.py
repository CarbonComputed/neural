__author__ = 'Kevin Carbone'

import random
import sys

seed = random.randint(0, sys.maxint)
random.seed(seed)
# random.seed(1586760772949995824)

def abstractMethod():
    """ This should be called when an abstract method is called that should have been
    implemented by a subclass. It should not be called in situations where no implementation
    (i.e. a 'pass' behavior) is acceptable. """
    raise NotImplementedError('Method not implemented! AbstractMethod.')

def ones(n):
	return [1.0 for x in range(n)]

def zeros(n):
	return [0.0 for x in range(n)]

def one():
    return 1.0

def zero():
    return 0.0

def random_weight():
    return random.uniform(-1,1)

def squared_error(expected, actual):
    ea = expected - actual
    return ea * ea

def normalize(input):
    old_min = min(input)
    old_range = max(input) - old_min
    new_min = 0.0
    new_range = 1.0
    return [float((n - old_min) / old_range * new_range + new_min) for n in input]

def dot(a,b):
    result = 0
    for i,j in zip(a,b):
        result += i*j
    return result