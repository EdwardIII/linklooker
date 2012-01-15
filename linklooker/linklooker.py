from urllib2 import Request, urlopen, HTTPError

class Links:
    """ Takes an array of urls, produced a dictionary with their status"""

    def __init__(self, urls):
        self.urls = urls

    def status_table(self):
        """ Returns an array of dictonaries: [ { <domain>: <Good|Bad> } ] """
        return map( lambda l: { l: l.is_success() }, self.urls )


class Link:
    """ Represents a url as a link with a urllib resource """

    def __init__(self, url):
        self.url = url

    def __str__(self):
        return self.url

    def is_success(self):
        req = Request(self.url)

        try:
            self.response = urlopen(req);
        except(HTTPError):
            pass


        if hasattr(self, 'response') and self.response.code == 200:
            return True
        else:
            return False


