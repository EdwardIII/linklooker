from urllib2 import Request, urlopen, HTTPError, URLError

class Links:
    """ Takes an array of urls, produces a dictionary with their status"""

    def __init__(self, urls):
        self.urls = urls

    def status_table(self):
        """ Returns an array of dictonaries:  { <domain>: <True|False> }  """
        return { l: Link(l).is_success() for l in self.urls }


class Link:
    """ Represents a url as a link with a urllib resource """

    def __init__(self, url):
        self.url = url
        

    def __str__(self):
        return self.url
    
    def _get_response(self):
        try:
            self.response = urlopen(Request(self.url))
        except(HTTPError, URLError):
            pass

    def is_success(self):
        """ Did this url return 200: Success code? Returns a boolean """
        self._get_response();

        if hasattr(self, 'response') and self.response.code == 200:
            return True
        else:
            return False

    def contains_url(self, url):
        """ Does the page this link points to contain the url inputted? Returns a boolean """

        from BeautifulSoup import BeautifulSoup
        self._get_response();
        if not hasattr(self, 'response'):
            return False #TODO: Should probably raise exception
        doc = BeautifulSoup(self.response.read())
                
        link_featuring_url = doc.find('a', href=url)

        
        if link_featuring_url:
            return True
        else:
            return False




