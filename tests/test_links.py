import unittest
from linklooker import linklooker

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.links = linklooker.Links(['http://google.com', 'http://not-a-real-domain-name.com'])

    def test_status_table(self):
        expected = { 'http://google.com': 'Good', 'http://not-a-real-domain-name.com': 'Good' };
        self.assertEqual(self.links.status_table(), expected)

if __name__ == '__main__':
    unittest.main()
