from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Setup ChromeDriver
service = Service("C:/Selenium_data/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Example page with multiple checkboxes
URL = "https://www.w3schools.com/howto/howto_css_custom_checkbox.asp"
driver.get(URL)

try:
    driver.maximize_window()
    time.sleep(2)

    # Find all checkboxes on the page
    checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

    print(f"Found {len(checkboxes)} checkboxes on the page.\n")

    for index, checkbox in enumerate(checkboxes, start=1):
        # Scroll into view
        driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
        time.sleep(0.5)

        # Safe click: use JS click if normal click fails
        try:
            checkbox.click()
        except:
            driver.execute_script("arguments[0].click();", checkbox)

        print(f"Checkbox {index} clicked successfully.")
        print(f"🟢 Checkbox {index} selected state: {checkbox.is_selected()}\n")
        time.sleep(0.5)

    print("🎉 All checkboxes processed successfully!")

except Exception as e:
    print("❌ ERROR:", e)

finally:
    time.sleep(2)
    driver.quit()
