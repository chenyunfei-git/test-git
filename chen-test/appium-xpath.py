#!urs/bin/python
#!_*_ coding:UTF-8 _*_

from appium import webdriver


if __name__ == '__main__':
    desired_caps = {
        'platformName': 'Android',
        'deviceName': '127.0.0.1:62001',
        'platformVersion': '5.1.1',
        'appPackage': 'com.tencent.mobileqq',
        'appActivity': '.activity.LoginActivity'
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

driver.implicitly_wait(120)  #以秒为单位
driver.find_element_by_id('com.tencent.mobileqq:id/btn_login').click()  #点击登录
driver.implicitly_wait(60)  #以秒为单位
driver.find_element_by_class_name("android.widget.TextView").click()
driver.implicitly_wait(30)  #以秒为单位
driver.find_element_by_class_name('android.widget.EditText').send_keys("1292394137")  #输入QQ号
driver.implicitly_wait(15)  #以秒为单位
driver.find_element_by_id('com.tencent.mobileqq:id/password').send_keys("SJN1020..")  #输入密码
driver.implicitly_wait(15)  #以秒为单位
driver.find_element_by_id('com.tencent.mobileqq:id/login').click()  #点击登录
driver.implicitly_wait(15)  #以秒为单位
driver.find_element_by_id('com.tencent.mobileqq:id/dialogRightBtn').click()  #点击同意
driver.implicitly_wait(60)  #以秒为单位
driver.find_element_by_id('com.tencent.mobileqq:id/login').click()  #点击登录
driver.implicitly_wait(30)  #以秒为单位
driver.find_element_by_xpath("//*[@text='动态']").click()
driver.implicitly_wait(30)  #以秒为单位
driver.find_element_by_xpath("//*[@resource-id='com.tencent.mobileqq:id/ibc']").click()  #进入空间
driver.implicitly_wait(60)  #以秒为单位
driver.find_element_by_xpath("//*[@resource-id='com.tencent.mobileqq:id/dq7'][@text='相册']").click()  #进入相册
driver.implicitly_wait(60)  #以秒为单位
driver.find_element_by_xpath("//*[@resource-id='com.tencent.mobileqq:id/bij']").click()  #关闭提示框
driver.implicitly_wait(60)  #以秒为单位
driver.find_element_by_xpath("//*[@resource-id='com.tencent.mobileqq:id/der']").click()   #添加照片
driver.implicitly_wait(60)  #以秒为单位
driver.find_element_by_xpath("//*[@text='拍摄']").click()  #点击拍摄文字








