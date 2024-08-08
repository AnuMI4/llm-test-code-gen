def test_link_1():
  response = requests.get("http://www.cwa.mdx.ac.uk/spikeLearn/spikeLearn.html")
  assert response.status_code == 200

def test_link_2():
  response = requests.get("https://www.humanbrainproject.eu/")
  assert response.status_code == 200

def test_link_3():
  response = requests.get("http://www.ics.uci.edu/~mlearn/MLRepository.html")
  assert response.status_code == 200

def test_link_4():
  response = requests.get("http://www.cwa.mdx.ac.uk/chris/chrisroot.html")
  assert response.status_code == 200