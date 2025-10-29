from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# Set up Firefox WebDriver automatically
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

driver.get('https://www.google.com')

try:
    # Using CSS selector instead of XPath
    element = driver.find_element(By.CSS_SELECTOR, "div.Fgvgjc")
    print("TestCase Passed: Element by CSS Selector found")
except Exception as e:
    print("TestCase Failed: Element by CSS Selector not found")

driver.quit()





