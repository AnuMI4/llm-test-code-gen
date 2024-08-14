def test_phone_field_is_editable():
    driver = webdriver.Chrome()
    driver.get("https://demo.wpeverest.com/user-registration/guest-registration-form/")
    phone_input = driver.find_element_by_id("phone_1665627880")
    phone_input.send_keys("1234567890")
    assert phone_input.get_attribute("value") == "1234567890"
