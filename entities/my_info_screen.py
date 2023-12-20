from selenium.webdriver.common.by import By

import conftest
from pages.base_page import BasePage


class MyInfoScreen(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.my_info = (By.XPATH, "//a[@href='/web/index.php/pim/viewMyDetails']")
        self.name = (By.XPATH, "//div[@class='orangehrm-edit-employee-name']")