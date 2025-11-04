from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
import time

# Path to your ChromeDriver
service = Service("C:/Selenium_data/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Example page (replace as needed)
URL = "https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select_multiple"
driver.get(URL)

try:
    driver.maximize_window()

    # The example page uses an iframe, so we must switch to it
    driver.switch_to.frame("iframeResult")

    # Locate the multi-select element
    select = Select(driver.find_element(By.NAME, "cars"))

    # Select multiple options by value
    select.select_by_value("volvo")
    select.select_by_value("audi")

    print("✅ Selected values: volvo and audi")

    time.sleep(2)  # wait so you can see it happen

    # Deselect options by value
    select.deselect_by_value("volvo")
    select.deselect_by_value("audi")

    print("✅ Deselected values: volvo and audi")

except Exception as e:
    print("❌ ERROR:", e)

finally:
    time.sleep(2)
    driver.quit()
