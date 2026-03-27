class TestCookies:
    URL = "https://www.example.com"

    def test_add_and_retrieve_cookie(self, driver):
        driver.get(self.URL)
        cookie = {
            "name": "my_test_cookie",
            "value": "selenium_cookie_value",
            "domain": "example.com",
            "path": "/",
            "secure": True,
        }
        driver.add_cookie(cookie)
        retrieved = driver.get_cookie("my_test_cookie")
        assert retrieved is not None
        assert retrieved["value"] == "selenium_cookie_value"

    def test_delete_cookie_by_name(self, driver):
        driver.get(self.URL)
        driver.add_cookie({"name": "my_test_cookie", "value": "selenium_cookie_value"})
        driver.delete_cookie("my_test_cookie")
        assert driver.get_cookie("my_test_cookie") is None

    def test_delete_all_cookies(self, driver):
        driver.get(self.URL)
        driver.add_cookie({"name": "cookie1", "value": "value1"})
        driver.add_cookie({"name": "cookie2", "value": "value2"})
        driver.delete_all_cookies()
        assert driver.get_cookies() == []
