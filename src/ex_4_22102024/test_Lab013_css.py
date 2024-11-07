from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os, time


def test_vwo_using_css_selector(browser_options, driver):
    load_dotenv()
    driver.get("https://app.vwo.com")
    user_name = driver.find_element(By.CSS_SELECTOR, "input[id='login-username']")
    user_name.send_keys(os.getenv("USERNAME"))
    password = driver.find_element(By.CSS_SELECTOR, "#login-password")
    password.send_keys(os.getenv("PASSWORD"))
    time.sleep(4)
