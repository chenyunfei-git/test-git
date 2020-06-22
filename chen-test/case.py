import unittest
from HTMLTestRunnerCN import HTMLTestRunner
from asyncio import sleep


class TestCase(unittest.TestCase):
    def test_case(self):
        sleep(120)  # 以秒为单位
        self.driver.find_element_by_id('com.tencent.mobileqq:id/btn_login').click()  # 点击登录
        sleep(60)  # 以秒为单位
        self.driver.find_element_by_class_name("android.widget.TextView").click()
        sleep(30)  # 以秒为单位
        self.driver.find_element_by_class_name('android.widget.EditText').send_keys("1292394137")  # 输入QQ号
        self.driver.find_element_by_id('com.tencent.mobileqq:id/password').send_keys("SJN1020..")  # 输入密码
        self.driver.find_element_by_id('com.tencent.mobileqq:id/login').click()  # 点击登录
        self.driver.find_element_by_id('com.tencent.mobileqq:id/dialogRightBtn').click()  # 点击同意
        sleep(60)  # 以秒为单位
        self.driver.find_element_by_id('com.tencent.mobileqq:id/login').click()  # 点击登录
        sleep(180)  # 以秒为单位
        self.driver.find_element_by_id('com.tencent.mobileqq:id/ba3').click()  # 点击+号
        sleep(30)  # 以秒为单位
        self.driver.find_element_by_id('com.tencent.mobileqq:string/adp').click()  # 点击加好友/群
        sleep(60)  # 以秒为单位
        self.driver.find_element_by_id('com.tencent.mobileqq:id/bz0').click()  # 点击输入框
        sleep(60)  # 以秒为单位
        self.driver.find_element_by_id('com.tencent.mobileqq:id/et_search_keyword').send_keys("1292394137")  # 输入QQ号
        sleep(60)  # 以秒为单位
        self.driver.find_element_by_id('com.tencent.mobileqq:id/czn').click()  # 点击找人

    def runTest(self):
        pass

    if __name__ == '__main__':
       suite = unittest.TestSuite()
       suite.addTest(test_case)  # 存放测试用例
       fg = open('./result.html', 'wb')
       runner = HTMLTestRunner(stream=fg, title='陈云飞测试报告', description='测试执行描述')
       runner.run(suite)






