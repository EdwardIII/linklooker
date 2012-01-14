from linklooker import link
import unittest

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.link = link.link('http://google.com')

    def test_is_success(self):
        self.assertEqual(self.link.is_success(), 1)

if __name__ == '__main__':
    unittest.main()
