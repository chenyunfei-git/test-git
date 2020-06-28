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
            'appPackage': 'com.tencent.mobileqq',
            'appActivity': '.activity.LoginActivity'
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def test_chen(self):
        time.sleep(30)  # 以秒为单位
        self.driver.find_element_by_id('com.tencent.mobileqq:id/btn_login').click()  # 点击登录
        time.sleep(30)  # 以秒为单位
        self.driver.find_element_by_class_name("android.widget.TextView").click()
        time.sleep(30)  # 以秒为单位
        self.driver.find_element_by_class_name('android.widget.EditText').send_keys("1292394137")  # 输入QQ号
        self.driver.find_element_by_id('com.tencent.mobileqq:id/password').send_keys("SJN1020..")  # 输入密码
        self.driver.find_element_by_id('com.tencent.mobileqq:id/login').click()  # 点击登录
        self.driver.find_element_by_id('com.tencent.mobileqq:id/dialogRightBtn').click()  # 点击同意
        time.sleep(30)  # 以秒为单位
        self.driver.find_element_by_id('com.tencent.mobileqq:id/login').click()  # 点击登录
        time.sleep(30)  # 以秒为单位
        self.driver.find_element_by_id('com.tencent.mobileqq:id/ba3').click()  # 点击+号
        time.sleep(30)  # 以秒为单位
        self.driver.find_element_by_id('com.tencent.mobileqq:string/adp').click()  # 点击加好友/群
        time.sleep(30)  # 以秒为单位
        self.driver.find_element_by_id('com.tencent.mobileqq:id/bz0').click()  # 点击输入框
        time.sleep(30)  # 以秒为单位
        self.driver.find_element_by_id('com.tencent.mobileqq:id/et_search_keyword').send_keys("1292394137")  # 输入QQ号
        time.sleep(30)  # 以秒为单位
        self.driver.find_element_by_id('com.tencent.mobileqq:id/czn').click()  # 点击找人

        self.driver.get_screenshot_as_file('E:\\陈云飞.png')  # 测试截图


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(ContactsAndroidTests("test_chen"))  # 存放测试用例
    fg = open('./result.html', 'wb')
    runner = HTMLTestRunner(stream=fg, title='陈云飞测试报告', description='测试执行描述')
    runner.run(suite)