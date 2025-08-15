import pytest
from page.page_1_web_inputs import Page1WebInputs



class BaseTest:

    web_input : Page1WebInputs

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.web_input = Page1WebInputs(driver)