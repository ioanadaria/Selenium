from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# ChromeDriver path
service = Service("C:/Selenium_data/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Replace these with your credentials and URL
username = "myUsername"
password = "myPassword"
url = "https://example.com/protected"  # URL that requires basic auth

# Format URL with credentials
auth_url = f"https://{username}:{password}@{url.split('https://')[1]}"

try:
    driver.get(auth_url)
    driver.maximize_window()
    print("✅ Authenticated successfully!")

    time.sleep(3)  # wait to see the page

except Exception as e:
    print("❌ ERROR:", e)

finally:
    driver.quit()
