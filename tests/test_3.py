
import requests

def test_links():
    links = ['http://www.cwa.mdx.ac.uk/spikeLearn/spikeLearn.html', 'https://www.humanbrainproject.eu/', 'http://www.ics.uci.edu/~mlearn/MLRepository.html', 'http://www.cwa.mdx.ac.uk/chris/chrisroot.html']
    for link in links:
        try:
            response = requests.get(link)
            assert response.status_code == 200
            assert "://" in link
            domain = link.split("://")[1].split("/")[0]
            path = "/".join(link.split("://")[1].split("/")[1:])
            assert domain != "" and domain != None
            assert path != "" and path != None
        except AssertionError:
            print(f"Invalid URL structure for {link}")

