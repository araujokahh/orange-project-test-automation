from selenium.webdriver.common.by import By

import conftest
from pages.base_page import BasePage


class LogoutScreen(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.menu_picture = (By.XPATH, "//img[contains(@alt, 'profile picture')]")
        self.logout = (By.XPATH, "//a[contains(@href, '/web/index.php/auth/logout')]")


