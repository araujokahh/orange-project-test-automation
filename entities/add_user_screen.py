from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class AddUserScreen(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.user_role = (By.XPATH, "//div[@class='oxd-select-text--after']")
        self.admin = (By.XPATH, "//span[contains(text(), 'Admin')]")
        self.employee_name = (By.XPATH, "//*[@placeholder='Type for hints...']")
        self.employee_name_select = (By.XPATH, "//span[contains(text(), 'Linda Jane Anderson')]")
        self.status = (By.XPATH, "//label[text()='Status']/../following-sibling::div//i[contains(@class, 'arrow')]")
        self.enabled = (By.XPATH, "//span[contains(text(), 'Enabled')]")
        self.username = (By.XPATH, "//input[@class='oxd-input oxd-input--active'][@autocomplete='off']")
        self.password = (By.XPATH, "//input[@class='oxd-input oxd-input--active'][@type='password']")
        self.confirm_password = (By.XPATH, "//input[@class='oxd-input oxd-input--active'][@type='password']")
        self.save_button = (By.XPATH, "//button[@type='submit']")
        self.successfully_saved = (By.XPATH, "//p[text()= 'Successfully Saved']")

