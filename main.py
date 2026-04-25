from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
import time 

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://automationexercise.com")

assert "Automation Exercise" in driver.title

logo = driver.find_element(By.XPATH, "//img[@alt='Website for automation practice']")

try:
    logo = driver.find_element(By.XPATH, "//img[@alt='Website for automation practice']")
    assert logo.is_displayed(), "Home page logo not visible!"
except Exception as e:
    raise AssertionError("Logo locator failed.") from e


time.sleep(10)

driver.quit()