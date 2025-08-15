from conftest import driver

from selenium.webdriver.support.wait import WebDriverWait



class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=20)

    def open(self, url):
        self.driver.get(url=url)
