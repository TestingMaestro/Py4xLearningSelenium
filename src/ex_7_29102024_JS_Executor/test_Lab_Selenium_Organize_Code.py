import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton


class TestJsExecutor:
    def __init__(self):
        self.driver = None

    def open_browser(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://selectorshub.com/xpath-practice-page")

    def test_js_p3(self, driver):
        title = self.driver.execute_script("return document.title")
        URL = self.driver.execute_script("return document.URL")
        print("\n", title)
        print(URL)

        time.sleep(5)


test = TestJsExecutor()
test.open_browser()
test.test_actions_p3(webdriver)
