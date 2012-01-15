import unittest
from linklooker import linklooker

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.goodLink = linklooker.Link('http://google.com')
        self.badLink = linklooker.Link('http://obviously-wouldnt-exist-in-reality.com')

    def test_is_success(self):
        self.assertEqual(self.goodLink.is_success(), True)
        self.assertEqual(self.badLink.is_success(), False)

if __name__ == '__main__':
    unittest.main()
