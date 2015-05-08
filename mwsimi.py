#!/usr/bin/env python

import mwclient
from IPython import embed
from sklearn.feature_extraction.text import TfidfVectorizer
import sys

# annoying stuff to make mwclient shut up about logging
import logging
class NullHandler(logging.Handler):
    def emit(self, record):
        pass
h = NullHandler()
logging.getLogger("mwclient").addHandler(h)
# end annoying stuff

class Site(object):

    def __init__(self, site=None, username=None, password=None):
        """Create a Site object

        Keyword arguments:
        site -- the URL to the MW site API (e.g. 'localhost/wiki.api.php')
        username -- the MW username
        password -- the MW password
        """
        if site:
            self.site = mwclient.Site(site)
        if username:
            self.username = username
        if password:
            self.password = password
        if site and username and password:
            self.site.login(username, password)

    def pagecount(self):
        """returns an integer of the total number of pages"""
        return sum(1 for _ in self.site.allpages())

    def loadpages(self, min_length=None, **kwargs):
        """loads all pages into an instance variable and calculates similarities

        Keyword arguments:
        min_length -- used to exclude very small pages which can often trigger false positives
        prefix -- select only pages starting with string
        namespace -- select only pages in namespace (integer as string)
        
        Other keyword arguments, see the mwclient.allpages docstring at:
        https://github.com/mwclient/mwclient/blob/87d525fd24db3546f8b2b9d1ffa1dc50975911cc/mwclient/client.py#L565
        """
        ttl = self.pagecount()
        loaded = 0
        self.allpages = []

        for page in self.site.allpages(**kwargs):
            sys.stdout.write('\rLoaded %s of %s' % (loaded, ttl))
            sys.stdout.flush()
            if len(page.text()) >= min_length:
                self.allpages.append( { 'index': loaded-1, 'title': page.name, 'text': page.text() } )
                loaded += 1

        allpages_text = [x['text'] for x in self.allpages]
        vect = TfidfVectorizer(min_df=1)
        tfidf = vect.fit_transform(allpages_text)
        self.raw_sims = (tfidf * tfidf.T).A

        for page in self.allpages:
            hits = [] # this holds the indexes of pages with high similarity scores
            idx = 0
            for score in self.raw_sims[page['index']]:
                if score > 0.5 and idx != page['index']:
                    hits.append(idx)
                idx += 1
            page['hits'] = hits

if __name__ == '__main__':
    dev = Site('CHANGEME', 'CHANGEME', 'CHANGEME')
    embed()
