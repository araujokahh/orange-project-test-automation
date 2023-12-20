from entities.logout_screen import LogoutScreen


class LogoutPage(LogoutScreen):
    logout_screen = LogoutScreen()

    def do_logout(self):
        self.click(self.menu_picture)
        self.click(self.logout)


