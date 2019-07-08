import logging
import os
import time
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://my.daqri.com", help="url")
    parser.addoption("--browser", action="store", default="chromium", help="browser")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture
def teardown(browser, request):
    yield
    # request.node is an "item" because we use the default
    # "function" scope
    if request.node.rep_setup.failed:
        take_screenshot(browser, request)
        print("WOWOWOWOWOWOWOOWOWOWOWOO", request.node.nodeid)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            take_screenshot(browser, request)
            print("BOOOOOOOOOOOOOOOOOOOOOOOO", request.node.nodeid)


@pytest.fixture(scope="module")
def url(request):
    return request.config.getoption("--url")

@pytest.fixture(scope="module")
def browser_type(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="module", autouse=True)
def browser(browser_type):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')

    if browser_type == "chromium":
        browser = webdriver.Remote(
            command_executor='http://chrome:4444/wd/hub', # http://chrome:4444/wd/hub
            options=options,
            desired_capabilities=DesiredCapabilities.CHROME)
    else:
        browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=options,
            desired_capabilities=DesiredCapabilities.FIREFOX)
    browser.maximize_window()
    print(browser)
    return browser

@pytest.fixture(scope="function", autouse=True)
def logging_test_name(request):
    """
    Fixture that adds the test file path and test method name to log file
    for debugging purpose
    """
    print("============Test file path - {}=============".format(request.node.fspath))
    print("============Test method name - {}============".format(request.node.name))
    # print ("HELLLOOO")
    # logging.info("============Test file path - {}=============".format(request.node.fspath))
    # logging.info("============Test method name - {}============".format(request.node.originalname))

def take_screenshot(browser, request):
    screenshots_dir = "./"
    method_name = request.node.name
    # testname = request.node.name
    screenshot_file_path = "{0}/{1}.png".format(screenshots_dir,method_name)
    browser.save_screenshot(screenshot_file_path)
