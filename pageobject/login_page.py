from time import sleep

from selenium.webdriver.common.by import By

from base.base_page import BasePage


class LoginPage(BasePage):
    # 页面的元素
    login_link = (By.LINK_TEXT, "会员登入")
    user_name = (By.ID, "Header_HeadLoginView_UserLogin1_LoginUser_UserName")
    password = (By.ID, "Header_HeadLoginView_UserLogin1_LoginUser_Password")
    submit = (By.ID, "LoginButton")
    my_account = (By.XPATH, "//i[@class='far fa-user']")
    quit_link = (By.LINK_TEXT, "退出")

    # 页面的操作
    def login_advantech(self, username="2548746714@qq.com", password="Galax@123"):
        self.click(LoginPage.login_link)
        self.wait(10)
        self.send_keys(LoginPage.user_name, username)
        self.send_keys(LoginPage.password, password)
        self.click(LoginPage.submit)

    # 断言
    def get_except_result(self):
        self.move_to(LoginPage.my_account)
        self.wait(10)
        return self.get_value(LoginPage.quit_link)