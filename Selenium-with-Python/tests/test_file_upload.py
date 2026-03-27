import time

from selenium.webdriver.common.by import By


class TestFileUpload:
    """
    Uses https://the-internet.herokuapp.com/upload — a purpose-built test site
    that avoids AutoIt or hardcoded local file paths.
    """

    URL = "https://the-internet.herokuapp.com/upload"

    def test_file_upload_via_send_keys(self, driver, tmp_path):
        test_file = tmp_path / "test_upload.txt"
        test_file.write_text("Selenium file upload test content")

        driver.get(self.URL)
        file_input = driver.find_element(By.ID, "file-upload")
        file_input.send_keys(str(test_file))
        driver.find_element(By.ID, "file-submit").click()
        time.sleep(1)

        assert "File Uploaded!" in driver.page_source
