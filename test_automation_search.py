import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestAmazon:
    search_words = ('dress', 'shoes', 'toys', 'dress')

    driver = ''

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get('https://www.amazon.com/')

    @pytest.mark.parametrize('search_query', search_words)
    def test_amazon_search_dress(self, search_query):
        search = self.driver.find_element(By.ID, 'twotabsearchtextbox')
        search.send_keys(search_query, Keys.ENTER)

        expected_text = f'\"{search_query}\"'
        actual_text = self.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text

        assert expected_text == actual_text, f'Error.Expected text: {expected_text}, but actual text: {actual_text}'

    def teardown_method(self):
        self.driver.quit()

