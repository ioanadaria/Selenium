"""
Basic HTTP authentication test using a purpose-built test site.
Credentials for https://the-internet.herokuapp.com/basic_auth are: admin / admin
"""


class TestAuthentication:
    BASE_URL = "https://the-internet.herokuapp.com/basic_auth"
    USERNAME = "admin"
    PASSWORD = "admin"

    def test_basic_auth_via_url(self, driver):
        host = self.BASE_URL.replace("https://", "")
        auth_url = f"https://{self.USERNAME}:{self.PASSWORD}@{host}"
        driver.get(auth_url)
        assert "Basic Auth" in driver.page_source
        assert "Congratulations" in driver.page_source
