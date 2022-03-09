import unittest

from selenium import webdriver


class BaseUtil(unittest.TestCase):

    def setUp(self) -> None:
        global dr
        self.dr = webdriver.Chrome()
        dr = self.dr
        self. dr.maximize_window()
        # 打开研华
        self.dr.get('https://iotmart.advantech.com.cn')

    def tearDown(self) -> None:
        self.dr.quit()