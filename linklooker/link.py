from urllib2 import Request, urlopen

class link:
    """ Represents a url as a link with a urllib resource """

    def __init__(self, url):
        self.url = url

    def is_success(self):
        req = Request(self.url)
        self.response = urlopen(req);
        if(self.response.code == 200):
            return 1
        else:
            return 0


