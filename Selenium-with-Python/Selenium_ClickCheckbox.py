from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service = Service("C:/Selenium_data/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

URL = "https://www.w3schools.com/howto/howto_css_custom_checkbox.asp"
driver.get(URL)

try:
    driver.maximize_window()
    time.sleep(2)

    # Scroll and locate checkbox (use JS click for hidden/custom checkboxes)
    checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
    driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
    driver.execute_script("arguments[0].click();", checkbox)

    print("✅ Checkbox clicked successfully (even if hidden or custom).")
    print("🟢 Checkbox is selected:", checkbox.is_selected())

    time.sleep(2)

except Exception as e:
    print("❌ ERROR:", e)

finally:
    driver.quit()

