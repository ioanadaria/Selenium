import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class TestSelectByIndex:
    URL = "https://www.selenium.dev/selenium/web/web-form.html"

    def test_select_option_by_index(self, driver):
        driver.get(self.URL)
        select = Select(driver.find_element(By.ID, "my-select"))
        select.select_by_index(1)
        assert select.first_selected_option is not None


class TestSelectByValue:
    URL = "https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select_multiple"

    def test_select_and_deselect_by_value(self, driver):
        driver.get(self.URL)
        driver.switch_to.frame("iframeResult")
        select = Select(driver.find_element(By.NAME, "cars"))
        select.select_by_value("volvo")
        select.select_by_value("audi")
        selected_values = [opt.get_attribute("value") for opt in select.all_selected_options]
        assert "volvo" in selected_values
        assert "audi" in selected_values
        select.deselect_by_value("volvo")
        select.deselect_by_value("audi")
        assert select.all_selected_options == []


class TestSelectAllMethods:
    URL = "https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select_multiple"

    def test_all_select_methods(self, driver):
        driver.get(self.URL)
        driver.switch_to.frame("iframeResult")
        select = Select(driver.find_element(By.NAME, "cars"))

        select.select_by_visible_text("Volvo")
        assert any(opt.text == "Volvo" for opt in select.all_selected_options)

        select.select_by_value("audi")
        assert any(opt.get_attribute("value") == "audi" for opt in select.all_selected_options)

        select.select_by_index(2)
        select.deselect_by_value("audi")
        select.deselect_all()
        assert select.all_selected_options == []
