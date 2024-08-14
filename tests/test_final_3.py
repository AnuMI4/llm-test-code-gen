from selenium import webdriver
import pytest

@pytest.mark.parametrize("input_type", ["firstName", "lastName"])
def test_editable_fields(input_type):
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/register")
    input_field = driver.find_element_by_name(input_type)
    assert input_field.is_displayed() and input_field.is_enabled()
    input_field.send_keys("Test User")
    assert input_field.get_attribute("value") == "Test User"
    driver.quit()

@pytest.mark.parametrize("link", ["Cancel"])
def test_links(link):
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/register")
    link = driver.find_element_by_link_text(link)
    assert link.is_displayed() and link.is_enabled()
    response = requests.get(link.get_attribute("href"))
    assert response.status_code == 200
    url = "http://localhost:3000/login" + "/register"
    assert driver.current_url == url
    driver.quit()