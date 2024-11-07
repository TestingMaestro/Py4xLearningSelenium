import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure


@allure.title("ActionChains class - drag_and drop")
@allure.description("Verify the Actions P3 - drag_drop")
def test_actions_copy_and_paste():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    driver.maximize_window()

    f_name = driver.find_element(By.NAME, "firstname")

    l_name = driver.find_element(By.NAME, "lastname")

    actions = ActionChains(driver=driver)

    f_name.click()
    f_name.send_keys("First name")
    actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

    actions.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

    l_name.click()
    actions.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

    time.sleep(10)
