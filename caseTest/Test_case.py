from HTMLTestRunnerCN import HTMLTestRunner
import unittest
import time

import requests

from caseTest.Test import appnium_start

class Case_test(unittest.TestCase):
        def test_case(self):
            self.driver = appnium_start()
            time.sleep(10)
            print('true')
            try:
                self.driver.find_element_by_id('com.shmj.xiaoxiucai:id/o8').click()
            except:
                print('false')
            time.sleep(5)
            try:
                self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
            except:
                print('false')
            time.sleep(2)
            try:
                self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
            except:
                print('false')
            time.sleep(5)
            try:
                self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
            except:
                print('false')
            time.sleep(5)
            try:

                self.driver.find_element_by_id("com.shmj.xiaoxiucai:id/ax").click()
            except:
                print("false")
            try:
                self.driver.find_element_by_id("com.shmj.xiaoxiucai:id/ek").send_keys('18720102420')
                print('true')
            except:
                print('false')
            time.sleep(2)
            try:
                self.driver.find_element_by_id("com.shmj.xiaoxiucai:id/b1").click()
                time.sleep(5)
                response = requests.get(
                    'http://test-u-hxxc.tt.cn/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=18720102420')
                key = response.json()
                print(key)
                time.sleep(10)
                self.driver.find_element_by_id("com.shmj.xiaoxiucai:id/em").send_keys(key)
                time.sleep(5)
                self.driver.find_element_by_id("com.shmj.xiaoxiucai:id/b2").click()
            except:
                print('false')
            time.sleep(10)
            self.driver.get_screenshot_as_file('E:\\陈云飞.png')  # 测试截图


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Case_test('test_case')) # 存放测试用例
    test = open('E:\\陈云飞测试报告.html', 'wb')
    runner = HTMLTestRunner(stream=test, title='陈云飞测试报告', description='测试执行描述')
    runner.run(suite)
