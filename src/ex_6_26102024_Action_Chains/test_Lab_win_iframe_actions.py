import time

import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton


@allure.title("Combined_ Window_actions_iframes")
@allure.description("Combined_ Window_actions_iframes")
def test_complex_sc1():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(chrome_options)
    driver.maximize_window()
    driver.get(
        "https://app.vwo.com/#/test/ab/13/heatmaps/1?token"
        "=eyJhY2NvdW50X2lkIjo2NjY0MDAsImV4cGVyaW1lbnRfaWQiOjEzLCJjcmVhdGVkX29uIjoxNjcxMjA1MDUwLCJ0eXBlIjoiY2FtcGFpZ24iLCJ2ZXJzaW9uIjoxLCJoYXNoIjoiY2IwNzBiYTc5MDM1MDI2N2QxNTM5MTBhZDE1MGU1YTUiLCJzY29wZSI6IiIsImZybiI6ZmFsc2V9&isHttpsOnly=1")

    main_window_handle = driver.current_window_handle

    my_list = driver.find_elements(By.CSS_SELECTOR, "[data-qa=danawobuqa]")

    variation = my_list[1]

    actions = ActionChains(driver=driver)
    actions.click(variation).perform()

    time.sleep(15)

    all_handles = driver.window_handles

    for handle in all_handles:
        if handle != main_window_handle:
            driver.switch_to.window(handle)
            # child window
            print(driver.title)
            # iframe by id
            # WebDriverWait(driver=driver, timeout=30).until(
            #     EC.frame_to_be_available_and_switch_to_it("heatmap-iframe"))
            driver.switch_to.frame("heatmap-iframe")

            click_map = driver.find_element(By.XPATH,
                                            "//span[text()='Clickmap']/parent::div/parent::div/div[last()]/span")

            click_map.click()
            time.sleep(30)

        ''' WebDriverWait(driver=driver, timeout=20).until(EC.element_to_be_clickable((By.XPATH,
                                                                                    "//span[text("
                                                                                    ")='Clickmap']/parent"
                                                                                    "::div/parent::div/div["
                                                                                    "last()]/span")))'''
    time.sleep(30)
