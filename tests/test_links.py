import unittest
from linklooker.linklooker import Links

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.links = Links(['http://google.com', 'http://not-a-real-domain-name.com'])

    def test_status_table(self):
        expected = { 'http://google.com': True, 'http://not-a-real-domain-name.com': False }
        self.assertEqual(sorted(self.links.status_table()), sorted(expected))

if __name__ == '__main__':
    unittest.main()
