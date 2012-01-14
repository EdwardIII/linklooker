import unittest
from Linklooker import Linklooker

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.goodLink = Linklooker.Link('http://google.com')
        self.badLink = Linklooker.Link('http://obviously-wouldnt-exist-in-reality.com')

    def test_is_success(self):
        self.assertEqual(self.goodLink.is_success(), True)
        self.assertEqual(self.badLink.is_success(), False)

if __name__ == '__main__':
    unittest.main()
