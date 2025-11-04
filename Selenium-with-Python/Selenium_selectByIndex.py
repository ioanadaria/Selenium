from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service

# Path to your ChromeDriver
service = Service("C:/Selenium_data/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

URL = "https://www.selenium.dev/selenium/web/web-form.html"
driver.get(URL)

try:
    driver.maximize_window()

    driver.find_element(By.ID, "inputEmail").send_keys("Alan_Alford63@hotmail.com")
    driver.find_element(By.ID, "inputPassword").send_keys("Alan_Alford63")
    driver.find_element(By.ID, "inputAddress").send_keys("Newton Building, Ste 472")
    driver.find_element(By.ID, "inputCity").send_keys("Seattle")
    driver.find_element(By.ID, "inputZip").send_keys("WA 98195")

    # ✅ Select multiple options
    opt = Select(driver.find_element(By.ID, "inputgadget"))
    opt.select_by_index(2)
    opt.select_by_index(1)

    print("✅ Test Case Passed")

except Exception as e:
    print("❌ Test Case Failed:", e)

finally:
    driver.quit()
