__author__ = 'Kevin Carbone'

def abstractMethod():
    """ This should be called when an abstract method is called that should have been
    implemented by a subclass. It should not be called in situations where no implementation
    (i.e. a 'pass' behavior) is acceptable. """
    raise NotImplementedError('Method not implemented! AbstractMethod.')

def ones(n):
	return [1.0 for x in range(n)]

def zeros(n):
	return [0.0 for x in range(n)]