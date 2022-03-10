from typing import Union, Set, Any, FrozenSet

from ddt import ddt, data, unpack

from base.base_util import BaseUtil
from common.excel_util import ExcelUtil
from pageobject.login_page import LoginPage


@ddt
class TestLogin(BaseUtil):
        @data(*ExcelUtil().read_excel())
        @unpack
        def test_login_01(self, index, user_name, password):
            """
            输入正确的用户名和密码
            :return:
            """
            lp = LoginPage(self.dr)
            lp.login_advantech(user_name, password)
            if index == 1:
                self.assertEqual(lp.get_except_result(), "退出")
                print("git test")

