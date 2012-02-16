from urllib2 import Request, urlopen, HTTPError, URLError
import csv

class Links:
    """ Takes an array of urls, produces a dictionary with their status"""

    def __init__(self, urls = None):
        if urls: self.urls = urls

    def status_table(self):
        """ Returns an array of dictonaries:  { <domain>: <True|False> }  """
        return { l: Link(l).is_success() for l in self.urls }

    def status_table_from_csv(self, filename):
        """ 
        Imports a CSV with this format: <url>,<link to check this url actually contains>
        Returns a list of dictionaries, e.g.: [ { url: www.example.com, status: True, contains_link: True } ]
        """

        urls = csv.reader(open(filename))
        status_table = []
        for row in urls:
            link = Link(row[0])
            new_row = { 
                    'url': row[0], 
                    'is_success': link.is_success(), 
                    'contains_link': link.contains_url(row[1])
                    }
            status_table.append(new_row);

        return status_table

    def _csv_to_linkrows(filename):
        urls = csv.reader(open(filename))
        return map(lambda r: LinkRow(url=r[1], 
                    claimed_pagerank=r[2], target_link=r[4]), urls)


    def status_table_from_pagerank_csv(self, filename):
        """
        Imports CSV with this format: [ID],<URL to search>,<page rank to verify>,<search term in link>,<link destination>
        Returns a list of dictionaries, e.g.: [ { url: www.example.com, status: True, contains_link: True, pagerank_verified: True, pagerank: 2 } ]
        """

        urls = csv.reader(open(filename))
        status_table = []
        for row in urls:
            link = Link(row[1])
            new_row = { 
                    'url': row[1], 
                    'is_success': link.is_success(), 
                    'contains_link': link.contains_url(row[4]),
                    'pagerank_verified': link.has_pagerank(row[2]),
                    'pagerank': link.get_pagerank()
                    }
            status_table.append(new_row);

        return status_table

class LinkRow:
    """
    Represents a row as provided in a CSV file. 
    Required named parameters: url=, claimed_pagerank=, target_link=
    """
    def __init__(**kwargs):
        self.url = kwargs['url']
        self.claimed_pagerank = kwargs['claimed_pagerank']
        self.target_link = kwargs['target_link']

class Link:
    """ Represents a url as a link """

    def __init__(self, url):
        self.url = url
        self.pagerank = None

    def __str__(self):
        return self.url
    
    def _get_response(self):
        try:
            self.response = urlopen(Request(self.url))
        except(HTTPError, URLError):
            pass

    def is_success(self):
        """ Did this url return 200: Success code? Returns a boolean """
        self._get_response()

        if hasattr(self, 'response') and self.response.code == 200:
            return True
        else:
            return False

    def get_pagerank(self):
        if self.pagerank is None:
            from pagerank import getpagerank
            try:
                self.pagerank = int(getpagerank(self.url).strip())
            except ValueError:
                self.pagerank = 0 #XXX: But could be any non-intable value being passed through 

            return self.pagerank
        else:
            return self.pagerank

    def has_pagerank(self, rank):
        return True if int(rank) == self.get_pagerank() else False

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




