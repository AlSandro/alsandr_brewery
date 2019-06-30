import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://my.daqri.com", help="url")
    parser.addoption("--browser", action="store", default="chromium", help="browser")

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

    print(browser)
    return browser

