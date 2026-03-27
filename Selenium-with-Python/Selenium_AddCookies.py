from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# --- Setup ChromeDriver ---
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

URL = "https://www.example.com"
driver.get(URL)

try:
    driver.maximize_window()
    time.sleep(2)

    # --- Add a cookie ---
    cookie = {
        'name': 'my_test_cookie',
        'value': 'selenium_cookie_value',
        'domain': 'example.com',
        'path': '/',
        'secure': True
    }
    driver.add_cookie(cookie)
    print("✅ Cookie added successfully!")

    # --- Retrieve all cookies ---
    all_cookies = driver.get_cookies()
    print("All cookies on the site:")
    for c in all_cookies:
        print(c)

    # --- Get specific cookie ---
    retrieved_cookie = driver.get_cookie('my_test_cookie')
    print("Retrieved cookie:", retrieved_cookie)

    # --- Delete a specific cookie ---
    driver.delete_cookie('my_test_cookie')
    print("✅ Cookie deleted successfully!")

    # --- Verify deletion ---
    print("Cookies after deletion:", driver.get_cookies())

    print("🎉 Cookie handling demo completed successfully!")

except Exception as e:
    print("❌ ERROR:", e)

finally:
    time.sleep(2)
    driver.quit()
