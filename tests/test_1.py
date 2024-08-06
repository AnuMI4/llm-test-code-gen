
import requests

def test_links():
    links = ['http://www.cwa.mdx.ac.uk/spikeLearn/spikeLearn.html', 'https://www.humanbrainproject.eu/', 'http://www.ics.uci.edu/~mlearn/MLRepository.html', 'http://www.cwa.mdx.ac.uk/chris/chrisroot.html']
    for link in links:
        response = requests.get(link)
        assert response.status_code == 200
