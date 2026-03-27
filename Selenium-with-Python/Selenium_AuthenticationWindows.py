from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Credentials loaded from environment variables for security
username = os.environ.get("BASIC_AUTH_USER", "admin")
password = os.environ.get("BASIC_AUTH_PASS", "admin")
url = "https://the-internet.herokuapp.com/basic_auth"

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
