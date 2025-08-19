
from conftest import driver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=20)


    def open(self, url):
        self.driver.get(url=url)


    def click_button(self, button):
        self.wait.until(EC.element_to_be_clickable(button)).click()


    def click_input_and_send_keys(self, locator, text):
        self.wait.until(EC.element_to_be_clickable(locator)).send_keys(text)