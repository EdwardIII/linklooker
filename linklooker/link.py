from urllib2 import Request, urlopen

class link:
    """ Base class for the linklooker """

    def __init__(self, url):
        self.url = url

    def is_success():
        req = Request(self.url)
        self.response = urlopen(req);
        if(self.response == 200):
            return 1
        else:
            return 0


