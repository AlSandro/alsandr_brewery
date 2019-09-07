
"""
Class for WebDriver waiter method
"""
import logging
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def wait_for_element(element, driver, delay):
    """
      Waits for element to be present
      :param element: Web Element
      :param driver: WebDriver
      :param delay: waiting time
    """
    try:
        my_elem = WebDriverWait(driver, delay).until(ec.visibility_of_element_located(element))
        logging.info("Page is ready!")
    except TimeoutException:
        logging.info("Loading took too much time!")
        assert False, "Element in program did not load in time or did not show"
    return my_elem


def wait_for_element_presence(element, driver, delay=15):
    """
      Waits for element to be present
      :param element: Web Element
      :param driver: WebDriver
      :param delay: waiting time
    """
    try:
        my_elem = WebDriverWait(driver, delay).until(ec.presence_of_element_located(element))
        logging.info("Page is ready!")
    except TimeoutException:
        logging.info("Loading took too much time!")
        assert False, "Element in program did not load in time or did not show"
    return my_elem


def wait_until_element_is_not_visible(element, driver, delay=15):
    """
      Waits for element to be not visible anymore
      :param element: Web Element
      :param driver: WebDriver
      :param delay: waiting time
    """
    try:
        my_elem = WebDriverWait(driver, delay).until(ec.invisibility_of_element_located(element))
        logging.info("Element is hidden!")
    except TimeoutException:
        logging.info("It took too much time to disappear!")
        assert False, "Element is still visible"
    return my_elem


def take_screenshot(browser, test_name):
	screenshots_dir = "./"
	screenshot_file_path = "{}/{}.png".format(screenshots_dir, test_name)
	browser.save_screenshot(screenshot_file_path)