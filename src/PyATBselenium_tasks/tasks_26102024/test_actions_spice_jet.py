import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure


@allure.title("ActionChains class - drag_and drop")
@allure.description("Verify the Actions P3 - drag_drop")
def test_actions_drag_and_drop():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://www.spicejet.com/")
    driver.maximize_window()

    from_city = driver.find_element(By.XPATH, "//input[@value='Delhi (DEL)']")
    actions = ActionChains(driver=driver)

    WebDriverWait(driver=driver, timeout=6).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@value='Delhi (DEL)']")))
    time.sleep(5)

    actions.move_to_element(from_city).click(from_city)
    actions.send_keys_to_element(from_city, "mum").perform()
