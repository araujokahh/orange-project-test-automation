from entities.add_user_screen import AddUserScreen


class AddUserPage(AddUserScreen):
    add_user_screen = AddUserScreen()

    def user_role_field(self):
        self.click(self.user_role)
        self.click(self.admin)

    def employee_name_field(self, name):
        self.write(self.employee_name, name), self.wait(10)
        self.click(self.employee_name_select)

    def status_field(self):
        self.click(self.status)
        self.click(self.enabled)

    def username_field(self, username):
        self.write(self.username, username)

    def password_field(self, password, confirm_password):
        self.write(self.password, password)
        self.write(self.confirm_password, confirm_password)

    def save_button_submit(self):
        self.click(self.save_button)

    def check_successfully_saved(self):
        self.check_if_element_exist(self.successfully_saved)