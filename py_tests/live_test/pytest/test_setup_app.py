#!/usr/bin/env python3

import pytest
import helpers
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture(scope="module")
def open_url(browser,url):
    browser.set_window_size(width=1440, height=900)
    browser.get(url)
    # browser.get("https://admin:password@{0}".format(url))
    # print(browser.title)

def test_login_to_setup_app(something, logging_test_name, browser, open_url, request):
    # description = browser.find_element(By.CLASS_NAME, "summary")
    # assert "Manage your DAQRI Smart Devices. Manage your DAQRI Account." in browser.page_source
    # assert browser.title == "my.daqri.com"
    
    print( 'Running the test in '.format(str(browser.execute_script("return navigator.userAgent"))) )
    # is_visible(browser, find_element(By.CLASS_NAME, "summary"))
    # locator = browser.find_element_by_xpath("//form[input/@name='username']")
    helpers.wait_for_element_presence(element=(By.CLASS_NAME, "content"))
    print(browser.title)
    # take_screenshot(browser, request)

@pytest.mark.skip(reason="no way of currently testing this")
def test_login_to_setup_app2(something, logging_test_name, browser, open_url, request):
    # description = browser.find_element(By.CLASS_NAME, "summary")
    # assert "Manage your DAQRI Smart Devices. Manage your DAQRI Account." in browser.page_source
    # assert browser.title == "my.daqri.com"
    
    print( 'Running the test in '.format(str(browser.execute_script("return navigator.userAgent"))) )
    # is_visible(browser, find_element(By.CLASS_NAME, "summary"))
    assert 1 == 2
    print(browser.title)
    # take_screenshot(browser, request)
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

# def login(browser, username, password):


# return True if element is visible within 2 seconds, otherwise False
def is_visible(locator, browser, timeout=15):
    try:
        ui.WebDriverWait(browser, timeout).until(EC.visibility_of_element_located(locator))
        return True
    except TimeoutException:
        return False

# return True if element is not visible within 2 seconds, otherwise False
def is_not_visible(browser, locator, timeout=15):
    try:
        ui.WebDriverWait(browser, timeout).until_not(EC.visibility_of_element_located(locator))
        return True
    except TimeoutException:
        return False

def test_teardown(browser, request):
    print("I'm running teardown!!!!")
    method_name = request.node.name
    # if request.node.rep_call.failed:
    #     print('test {} failed :('.format(method_name))
    browser.close()
    browser.quit()


pytest.main()