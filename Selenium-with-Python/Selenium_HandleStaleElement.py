from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException, NoSuchElementException
import time

# --- Config ---
CHROMEDRIVER_PATH = "C:/Selenium_data/chromedriver-win64/chromedriver-win64/chromedriver.exe"
URL = "https://www.w3schools.com/js/tryit.asp?filename=tryjs_myfirst"
MAX_RETRIES = 3
WAIT_BETWEEN_RETRIES = 1  # seconds

# --- Setup Chrome ---
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service)

try:
    driver.maximize_window()
    driver.get(URL)
    time.sleep(2)

    # --- Remove overlay if present ---
    try:
        overlay = driver.find_element(By.CSS_SELECTOR, ".sn-content")
        driver.execute_script("arguments[0].style.display='none';", overlay)
        print("Overlay removed")
    except NoSuchElementException:
        pass

    # --- Switch to iframe if needed ---
    iframe = driver.find_element(By.ID, "iframeResult")
    driver.switch_to.frame(iframe)

    # --- Helper function to safely click element ---
    def safe_click(by, locator):
        for attempt in range(MAX_RETRIES):
            try:
                elem = driver.find_element(by, locator)
                driver.execute_script("arguments[0].click();", elem)
                return elem
            except StaleElementReferenceException:
                print(f"⚠️ StaleElementReferenceException caught on attempt {attempt + 1}, retrying...")
                time.sleep(WAIT_BETWEEN_RETRIES)
            except ElementClickInterceptedException:
                print(f"⚠️ ElementClickInterceptedException caught, clicking via JS")
                driver.execute_script("arguments[0].click();", elem)
                return elem
        raise Exception(f"❌ Failed to click element after {MAX_RETRIES} attempts")

    # --- Locate text element ---
    text_locator = (By.ID, "demo")
    text_elem = driver.find_element(*text_locator)
    print("Original text:", text_elem.text)

    # --- Click button safely ---
    button_elem = safe_click(By.TAG_NAME, "button")
    time.sleep(1)

    # --- Access text element safely after click ---
    for attempt in range(MAX_RETRIES):
        try:
            print("Updated text:", text_elem.text)
            break
        except StaleElementReferenceException:
            print(f"⚠️ StaleElementReferenceException caught when reading text, retry {attempt + 1}")
            text_elem = driver.find_element(*text_locator)
            time.sleep(WAIT_BETWEEN_RETRIES)

    print("🎉 Stale element handling demo completed successfully!")

except Exception as e:
    print("❌ ERROR:", e)

finally:
    time.sleep(2)
    driver.quit()
