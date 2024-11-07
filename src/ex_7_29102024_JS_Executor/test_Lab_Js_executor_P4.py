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


@allure.title("Action P3- ActionChains class - mouse events")
@allure.description("Verify the Actions P3 - click and hold")
def test_shadow_dom_():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.maximize_window()
    driver.get("https://selectorshub.com/xpath-practice-page")

    user_name = driver.find_element(By.XPATH, "//div[@id='userName']")

    driver.execute_script("arguments[0].scrollIntoView(true);", user_name)

    WebDriverWait(driver=driver,timeout=15).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='userName']")))
    input_box = driver.execute_script(
        "return document.querySelector('div#userName').shadowRoot.querySelector('#app2').shadowRoot.querySelector('#pizza')")
    input_box.send_keys("farmhouse")
    time.sleep(15)
