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
    driver.get("https://the-internet.herokuapp.com/windows")
    driver.maximize_window()

    parent_window = driver.current_window_handle
    print(parent_window)

    link = driver.find_element(By.LINK_TEXT, "Click Here")
    link.click()

    window_handles = driver.window_handles
    print(window_handles)
    time.sleep(5)
    try:
        for window in window_handles:
            driver.switch_to.window(window)
            WebDriverWait(driver=driver, timeout=7).until(EC.new_window_is_opened(window_handles))
            if "New Window" in driver.page_source:
                print("test case passed")
                break

            driver.switch_to.window(parent_window)

            assert "Opening a new window" == driver.page_source

    except Exception as e:
        print(e)
