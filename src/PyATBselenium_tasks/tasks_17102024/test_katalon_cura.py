import time
import allure
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


@allure.title("Katalon-cura-demo project login test")
@allure.description("Verifying username/password and Login button functionality ")
def test_Katalon_cura_demo_login_tc_chrome(browser_options):
    driver = webdriver.Chrome(browser_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_appointment_btn = driver.find_element(By.ID, value="btn-make-appointment")
    make_appointment_btn.click()
    current_url = driver.current_url
    print(current_url)
    time.sleep(6)
    assert current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    user_name = driver.find_element(By.NAME, value="username")
    user_name.send_keys("John Doe")
    password = driver.find_element(By.NAME, value="password")
    password.send_keys("ThisIsNotAPassword")
    login_btn = driver.find_element(By.ID, value="btn-login")
    login_btn.click()
    time.sleep(6)
    home_page_url = driver.current_url
    print(home_page_url)
    assert home_page_url == "https://katalon-demo-cura.herokuapp.com/#appointment"
    time.sleep(10)
