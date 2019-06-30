#!/usr/bin/env python3

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture(scope="module")
def open_url(browser,url):
    browser.get(url)
    # description = browser.find_element(By.CLASS_NAME, "summary")
    # assert "Manage your DAQRI Smart Devices. Manage your DAQRI Account." in browser.page_source
    # assert browser.title == "my.daqri.com"
    print(browser.title)

def test_add_todo(browser, open_url):
    description = browser.find_element(By.CLASS_NAME, "summary")
    assert "Manage your DAQRI Smart Devices. Manage your DAQRI Account." in browser.page_source
    assert browser.title == "my.daqri.com"
    print( 'Running the test in ' + str(browser.execute_script("return navigator.userAgent")) )
    print(browser.title)

    
    # todoText = "Add to do item 1 by PYTEST"
    # newItemAdded = False
    # originItemsCount = len(chrome.find_elements(By.XPATH, '//*[@class="todo"]'))
    # chrome.find_element_by_name('addToDo').send_keys(todoText)
    # chrome.find_element_by_name('addToDo').send_keys(Keys.ENTER)
    # updatedList = chrome.find_elements(By.XPATH, '//*[@class="todo"]')
    # assert len(updatedList) == originItemsCount+1
    # for item in updatedList:
    #     if item.text.find(todoText):
    #         newItemAdded = True

    # assert newItemAdded == True

# def test_complete_todo(chrome, open_url):
#     chrome.find_element_by_name('btnComplete').click()
#     assert chrome.find_element(By.XPATH, '//*[@class="todo"]').get_attribute('style') == 'text-decoration: line-through;'

# def test_remove_todo(chrome, open_url):
#     originItemsCount = len(chrome.find_elements(By.XPATH, '//*[@class="todo"]'))
#     chrome.find_element_by_name('btnDelete').click()
#     newItemCount = len(chrome.find_elements(By.XPATH, '//*[@class="todo"]'))
#     assert newItemCount == originItemsCount-1

def test_teardown(browser):
    browser.close()
    browser.quit()
