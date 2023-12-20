from entities.my_info_screen import MyInfoScreen


class MyInfoPage(MyInfoScreen):
    my_info_screen = MyInfoScreen()

    def my_info_click(self):
        self.click(self.my_info)

    def check_my_info(self):
        self.check_if_element_exist(self.name)


