from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
import time

# Setup ChromeDriver
service = Service("C:/Selenium_data/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# URL with a multi-select dropdown
URL = "https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select_multiple"
driver.get(URL)

try:
    driver.maximize_window()
    driver.switch_to.frame("iframeResult")  # Dropdown is inside an iframe

    # Initialize Select object
    select = Select(driver.find_element(By.NAME, "cars"))

    # --- Helper function to print selected options ---
    def print_selected():
        selected = [opt.text for opt in select.all_selected_options]
        print("🟢 Currently selected options:", selected if selected else "None")

    # --- SELECT METHODS ---
    print("\n--- Selecting Options ---")

    select.select_by_visible_text("Volvo")
    print("✅ Selected by visible text: Volvo")
    print_selected()
    time.sleep(1)

    select.select_by_value("audi")
    print("✅ Selected by value: audi")
    print_selected()
    time.sleep(1)

    select.select_by_index(2)  # Opel
    print("✅ Selected by index: 2 (Opel)")
    print_selected()
    time.sleep(1)

    # --- DESELECT METHODS ---
    print("\n--- Deselecting Options ---")

    select.deselect_by_value("audi")
    print("✅ Deselected by value: audi")
    print_selected()
    time.sleep(1)

    select.deselect_all()
    print("✅ All options deselected")
    print_selected()
    time.sleep(1)

    print("\n🎉 Test Completed Successfully!")

except Exception as e:
    print("❌ ERROR:", e)

finally:
    time.sleep(2)
    driver.quit()
