from unittest import TestCase

from p535.Solution import Codec


class TestCodec(TestCase):
    def test_encode(self):
        sol = Codec()
        hash = sol.encode('feafielsa:feafjeia;')
        print(hash, hash[19:])