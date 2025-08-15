from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

from links.links import Links


class Page1WebInputs(BasePage):

    url = Links.web_inputs

    button_display_inputs = ('xpath', '//button[@id="btn-display-inputs"]')
    button_clear_inputs = ('xpath', '//button[@id="btn-clear-inputs"]')

    input_number = ('xpath', '//input[@id="input-number"]')
    input_text = ('xpath', '//input[@id="input-text"]')
    input_password = ('xpath', '//input[@id="input-password"]')
    input_date = ('xpath', '//input[@id="input-date"]')

    output_number = ('xpath', '//strong[@id="output-number"]')
    output_text = ('xpath', '//strong[@id="output-text"]')
    output_password = ('xpath', '//strong[@id="output-password"]')
    output_date = ('xpath', '//strong[@id="output-date"]')


    def click_button(self, button):
        self.wait.until(EC.element_to_be_clickable(button)).click()

    def click_input_and_send_keys(self, input, text):
        self.wait.until(EC.element_to_be_clickable(input)).send_keys(text)

    def get_value_from_output(self, output):
        value = self.wait.until(EC.visibility_of_element_located(output)).text
        return value





