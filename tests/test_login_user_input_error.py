import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from locators import TestLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestLoginError():
    def create_random_password(self):
        password = random.randint(0, 99999)
        return password
    def create_random_email(self):
        number = random.randint(000000, 999999)
        email = f'mariakobzar_{number}@gmail.com'
        return email

    def test_login_user_input_password_error(self):
        email = self.create_random_email()
        password = str(self.create_random_password())
        options = Options()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=options)
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.SEARCH_ACCOUNT).click()
        driver.find_element(*TestLocators.SEARCH_REGISTRATION).click()
        driver.find_element(*TestLocators.SEARCH_NAME).send_keys('Maria')
        driver.find_element(*TestLocators.SEARCH_EMAIL).send_keys(email)
        driver.find_element(*TestLocators.SEARCH_PASSWORD).send_keys(password)
        driver.find_element(*TestLocators.SEARCH_BUTTON_REGISTER).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(TestLocators.SEARCH_INPUT_ERROR))
        driver.quit()