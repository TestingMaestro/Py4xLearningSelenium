import time

import pytest
import allure
from selenium.webdriver.common.by import By
from selenium import webdriver


@allure.title("Verify the serch and get all titles")
@allure.description("Verify the serch and get all titles")
def test_ebay_come(browser_options):
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/")

    time.sleep(5)
    search_box = driver.find_element(By.XPATH, "//input[@placeholder='Search for anything']")
    search_box.send_keys("Asus")
    time.sleep(5)
    search_btn = driver.find_element(By.XPATH, "//input[@value='Search']")
    search_btn.click()
    time.sleep(5)
    all_titles = driver.find_elements(By.XPATH, "//div[@class='s-item__title']")
    print(len(all_titles))
    all_prices = driver.find_elements(By.XPATH, "//span[@class='s-item__price']")
    print(len(all_prices))

    titles = []
    prices = []

    for items, i in zip(all_titles, all_prices):
        titles.append(items.text)
        text_price = i.text.replace('$', '').replace(',', '')
        try:
            prices.append(float(text_price))
            print(f"{items.text} : {i.text}")
        except ValueError as e:
            continue

    min_price = min(prices)
    max_price = max(prices)

    print(f"Minimum Price:${min_price}")
    print(f"Maximum Price:${max_price}")
    # ele = len(all_titles[0].text)
    # my_list = []
    # my_list = my_list.extend([ele])
    # print(my_list)
    # print(ele)
    # for items in range(len(all_titles)):
    #     text = all_titles[items].text
    #     if text is None:
    #         pass
    #     else:
    #         print(all_titles[items].text)
