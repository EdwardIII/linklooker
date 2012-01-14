import unittest
from Linklooker import Linklooker

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.looker = Linklooker(['http://google.com', 'http://not-a-real-domain-name.com'])

    def test_get_status(self):
        self.assertEqual(self.goodLink.is_success(), True)
        self.assertEqual(self.badLink.is_success(), False)

if __name__ == '__main__':
    unittest.main()
