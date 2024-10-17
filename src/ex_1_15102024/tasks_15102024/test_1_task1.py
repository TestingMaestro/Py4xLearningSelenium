from selenium import webdriver
import pytest
import allure


@allure.title("Verify that user is able to get the current URL and Title of webpage")
@allure.description("vveifying the title and current url are retrieved properly or not")
def katalon_cura_demo_project_loginpage():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com")
    current_title = driver.title
    current_url = driver.current_url
    print(current_title)
    print(driver.current_url)
    if current_title in driver.page_source == current_title:
        print(driver.page_source)
    # assert current_title in driver.page_source, f"expected is {current_title} actual = {driver.page_source} "


katalon_cura_demo_project_loginpage()
