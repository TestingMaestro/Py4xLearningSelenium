import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


@allure.title("Verify SVG")
@allure.description("Handling SVG")
def test_handling_svg():
    driver = webdriver.Chrome()
    driver.get("https://www.amcharts.com/svg-maps/?map=india")

    # (WebDriverWait(driver=driver, timeout=10).
    #  until(EC.visibility_of_element_located((By.NAME, "q"))))

    list_of_states = driver.find_elements(By.XPATH,
                                          "//*[local-name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*["
                                          "name()='path']")

    print(len(list_of_states))
    for states in range(len(list_of_states)):

        if "West Bengal" in list_of_states[states].get_attribute("aria-label"):
            list_of_states[states].click()
        # print(list_of_states[states].get_attribute("aria-label").strip())

    time.sleep(5)
