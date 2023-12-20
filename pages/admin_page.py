from entities.admin_screen import AdminScreen


class AdminPage(AdminScreen):
    admin_screen = AdminScreen()

    def click_add(self):
        self.click(self.add_button)

