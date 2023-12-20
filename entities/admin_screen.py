from selenium.webdriver.common.by import By

import conftest
from pages.base_page import BasePage


class AdminScreen(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.add_button = (By.XPATH, "//*[@class= 'oxd-button oxd-button--medium oxd-button--secondary']")
