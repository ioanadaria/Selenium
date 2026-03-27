import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    StaleElementReferenceException,
    ElementClickInterceptedException,
    NoSuchElementException,
)

MAX_RETRIES = 3
WAIT_BETWEEN_RETRIES = 1


class TestHandleStaleElement:
    URL = "https://www.w3schools.com/js/tryit.asp?filename=tryjs_myfirst"

    def _safe_click(self, driver, by, locator):
        for attempt in range(MAX_RETRIES):
            try:
                elem = driver.find_element(by, locator)
                driver.execute_script("arguments[0].click();", elem)
                return elem
            except StaleElementReferenceException:
                time.sleep(WAIT_BETWEEN_RETRIES)
            except ElementClickInterceptedException:
                elem = driver.find_element(by, locator)
                driver.execute_script("arguments[0].click();", elem)
                return elem
        raise Exception(f"Failed to click element after {MAX_RETRIES} attempts")

    def test_stale_element_handling(self, driver):
        driver.get(self.URL)
        time.sleep(2)

        try:
            overlay = driver.find_element(By.CSS_SELECTOR, ".sn-content")
            driver.execute_script("arguments[0].style.display='none';", overlay)
        except NoSuchElementException:
            pass

        iframe = driver.find_element(By.ID, "iframeResult")
        driver.switch_to.frame(iframe)

        text_locator = (By.ID, "demo")
        text_elem = driver.find_element(*text_locator)
        original_text = text_elem.text

        self._safe_click(driver, By.TAG_NAME, "button")
        time.sleep(1)

        updated_text = None
        for _ in range(MAX_RETRIES):
            try:
                updated_text = text_elem.text
                break
            except StaleElementReferenceException:
                text_elem = driver.find_element(*text_locator)
                time.sleep(WAIT_BETWEEN_RETRIES)

        assert updated_text is not None
        assert updated_text != original_text
