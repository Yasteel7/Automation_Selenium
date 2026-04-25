from selenium.webdriver.common.by import By
import time
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def handle_popups(driver):
    try:
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.continue-prompt-text"))
        )
        driver.find_element(By.CSS_SELECTOR, "div.continue-prompt-text").click()
    except:
        pass


def test_register_user(driver):
    driver.get("http://automationexercise.com")
    assert "Automation Exercise" in driver.title

    driver.find_element(By.CSS_SELECTOR, "a[href='/login']").click()
    
    username = "TestUser"
    unique_email = f"testuser{int(time.time())}@example.com"
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-name']").send_keys(username)
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-email']").send_keys(unique_email)

    
    driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']").click()

    assert "Enter Account Information" in driver.page_source
    
    title_choice = random.choice(["id_gender1", "id_gender2"])
    WebDriverWait(driver, 3).until(
       EC.element_to_be_clickable((By.ID, title_choice))
    ).click()
    
    driver.find_element(By.ID, "password").send_keys("SecurePass123")
    
    # the site allows any number of days for each month so 1-31 works for all months
    day_dropdown = driver.find_element(By.ID, "days")
    Select(day_dropdown).select_by_value(str(random.randint(1, 31)))
    
    month_dropdown = driver.find_element(By.ID, "months")
    Select(month_dropdown).select_by_value(str(random.randint(1, 12)))
    
    year_dropdown = driver.find_element(By.ID, "years")
    Select(year_dropdown).select_by_value(str(random.randint(1900, 2021)))
    
    driver.find_element(By.ID, "newsletter").click()

    driver.find_element(By.ID, "first_name").send_keys("TestFirst")
    driver.find_element(By.ID, "last_name").send_keys("TestLast")
    driver.find_element(By.ID, "company").send_keys("TestCompany")
    driver.find_element(By.ID, "address1").send_keys("123 Test Street")
    driver.find_element(By.ID, "address2").send_keys("Suite 456")

    countries = ["India", "United States", "Canada", "Australia", "Israel", "New Zealand", "Singapore"]
    Select(driver.find_element(By.ID, "country")).select_by_visible_text(random.choice(countries))
    
    driver.find_element(By.ID, "state").send_keys("TestState")
    driver.find_element(By.ID, "city").send_keys("TestCity")
    driver.find_element(By.ID, "zipcode").send_keys("12345")
    driver.find_element(By.ID, "mobile_number").send_keys("+27111234567")
    
    handle_popups(driver)
    driver.find_element(By.CSS_SELECTOR, "button[data-qa='create-account']").click()

    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h2[data-qa='account-created'] b"))
    )
    success_message = driver.find_element(By.CSS_SELECTOR, "h2[data-qa='account-created'] b").text
    assert success_message == "ACCOUNT CREATED!"
    
    handle_popups(driver)
    driver.find_element(By.CSS_SELECTOR, "a[data-qa='continue-button']").click()
    
    handle_popups(driver)
    logged_in_user_element = WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, "//a[contains(., 'Logged in as')]/b"))
    )
    logged_in_user = logged_in_user_element.text
    assert logged_in_user == username

    handle_popups(driver)
    driver.find_element(By.LINK_TEXT, "Delete Account").click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h2[data-qa='account-deleted'] b"))
    )
    deleted_message = driver.find_element(By.CSS_SELECTOR, "h2[data-qa='account-deleted'] b").text
    assert deleted_message == "ACCOUNT DELETED!"

    handle_popups(driver)
    driver.find_element(By.CSS_SELECTOR, "a[data-qa='continue-button']").click()
