import unittest
from HTMLTestRunnerCN import HTMLTestRunner
from datetime import time

from appium.webdriver import webdriver


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
        time.sleep(120)
        self.driver.find_element_by_id('com.tencent.mobileqq:id/btn_login').click()  #点击登录
        time.sleep(60)
        self.driver.find_element_by_class_name("android.widget.TextView").click()
        time.sleep(30)
        self.driver.find_element_by_class_name('android.widget.EditText').send_keys("1292394137")  #输入QQ号17159295
        time.sleep(15)
        self.driver.find_element_by_id('com.tencent.mobileqq:id/password').send_keys("SJN1020..")  #输入密码
        time.sleep(15)
        self.driver.find_element_by_id('com.tencent.mobileqq:id/login').click()  #点击登录
        time.sleep(15)
        self.driver.find_element_by_id('com.tencent.mobileqq:id/dialogRightBtn').click()  #点击同意
        time.sleep(60)
        self.driver.find_element_by_id('com.tencent.mobileqq:id/login').click()  #点击登录
        time.sleep(30)
        self.driver.find_element_by_xpath("//*[@text='动态']").click()
        time.sleep(30)
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.mobileqq:id/ibc']").click()  #进入空间
        time.sleep(60)
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.mobileqq:id/dq7'][@text='相册']").click()  #进入相册
        time.sleep(60)
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.mobileqq:id/bij']").click()  #关闭提示框
        time.sleep(60)
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.mobileqq:id/der']").click()   #添加照片
        time.sleep(60)
        self.driver.find_element_by_xpath("//*[@text='拍摄']").click()  #点击拍摄文字
        self.driver.get_screenshot_as_file('E:\\陈云飞.png')  # 测试截图


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(ContactsAndroidTests("test_chen"))  # 存放测试用例
    fg = open('E:\\陈云飞测试报告.html', 'wb')
    runner = HTMLTestRunner(stream=fg, title='陈云飞测试报告', description='测试执行描述')
    runner.run(suite)