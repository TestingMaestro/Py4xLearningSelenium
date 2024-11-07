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
from selenium.webdriver.chrome.options import Options


@allure.title("Action P3- ActionChains class - mouse events")
@allure.description("Verify the Actions P3 - click and hold")
def test_actions_make_my_trip():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()
    irritating_popup = driver.find_element(By.XPATH, "//span[@class='commonModal__close']")
    WebDriverWait(driver=driver, timeout=5).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@class='commonModal__close']")))

    irritating_popup.click()
    time.sleep(5)
    from_city = driver.find_element(By.XPATH, "//input[@id='fromCity']")

    actions = ActionChains(driver=driver)

    actions.move_to_element(from_city).click(from_city).send_keys_to_element(from_city,"del").perform()
    time.sleep(5)
    actions.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_UP).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

    # move the mouse to the from city
    # click on it
    # enter DEL
    # Arrow down [up and down]
    # enter
    time.sleep(10)
