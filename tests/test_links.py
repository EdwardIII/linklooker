import unittest
from linklooker.linklooker import Links

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.links = Links(['http://google.com', 'http://not-a-real-domain-name.com'])

    def test_status_table(self):
        expected = { 'http://google.com': True, 'http://not-a-real-domain-name.com': False }
        self.assertEqual(sorted(self.links.status_table()), sorted(expected))

    def test_status_table_from_csv(self):
        expected = [ { 'url': 'http://edwardiii.co.uk/', 'is_success': True, 'contains_link': True } ]
        self.assertEqual(self.links.status_table_from_csv('tests/urls-to-test.csv'), expected);
        


if __name__ == '__main__':
    unittest.main()
