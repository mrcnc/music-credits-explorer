import requests # http://pypi.python.org/pypi/requests
import time
import hashlib
import urllib
import os

class AllMusicGuide(object):
    api_url = 'http://api.rovicorp.com/data/v1'

    key = os.environ['ROVI_KEY']
    secret = os.environ['ROVI_SECRET']

    def _sig(self):
        timestamp = int(time.time())

        m = hashlib.md5()
        m.update(self.key)
        m.update(self.secret)
        m.update(str(timestamp))

        return m.hexdigest()

    def get(self, resource, params=None):
        """Take a dict of params, and return what we get from the api"""

        if not params:
            params = {}

        params = urllib.urlencode(params)

        sig = self._sig()

        url = "%s/%s?apiKey=%s&sig=%s&%s" % (self.api_url, resource, self.key, sig, params)
        print "making request %s" % url

        resp = requests.get(url)

        if resp.status_code != 200:
            # THROW APPROPRIATE ERROR
            pass

        return resp.content
