from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


class BasePage:
    def __init__(self, dr):
        self.dr = dr

    # 定位元素的关键字
    def locator_element(self, loc):
        return self.dr.find_element(*loc)

    # 设置值的关键字
    def send_keys(self, lco, value):
        self.locator_element(lco).send_keys(value)

    # 点击的关键字
    def click(self, loc):
        self.locator_element(loc).click()

    # 进入框架的关键字
    def goto_frame(self, frame_name):
        self.dr.switch_to.frame(frame_name)

    # 出框架的关键字
    def quit_frame(self):
        self.dr.switch_to.default_content()

    # 封装选中下拉框的关键字
    def choice_select(self, loc, value):
        sel = Select(self.locator_element(loc))
        sel.select_by_visible_text(value)

    def wait(self, sec):
        print("I`m waiting")
        self.dr.implicitly_wait(sec)

    # 鼠标悬浮
    def move_to(self, loc):
        target = self.locator_element(loc)
        ActionChains(self.dr).move_to_element(target).perform()

    # 获取文本的值
    def get_value(self, loc):
        return self.locator_element(loc).text


class Xiaohuhaoniu:
    def just_test(self):
        print("this is a test word")



