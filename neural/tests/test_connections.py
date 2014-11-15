import unittest
from neural.connections.full import FullConnection

class FullConnectionTest(unittest.TestCase):
    """Unit tests for Connection"""

    def test_forward(self):
        """Test the connections forward connection"""
        c = FullConnection(input1,input2)

    def test_backward(self):
        """Test the connections backward connection"""      

if __name__ == "__main__":
    unittest.main()