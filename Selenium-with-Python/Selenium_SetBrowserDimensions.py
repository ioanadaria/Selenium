from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# --- Setup ChromeDriver ---
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# --- Open a sample website ---
URL = "https://www.wikipedia.org/"
driver.get(URL)

try:
    # Give page a moment to load
    time.sleep(2)

    # Get the current window size
    current_size = driver.get_window_size()
    print(f"🪟 Current browser size: {current_size['width']}x{current_size['height']}")

    # Set custom dimensions (Width x Height)
    driver.set_window_size(1024, 768)
    print("✅ Browser resized to 1024x768")
    time.sleep(2)

    # Maximize the browser window
    driver.maximize_window()
    print("🖥️ Browser maximized")
    time.sleep(2)

    # Minimize the browser window
    driver.minimize_window()
    print("🔽 Browser minimized")
    time.sleep(2)

    # Restore window size to custom dimensions again
    driver.set_window_size(1280, 720)
    print("📏 Browser resized to 1280x720")

    print("🎉 Browser dimension handling test completed successfully!")

except Exception as e:
    print("❌ ERROR:", e)

finally:
    time.sleep(2)
    driver.quit()
