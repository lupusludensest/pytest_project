from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pytest

@pytest.fixture()
def environment_setup():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    # 1. Open the url
    driver.get( 'https://www.facebook.com/' )
    yield
    # Sleep to see what we have
    sleep(4)
    # Driver close
    driver.close()
    # Driver quit
    driver.quit()

def test_facebook_login_till_market_place(environment_setup):
    # Locators
    TEXT_HERE_1 = (By.XPATH, "//h2[@class='_8eso']")
    LOGIN_FLD = (By.ID, "email")
    PASSWORD_FLD = (By.ID, "pass")
    LGN_BTN = (By.NAME, "login")
    TEXT_HERE_2 = (By.XPATH, "(//span[@class='x1lliihq x6ikm8r x10wlt62 x1n2onr6'])[1]")
    TEXT_HERE_3 = (By.XPATH, "(//span[@class='x1lliihq x6ikm8r x10wlt62 x1n2onr6'])[5]")
    LOGIN = 'gurovvic@gmail.com'
    PASSWORD = 'MyUSA2023!@'

    # Explicit wait
    wait = WebDriverWait(driver, 15)

    # 2. Verify text "Connect with friends and the world around you on Facebook." is here
    expected_text = 'Connect with friends and the world around you on Facebook.'
    actual_text = wait.until(EC.presence_of_element_located(TEXT_HERE_1)).text
    assert expected_text in actual_text
    print(f'Expected "{expected_text}", and got: "{actual_text}"\n ')

    # 3. Send correct login 'gurovvic@gmail.com'
    wait.until(EC.presence_of_element_located(LOGIN_FLD)).clear()
    wait.until(EC.presence_of_element_located(LOGIN_FLD)).send_keys(LOGIN)

    # 4. Send correct password 'MyUSA2023!@'
    wait.until(EC.presence_of_element_located(PASSWORD_FLD)).clear()
    wait.until(EC.presence_of_element_located(PASSWORD_FLD)).send_keys(PASSWORD)

    # 5. Click on Log In button
    wait.until(EC.element_to_be_clickable(LGN_BTN)).click()

    # 6. Verify text "Gurov Vic" is here
    expected_text = 'Gurov Vic'
    actual_text = wait.until(EC.presence_of_element_located(TEXT_HERE_2)).text
    assert expected_text in actual_text
    print(f'Expected "{expected_text}", and got: "{actual_text}"\n ')

    # 7. Verify text "Marketplace" is here
    expected_text = 'Marketplace'
    actual_text = wait.until(EC.presence_of_element_located(TEXT_HERE_3)).text
    assert expected_text in actual_text
    print(f'Expected "{expected_text}", and got: "{actual_text}"\n ')

