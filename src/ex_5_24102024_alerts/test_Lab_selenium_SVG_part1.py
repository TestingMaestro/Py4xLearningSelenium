import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


@allure.title("Verify SVG")
@allure.description("Handling SVG")
def test_handling_svg():
    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com/")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Mac Mini")

    (WebDriverWait(driver=driver, timeout=10).
     until(EC.visibility_of_element_located((By.NAME, "q"))))

    list_svg_element = driver.find_elements(By.XPATH, "//*[local-name()='svg']")
    print(len(list_svg_element))

    (WebDriverWait(driver=driver, timeout=10).
     until(EC.presence_of_all_elements_located((By.XPATH, "//*[local-name()='svg']"))))

    list_svg_element[0].click()
    text = list_svg_element[0].text
    print(text)
    time.sleep(5)
