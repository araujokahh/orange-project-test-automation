
from entities.login_screen import LoginScreen


class LoginPage(LoginScreen):
    login_screen = LoginScreen()

    def login(self, username, password):
        self.write(self.username_field, username)
        self.write(self.password_field, password)
        self.click(self.login_button)







