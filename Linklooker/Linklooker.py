from urllib2 import Request, urlopen, HTTPError

class Linklooker:
    """ Glue class for the linklooker """

    def __init__(self, url):
        self.links = []
        self.links.append(link(url))

    def get_status():
        """ Returns a dictionary containing { <domain>: <Good|Bad> } """
        return


class Link:
    """ Represents a url as a link with a urllib resource """

    def __init__(self, url):
        self.url = url

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


