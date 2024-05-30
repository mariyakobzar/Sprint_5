import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from locators import TestLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestConstructionSections():

    def test_constructor_sections_ingredients(self, driver):
        #options = Options()
        #options.add_argument('--window-size=1920,1080')
        #driver = webdriver.Chrome(options=options)
        #driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.SEARCH_TAB_INGREDIENTS).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(TestLocators.SEARCH_HEADER_INGREDIENTS))
        assert driver.find_element(*TestLocators.SEARCH_HEADER_INGREDIENTS).text == "Начинки"
        #driver.quit()
    def test_constructor_sections_sauce(self, driver):
        #options = Options()
        #options.add_argument('--window-size=1920,1080')
        #driver = webdriver.Chrome(options=options)
        #driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.SEARCH_TAB_INGREDIENTS).click()
        driver.find_element(*TestLocators.SEARCH_TAB_SAUCE).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(TestLocators.SEARCH_HEADER_SAUCE))
        assert driver.find_element(*TestLocators.SEARCH_HEADER_SAUCE).text == "Соусы"
        #driver.quit()
    def test_constructor_sections_bread(self, driver):
        #options = Options()
        #options.add_argument('--window-size=1920,1080')
        #driver = webdriver.Chrome(options=options)
        #driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.SEARCH_TAB_INGREDIENTS).click()
        driver.find_element(*TestLocators.SEARCH_TAB_BREAD).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(TestLocators.SEARCH_HEADER_BREAD))
        assert driver.find_element(*TestLocators.SEARCH_HEADER_BREAD).text == "Булки"
        #driver.quit()