from base.base_test import BaseTest
from datetime import datetime
import pytest


class Test1WebInputs(BaseTest):


    @pytest.mark.parametrize('number, text, password, date',
                             [('89507586687', 'hello', '!QAZ1qaz', '04121987')],
                             ids=['test1'])
    def test1_web_inputs(self, number, text, password, date):
        self.web_input.open(self.web_input.url)
        self.web_input.click_input_and_send_keys(input = self.web_input.input_number, text = number)
        self.web_input.click_input_and_send_keys(input = self.web_input.input_text, text = text)
        self.web_input.click_input_and_send_keys(input = self.web_input.input_password, text = password)
        self.web_input.click_input_and_send_keys(input = self.web_input.input_date, text = date)
        self.web_input.click_button(button = self.web_input.button_display_inputs)

        assert self.web_input.get_value_from_output(self.web_input.output_number) == number
        assert self.web_input.get_value_from_output(self.web_input.output_text) == text
        assert self.web_input.get_value_from_output(self.web_input.output_password) == password
        assert self.web_input.get_value_from_output(self.web_input.output_date) == datetime.strptime(date, '%d%m%Y').strftime('%Y-%m-%d')
