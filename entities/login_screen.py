from selenium.webdriver.common.by import By

import conftest
from pages.base_page import BasePage


class LoginScreen(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.username_field = (By.XPATH, "//*[@name = 'username']")
        self.password_field = (By.XPATH, "//*[@name = 'password']")
        self.login_button = (By.XPATH, "//*[@type = 'submit']")
        self.error_login = (By.XPATH, "//*[@class= 'oxd-text oxd-text--p oxd-alert-content-text']")
