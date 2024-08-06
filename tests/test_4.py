
import requests

def test_link1():
    response = requests.get('http://www.cwa.mdx.ac.uk/spikeLearn/spikeLearn.html')
    assert response.status_code == 200

def test_link2():
    response = requests.get('https://www.humanbrainproject.eu/')
    assert response.status_code == 200

def test_link3():
    response = requests.get('http://www.ics.uci.edu/~mlearn/MLRepository.html')
    assert response.status_code == 200

def test_link4():
    response = requests.get('http://www.cwa.mdx.ac.uk/chris/chrisroot.html')
    assert response.status_code == 200
