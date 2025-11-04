from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Path to your ChromeDriver
service = Service("C:/Selenium_data/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

URL = "https://google.com/"
driver.get(URL)

try:
    driver.maximize_window()

    # Create and handle alert
    driver.execute_script("window.alert('This is an alert');")
    time.sleep(2)  # small delay to show it
    alert = driver.switch_to.alert
    alert.accept()

    print("✅ Dialog box popped up and was successfully handled by the script")

except Exception as e:
    print("❌ ERROR:", e)

finally:
    driver.quit()
