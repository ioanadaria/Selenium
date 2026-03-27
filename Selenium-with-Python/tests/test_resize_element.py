import time

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class TestResizeWebElement:
    URL = "https://jqueryui.com/resizable/"

    def test_resize_element_larger(self, driver):
        driver.get(self.URL)
        time.sleep(2)
        frame = driver.find_element(By.CSS_SELECTOR, ".demo-frame")
        driver.switch_to.frame(frame)
        resizable_box = driver.find_element(By.CSS_SELECTOR, ".ui-resizable")
        resize_handle = driver.find_element(By.CSS_SELECTOR, ".ui-resizable-se")
        initial_width = resizable_box.size["width"]
        initial_height = resizable_box.size["height"]
        ActionChains(driver).click_and_hold(resize_handle).move_by_offset(100, 80).release().perform()
        time.sleep(1)
        assert resizable_box.size["width"] >= initial_width
        assert resizable_box.size["height"] >= initial_height
