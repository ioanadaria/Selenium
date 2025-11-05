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

    # --- Add a cookie to demonstrate deletion ---
    cookie = {
        'name': 'my_test_cookie',
        'value': 'selenium_cookie_value',
        'domain': 'example.com',
        'path': '/',
        'secure': True
    }
    driver.add_cookie(cookie)
    print("✅ Cookie added successfully!")

    # --- Verify the cookie exists ---
    print("Before deletion, cookies:")
    for c in driver.get_cookies():
        print(c)

    # --- Delete cookie by name ---
    driver.delete_cookie('my_test_cookie')
    print("✅ Cookie 'my_test_cookie' deleted successfully!")

    # --- Verify deletion ---
    print("After deletion, cookies:")
    for c in driver.get_cookies():
        print(c)

    # --- Optional: Check if cookie still exists ---
    if driver.get_cookie('my_test_cookie') is None:
        print("✅ Confirmed: cookie no longer exists")
    else:
        print("❌ Cookie still exists!")

except Exception as e:
    print("❌ ERROR:", e)

finally:
    time.sleep(2)
    driver.quit()
