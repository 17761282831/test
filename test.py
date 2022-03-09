import unittest
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    """
    执行需要的用例并生成测试报告
    """
    # 使用unittest默认的测试用例加载器，去发现testcase目录下，以.py结尾测试用例
    suit = unittest.defaultTestLoader.discover("./testcase", "*.py")
    # 生成报告文件reports.html并存放至report目录下
    report_file = open("./report/reports.html", "wb")
    # 生成HTMLTestRunner运行器对象，并将执行结果存放至报告文件report_file中（HTMLTestRunner需要下载）
    runner = HTMLTestRunner(stream=report_file, verbosity=1, title="Advantech", description="执行结果如下")
    # 执行测试用例
    runner.run(suit)