from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
try:
    import autoit
    AUTOIT_AVAILABLE = True
except ImportError:
    AUTOIT_AVAILABLE = False

# --- Setup ChromeDriver ---
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# --- URL with file upload ---
URL = "https://www.w3schools.com/howto/howto_html_file_upload_button.asp"
driver.get(URL)

# --- File to upload ---
file_path = os.environ.get("UPLOAD_FILE_PATH", r"C:\path\to\your\file.txt")  # set via env var

try:
    driver.maximize_window()
    time.sleep(2)

    # Locate the file input
    file_input = driver.find_element(By.XPATH, "//input[@type='file']")

    try:
        # Try Selenium send_keys first
        file_input.send_keys(file_path)
        print("✅ File uploaded using Selenium send_keys!")

    except Exception as e:
        print("⚠️ Selenium send_keys failed:", e)
        print("Trying AutoIt fallback...")

        # Make hidden input visible if needed
        driver.execute_script("arguments[0].style.display='block';", file_input)
        driver.execute_script("arguments[0].click();", file_input)
        time.sleep(2)  # wait for dialog to appear

        # AutoIt handling
        dialog_title = "Open"  # Adjust if your Windows uses another language
        autoit.win_wait(dialog_title, 10)
        autoit.control_set_text(dialog_title, "Edit1", file_path)
        autoit.control_click(dialog_title, "Button1")
        print("✅ File uploaded using AutoIt fallback!")

    time.sleep(2)
    print("🎉 File upload process completed successfully!")

except Exception as e:
    print("❌ ERROR:", e)

finally:
    driver.quit()

