from selenium.webdriver.common.by import By


class TestBasicNavigation:
    def test_open_google_with_css_selector(self, firefox_driver):
        firefox_driver.get("https://www.google.com")
        assert "Google" in firefox_driver.title
