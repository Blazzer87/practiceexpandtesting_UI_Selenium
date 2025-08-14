import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

@pytest.fixture(autouse=True, scope='function')
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument('-maximized')
    driver : WebDriver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield
    driver.quit()
