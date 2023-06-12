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

def test_002_fb_wrong_credentials(environment_setup):
    # Locators
    LOGIN = (By.XPATH, "//input[@type='text']")
    PSWRD = (By.XPATH, "//input[@type='password']")
    LGN_BTN = (By.XPATH, "//button[@name='login']")
    INCRRT_HR = (By.XPATH, "//a[@class='_42ft _4jy0 _al4m _4jy6 _517h _51sy']")

    # Explicit wait
    wait = WebDriverWait(driver, 15)

    # 2. Send wrong login
    wait.until(EC.presence_of_element_located(LOGIN)).clear()
    wait.until(EC.presence_of_element_located(LOGIN)).send_keys('wrong@wrong.com')

    # 3. Send wrong password
    wait.until(EC.presence_of_element_located(PSWRD)).clear()
    wait.until(EC.presence_of_element_located(PSWRD)).send_keys('wrong_pswd')

    # 4. Click on login button
    wait.until(EC.element_to_be_clickable(LGN_BTN)).click()

    # 5. Verify "Try another way" text is here
    searhed = ('Try another way')
    actual = (wait.until(EC.presence_of_element_located(INCRRT_HR)).text)
    print(f'Actual: "{actual}"\nVS expected:\n"{searhed}"')
    assert searhed in actual
    if searhed in actual:
        print(f'Actual is OK:\n"{searhed}"\n')
    else:
        print(f'Actual email: "{actual}"\n')