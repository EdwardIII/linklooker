import unittest
from linklooker import linklooker

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.goodLinkWhichFeaturesMyGithub = linklooker.Link('http://edwardiii.co.uk/')
        self.goodLink = linklooker.Link('http://google.com/')
        self.badLink = linklooker.Link('http://obviously-wouldnt-exist-in-reality.com')

    def test_is_success(self):
        self.assertEqual(self.goodLink.is_success(), True)
        self.assertEqual(self.badLink.is_success(), False)

    def test_contains_url(self):
        my_github_url = 'http://github.com/EdwardIII/PasteBin'
        self.assertTrue(self.goodLinkWhichFeaturesMyGithub.contains_url(my_github_url))
        self.assertFalse(self.goodLink.contains_url(my_github_url))
        self.assertFalse(self.badLink.contains_url(my_github_url))

if __name__ == '__main__':
    unittest.main()
