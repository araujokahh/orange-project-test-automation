from entities.dashboard_screen import DashboardScreen


class DashboardPage(DashboardScreen):
    dashboard_screen = DashboardScreen()

    def check_successfull_login(self):
        self.check_if_element_exist(self.dashboard_confirm)

    def click_admin(self):
        self.click(self.admin_button)

