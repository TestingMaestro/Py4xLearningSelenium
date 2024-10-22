import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os


@allure.title("Verify the registration page")
@allure.description(
    "Complete all the required fields , ensure the user is successfully registered, and verify that the 'Your Account "
    "has been Created!' message is displayed")
def test_registration_page(browser_options):
    load_dotenv()

    driver = webdriver.Chrome(browser_options)
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")

    # Registration Details
    first_name = driver.find_element(By.NAME, "firstname")
    first_name.send_keys(os.getenv("FIRSTNAME"))

    last_name = driver.find_element(By.NAME, "lastname")
    last_name.send_keys(os.getenv("LASTNAME"))

    e_mail = driver.find_element(By.NAME, "email")
    e_mail.send_keys(os.getenv("EMAIL"))

    telephone = driver.find_element(By.NAME, "telephone")
    telephone.send_keys(os.getenv("PH_NO"))

    password = driver.find_element(By.NAME, "password")
    password.send_keys(os.getenv("PASSWORD"))

    confirm_password = driver.find_element(By.ID, "input-confirm")
    confirm_password.send_keys(os.getenv("PASSWORD"))

    privacy_checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
    privacy_checkbox.click()
    time.sleep(5)

    continue_btn = driver.find_element(By.XPATH, "//input[@value='Continue']")
    continue_btn.submit()  # works only if the button type is submit
    time.sleep(5)

    current_title = driver.title
    if current_title == "Your Account Has Been Created!":
        verify_text = driver.find_element(By.XPATH, "// h1[text() = 'Your Account Has Been Created!'] / parent::div / "
                                                    "h1")
        assert verify_text.text == current_title
        print("Title:", current_title)
        print("Webpage text:", verify_text)
        time.sleep(5)
