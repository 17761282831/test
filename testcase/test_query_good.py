from base.base_util import BaseUtil
from pageobject.query_goods import QueryGoods


class TestQueryGoods(BaseUtil):

    def test_query_goods_01(self):
        """
        查询商品
        :return:
        """
        ad = QueryGoods(self.dr)
        ad.add_to_cart()
        self.assertEqual(ad.get_except_result(), "加入购物车")