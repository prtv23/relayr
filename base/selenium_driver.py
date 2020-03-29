from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import logging
import utilities.custom_logger as cl
import time
import os


class SeleniumDriver:
    log = cl.custom_log(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def take_screenshots(self, message):

        screenshots_directory = "..\screenshots\\"
        current_directory = os.path.dirname(__file__)

        # this gives the 'Name' for the screenshot file
        screenshot_filename = os.path.join(screenshots_directory, message+".png")

        # this gives the 'Path' for the screenshot file : place where screenshots are saved
        destination_filename = os.path.join(current_directory, screenshot_filename)

        # path where the screenshots directory should be available
        new_directory_path = os.path.join(current_directory, screenshots_directory)

        # in case... if the screenshots directory is deleted, the below code creates a new 'Screenshots' directory
        if not (os.path.exists(new_directory_path)):
            os.mkdir(new_directory_path)

        # take screenshot
        self.driver.save_screenshot(destination_filename)

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()

        if locator_type == 'id':
            return By.ID
        if locator_type == 'name':
            return By.NAME
        if locator_type == 'classname':
            return By.CLASS_NAME
        if locator_type == 'linktext':
            return By.LINK_TEXT
        if locator_type == 'css':
            return By.CSS_SELECTOR
        if locator_type == 'xpath':
            return By.XPATH
        else:
            self.log.info("Locator Type"+locator_type+"not correct / supported")
            # self.log.info("Locator Type"+locator_type+"not correct / supported")
            return False

    def is_element_present(self, locator_type, locator):

        _by_type = self.get_by_type(locator_type)
        element = self.driver.find_element(_by_type, locator)

        if element is not None:
            self.log.info("is_element_present : Element Found")
            return True
        else:
            self.log.info("is_element_present : Element Not Found")
            return False

    def get_element(self, locator_type, locator):

        _by_type = self.get_by_type(locator_type)
        element = self.driver.find_elements(_by_type, locator)

        if element is not None:
            self.log.info("Element Found")
        else:
            self.log.info("Element Not Found")
        return element

    def enter_data_into_text_field(self, locator_type, locator, value):

        _by_type = self.get_by_type(locator_type)
        element = self.driver.find_element(_by_type, locator)

        if element is not None:
            self.log.info("Element Found")
        else:
            self.log.info("Element Not Found")
        element.send_keys(value)

    def keyboard_enter(self, locator_type, locator, value=""):

        _by_type = self.get_by_type(locator_type)
        element = self.driver.find_element(_by_type, locator)

        if element is not None:
            self.log.info("Element Found")
            element.send_keys(value, Keys.ENTER)
            return True
        else:
            self.log.info("Element not found")
            return False

    def element_click(self, locator_type, locator):

        _by_type = self.get_by_type(locator_type)
        element = self.driver.find_element(_by_type, locator)

        if element is not None:
            self.log.info("Element Clicked")
            element.click()
        else:
            self.log.info("Element could not be clicked")

    def clear_field(self, locator_type, locator):

        _by_type = self.get_by_type(locator_type)
        try:
            element = self.driver.find_element(_by_type, locator)
            element.clear()
        except NoSuchElementException:
            self.log.info("Element was not found")

    def validate_page_title(self, verify_page_title):

        page_title = self.driver.title
        print(verify_page_title)
        print(page_title)
        if verify_page_title == page_title:
            return True
        else:
            return False

    def wait_till_element_appears(self, locator_type, locator, timeout=30, poll_frequency=.5):
        try:
            by_type = self.get_by_type(locator_type)
            wait = WebDriverWait(self.driver, timeout, poll_frequency)
            wait.until(EC.element_to_be_clickable((by_type, locator)))
        except:
            self.log.info("Element not found ... till 30 seconds timeout")

    def wait_till_circle_disappears(self, timeout=30, poll_frequency=.5):
        try:
            by_type = "xpath"
            wait = WebDriverWait(self.driver, timeout, poll_frequency)
            locator = "//div[@class='loading-wrap']/img"
            # locator = ".loading-wrap>img"
            # Checking for Loading Circle ...
            # Loading Circle found ... polling till it disappears
            wait.until(EC.invisibility_of_element_located((by_type, locator)))
        except:
            # self.log.info.error("Loading Circle found ... till 30 seconds timeout")
            self.log.info("Loading Circle found ... till 30 seconds timeout")

        return None

    def wait_till_loading_disappears(self, timeout=30, poll_frequency=.5):
        try:
            by_type = "xpath"
            wait = WebDriverWait(self.driver, timeout, poll_frequency)
            locator = "//div/*[name()='svg']/*[name()='rect']"
            # Checking for Loading interface bar ...
            # Loading Interface bar found ... polling till it disappears
            wait.until(EC.invisibility_of_element_located((by_type, locator)))
        except:
            # self.log.info.error("Loading Circle found ... till 30 seconds timeout")
            self.log.info("Loading Circle found ... till 30 seconds timeout")
        return None

    def web_scroll(self, direction="up"):

        if direction == "up":
            self.driver.execute_script("window.scrollBy(0, -1000);")
        if direction == "down":
            self.driver.execute_script("window.scrollBy(0, 1000);")