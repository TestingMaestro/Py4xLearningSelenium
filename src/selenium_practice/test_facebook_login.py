import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_fb_login():

    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/")
    user_email = driver.find_element(By.NAME, value="email")
    user_email.send_keys("lihilfilsj")
    user_pass = driver.find_element(By.NAME, value="pass")
    user_email.send_keys("lihilfilsj")
    time.sleep(9)
