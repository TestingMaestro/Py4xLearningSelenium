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


@allure.title("Action P2 - ActionChains class - mouse events")
@allure.description("Verify the Actions P2 - Mouse Back")
def test_actions_p2():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    driver.maximize_window()
    click_link = driver.find_element(By.XPATH, "//a[@id='click']")
    click_link.click()
    time.sleep(5)
    action_builder = ActionBuilder(driver=driver)
    action_builder.pointer_action.pointer_up(MouseButton.BACK)
    action_builder.perform()
