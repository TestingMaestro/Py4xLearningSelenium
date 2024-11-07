import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import allure


@allure.title("ActionChains class - drag_and drop")
@allure.description("Verify the Actions P3 - drag_drop")
def test_actions_drag_and_drop():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    driver.maximize_window()

    element_to_drag = driver.find_element(By.XPATH, "//div[@id='draggable']")
    element_to_drop = driver.find_element(By.XPATH,"//div[@id='droppable']")

    actions = ActionChains(driver=driver)
    actions.drag_and_drop(element_to_drag,element_to_drop).perform()

    drop_msg = driver.find_element(By.XPATH,"//strong[text()='dropped']")
    message = drop_msg.text
    print(message)

    assert message == "dropped", f"expected -> drop message, found {message}"
    time.sleep(10)


