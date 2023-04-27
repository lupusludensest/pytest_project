import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from amazon_locators import *


class TestAmazon:
    search_words = ('dress', 'shoes', 'toys', 'shirts')
    driver = ''

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 15)
        self.driver.get('https://www.amazon.com/')

    @pytest.mark.parametrize('search_query', search_words)
    def test_amazon_search_whatever(self, search_query):
        search = self.driver.find_element( *SEARCH_FIELD)
        search.send_keys(search_query, Keys.ENTER)

        expected_text = f'\"{search_query}\"'
        actual_text = self.driver.find_element( *TEXT_FIELD).text

        assert expected_text == actual_text, f'Error.Expected text: {expected_text}, but actual text: {actual_text}'

    def teardown_method(self):
        self.driver.quit()

