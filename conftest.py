import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver



@pytest.fixture(autouse=True, scope='function')
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('start-maximized')
    options.add_argument('--headless')
    options.add_argument('incognito')
    options.page_load_strategy = 'eager'
    driver : WebDriver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
