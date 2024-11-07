import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton


@allure.title("Action P3- ActionChains class - mouse events")
@allure.description("Verify the Actions P3 - click and hold")
def test_actions_p3():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    driver.maximize_window()
    element_to_hold = driver.find_element(By.XPATH, "//div[@id='draggable']")

    actions = ActionChains(driver=driver)
    actions.click_and_hold(on_element=element_to_hold).perform()
    time.sleep(10)
