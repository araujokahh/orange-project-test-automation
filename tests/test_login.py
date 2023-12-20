import pytest

from pages.add_user_page import AddUserPage
from pages.admin_page import AdminPage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from pages.my_info_page import MyInfoPage


@pytest.mark.usefixtures("setup_teardown")
class TestLogin:
    def test_login(self):
        login_page = LoginPage()
        dashboard_page = DashboardPage()
        admin_page = AdminPage()
        add_user_page = AddUserPage()
        logout_page = LogoutPage()
        my_info_page = MyInfoPage()

        username_idea = "Linda.Jane.Anderson"
        password_1 = "MyPass@123"
        password_2 = "MyPass@123"

        login_page.login("Admin", "admin123")
        dashboard_page.check_successfull_login()

        dashboard_page.click_admin()

        admin_page.click_add()

        add_user_page.user_role_field()
        add_user_page.employee_name_field("a")
        add_user_page.status_field()
        add_user_page.username_field(username_idea)
        add_user_page.password_field(password_1, password_2)
        add_user_page.save_button_submit()
        add_user_page.check_successfully_saved()

        logout_page.do_logout()

        login_page.login(username_idea, password_1)
        dashboard_page.check_successfull_login()

        my_info_page.my_info_click()
        my_info_page.check_my_info()
