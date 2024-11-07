import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import *

@allure.title("Verify SVG")
@allure.description("Handling SVG")
def test_handling_svg():
    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com/")
    try:
        search_box = driver.find_element(By.NAME, "q")
        (WebDriverWait(driver=driver, timeout=10).
         until(EC.visibility_of_element_located((By.NAME, "q1"))))
        driver.refresh()
        search_box.send_keys("Mac Mini")
    except (StaleElementReferenceException,TimeoutException) as ee:
        print(ee)
