from selenium.webdriver.common.by import By

import conftest
from pages.base_page import BasePage


class DashboardScreen(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        admin_button = (By.XPATH, "//*[@class = 'oxd-text oxd-text--span oxd-main-menu-item--name' and text()= 'Admin']")
        self.admin_button = admin_button
        self.dashboard_confirm = (By.XPATH, "//*[@class = 'oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")

