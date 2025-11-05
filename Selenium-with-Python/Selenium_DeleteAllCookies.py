from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# --- Setup ChromeDriver ---
service = Service("C:/Selenium_data/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

URL = "https://www.example.com"
driver.get(URL)

try:
    driver.maximize_window()
    time.sleep(2)

    # --- Add some cookies for demonstration ---
    cookies_to_add = [
        {'name': 'cookie1', 'value': 'value1', 'domain': 'example.com', 'path': '/'},
        {'name': 'cookie2', 'value': 'value2', 'domain': 'example.com', 'path': '/'}
    ]
    for c in cookies_to_add:
        driver.add_cookie(c)
    print("✅ Cookies added successfully!")

    # --- Display cookies before deletion ---
    print("Before deleting all cookies:")
    for c in driver.get_cookies():
        print(c)

    # --- Delete all cookies ---
    driver.delete_all_cookies()
    print("✅ All cookies deleted successfully!")

    # --- Verify deletion ---
    if not driver.get_cookies():
        print("✅ Confirmed: no cookies exist")
    else:
        print("❌ Some cookies still exist:", driver.get_cookies())

except Exception as e:
    print("❌ ERROR:", e)

finally:
    time.sleep(2)
    driver.quit()
