from unittest import TestCase

from p297.Solution import Codec


class N:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class TestCodec(TestCase):
    def test_serialize(self):
        codec = Codec()

        self.assertEqual("^1*2^3*4>5*6",
                         codec.serialize(N(1, N(2), N(3, N(4), N(5, None, N(6))))))
        self.assertEqual("", codec.serialize(None))

        self.assertEqual("^1*-2^3*4>5*6", codec.serialize(codec.deserialize("^1*-2^3*4>5*6")))
