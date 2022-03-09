from time import sleep
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from pageobject.login_page import LoginPage


class QueryGoods(BasePage):
    # 页面元素
    online_order = (By.LINK_TEXT, "在线购买")
    classification = (By.NAME, "ctl00$MainContent$ctl00$ddlTopCategory")
    query = (By.ID, "tbxKeyword")
    query_button = (By.ID, "btnHeadSearch")
    add_link = (By.LINK_TEXT, "加入购物车")

    # 页面操作
    def add_to_cart(self, classification="全部分类", trade_name="AIMB-203G2-00A1E"):
        login = LoginPage(self.dr)
        login.login_advantech()
        self.wait(10)
        self.choice_select(QueryGoods.classification, classification)
        self.send_keys(QueryGoods.query, trade_name)
        self.wait(10)
        self.click(QueryGoods.query_button)

    def get_except_result(self):
        return self.get_value(QueryGoods.add_link)
