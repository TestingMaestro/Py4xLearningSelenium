import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_vwo_start_free_trial(browser_options):
    driver = webdriver.Chrome(browser_options)
    driver.get("https://app.vwo.com/#/login")
    driver.implicitly_wait(8)
    anchor_tag = driver.find_element(By.LINK_TEXT, "Start a free trial")
    anchor_tag.click()

    sso_page_title = driver.title
    print(sso_page_title)

    assert sso_page_title == "Get Started with Free Trial | VWO"
    driver.back()
