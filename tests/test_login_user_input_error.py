import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from helpers import Helpers
from locators import TestLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestLoginError():


    def test_login_user_input_password_error(self):
        email = Helpers.create_random_email()
        password = str(Helpers.create_random_error_password())
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
        assert driver.find_element(*TestLocators.SEARCH_INPUT_ERROR).text == "Некорректный пароль"
        driver.quit()