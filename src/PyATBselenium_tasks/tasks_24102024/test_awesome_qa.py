import time

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Verify that the user is able to check boxes and radio buttons")
@allure.description("Verify that the user is able to check boxes and radio buttons")
def test_handling_alerts_accept():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    driver.maximize_window()
    time.sleep(5)
    gender_eles = driver.find_elements(By.XPATH, "//b[contains(text(),'Gen')]/parent::div/input")
    WebDriverWait(driver=driver, timeout=5).until(
        EC.presence_of_all_elements_located((By.XPATH, "//b[contains(text(),'Gen')]/parent::div/input")))

    prof_eles = driver.find_elements(By.XPATH, "//span[text()='Profession']/parent::div/input")
    WebDriverWait(driver=driver, timeout=5).until(
        EC.presence_of_all_elements_located((By.XPATH, "//span[text()='Profession']/parent::div/input")))

    yoe_eles = driver.find_elements(By.XPATH, "//span[text()='Years of Experience']/parent::div/input")
    WebDriverWait(driver=driver, timeout=5).until(
        EC.presence_of_all_elements_located((By.XPATH, "//span[text()='Years of Experience']/parent::div/input")))

    for ele1 in range(len(gender_eles)):
        WebDriverWait(driver=driver, timeout=5).until(
            EC.element_to_be_clickable((By.XPATH, "//b[contains(text(),'Gen')]/parent::div/input")))
        # gender_eles[ele1].click()
        gender_eles[1].click()
        element1_clicked = gender_eles[1].is_selected()

        assert element1_clicked == True

    for ele2 in range(len(prof_eles)):
        WebDriverWait(driver=driver, timeout=5).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Profession']/parent::div/input")))
        # prof_eles[ele2].click()
        prof_eles[1].click()
        element2_clicked = prof_eles[1].is_selected()
        assert element2_clicked == True
        break

    for ele3 in range(len(yoe_eles)):
        WebDriverWait(driver=driver, timeout=5).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Years of Experience']/parent::div/input")))
        # yoe_eles[ele3].click()
        yoe_eles[2].click()
        element3_clicked = yoe_eles[2].is_selected()
        assert element3_clicked == True

    # prof_eles = driver.find_element(By.XPATH, "//span[text()='Profession']/parent::div/input[last()]")
    # yoe_eles = driver.find_element(By.XPATH, "//span[text()='Years of Experience']/parent::div/input[position() = 3]")
    # gender_eles.click()
    #
    # prof_ele = driver.find_element(By.XPATH, "//span[text()='Profession']/parent::div/input[last()]")
    # prof_ele.click()
    #
    # yoe_ele = driver.find_element(By.XPATH, "//span[text()='Years of Experience']/parent::div/input[position() = 3]")
    # yoe_ele.click()

    # or
