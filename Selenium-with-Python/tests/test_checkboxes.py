from selenium.webdriver.common.by import By


class TestCheckboxes:
    URL = "https://www.w3schools.com/howto/howto_css_custom_checkbox.asp"

    def test_click_single_checkbox(self, driver):
        driver.get(self.URL)
        checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
        driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
        driver.execute_script("arguments[0].click();", checkbox)
        assert checkbox.is_selected()

    def test_click_all_checkboxes(self, driver):
        driver.get(self.URL)
        checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
        assert len(checkboxes) > 0, "No checkboxes found on page"
        for checkbox in checkboxes:
            driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
            try:
                checkbox.click()
            except Exception:
                driver.execute_script("arguments[0].click();", checkbox)
        assert all(cb.is_selected() for cb in checkboxes)
