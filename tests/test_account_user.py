import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from helpers import Helpers
from locators import TestLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestAccountEntrance():

    def test_account_entrance(self):
        email = Helpers.create_random_email()
        password = str(Helpers.create_random_password())
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
            expected_conditions.presence_of_element_located(TestLocators.SEARCH_HEADER_ENTRANCE))
        driver.find_element(*TestLocators.SEARCH_EMAIL_ENTRANCE).send_keys(email)
        driver.find_element(*TestLocators.SEARCH_PASSWORD_ENTRANCE).send_keys(password)
        driver.find_element(*TestLocators.SEARCH_ENTER).click()
        driver.find_element(*TestLocators.SEARCH_LOGO).click()
        driver.find_element(*TestLocators.SEARCH_ACCOUNT).click()
        assert driver.find_element(*TestLocators.SEARCH_PROFILE).text == "Профиль"
        driver.quit()