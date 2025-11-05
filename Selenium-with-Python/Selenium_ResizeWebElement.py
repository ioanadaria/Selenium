from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

# --- Setup ChromeDriver ---
service = Service("C:/Selenium_data/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# --- Open sample site with resizable element ---
URL = "https://jqueryui.com/resizable/"
driver.get(URL)

try:
    driver.maximize_window()
    time.sleep(2)

    # --- Switch to the iframe containing the resizable element ---
    frame = driver.find_element(By.CSS_SELECTOR, ".demo-frame")
    driver.switch_to.frame(frame)

    # --- Locate the resize handle (bottom-right corner of the box) ---
    resize_handle = driver.find_element(By.CSS_SELECTOR, ".ui-resizable-se")

    # --- Perform click-and-drag action to resize the element ---
    actions = ActionChains(driver)
    actions.click_and_hold(resize_handle).move_by_offset(100, 80).release().perform()
    print("✅ Element resized successfully by 100x80 pixels")

    time.sleep(2)

    # Try another resize (smaller this time)
    actions.click_and_hold(resize_handle).move_by_offset(-50, -30).release().perform()
    print("✅ Element resized again (shrunk by 50x30 pixels)")

    print("🎉 Web element resizing test completed successfully!")

except Exception as e:
    print("❌ ERROR:", e)

finally:
    time.sleep(2)
    driver.quit()
