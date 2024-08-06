
import re
import requests
from requests import HTTPError

def test_links():
    links = ['http://www.cwa.mdx.ac.uk/spikeLearn/spikeLearn.html', 'https://www.humanbrainproject.eu/', 'http://www.ics.uci.edu/~mlearn/MLRepository.html', 'http://www.cwa.mdx.ac.uk/chris/chrisroot.html']
    for link in links:
        try:
            r = requests.get(link)
            assert re.match(r"^http(s)?://", link), "Invalid protocol"
            assert re.match(r"^\w+(\.\w+)+$", link), "Invalid domain"
            assert re.match(r"^/.*$", link), "Invalid path"
            assert r.status_code == 200, "Invalid response"
        except HTTPError:
            print("Failed to connect")
