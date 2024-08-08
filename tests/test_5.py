
import requests

def test_cwa():
    url = "http://www.cwa.mdx.ac.uk/spikeLearn/spikeLearn.html"
    response = requests.get(url)
    assert response.status_code == 200

def test_humanbrainproject():
    url = "https://www.humanbrainproject.eu/"
    response = requests.get(url)
    assert response.status_code == 200

def test_mlrepository():
    url = "http://www.ics.uci.edu/~mlearn/MLRepository.html"
    response = requests.get(url)
    assert response.status_code == 200

def test_chris():
    url = "http://www.cwa.mdx.ac.uk/chris/chrisroot.html"
    response = requests.get(url)
    assert response.status_code == 200
