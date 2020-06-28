#!urs/bin/python
#!_*_ coding:UTF-8 _*_
import unittest
import time
from HTMLTestRunnerCN import HTMLTestRunner

from appium import webdriver


class ContactsAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': '127.0.0.1:62001',
            'platformVersion': '5.1.1',
            'appPackage': 'com.songheng.eastnews',
            'appActivity': 'com.oa.eastfirst.activity.MainActivity'
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def test_Demo(self):
        time.sleep(3)
        self.driver.find_element_by_id('com.songheng.eastnews:id/rb_bottom_mine').click()
        time.sleep(3)
        self.driver.find_element_by_id('com.songheng.eastnews:id/rb_bottom_search').click()
        self.driver.find_element_by_id('com.songheng.eastnews:id/edit_search').send_keys("特朗普")
        self.driver.find_element_by_id('com.songheng.eastnews:id/btn_search').click()
        time.sleep(10)
        self.driver.get_screenshot_as_file('E:\\陈云飞.png')  # 测试截图


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(ContactsAndroidTests("test_Demo"))  # 存放测试用例
    fg = open('E:\\陈云飞测试报告.html', 'wb')
    runner = HTMLTestRunner(stream=fg, title='陈云飞测试报告', description='测试执行描述')
    runner.run(suite)