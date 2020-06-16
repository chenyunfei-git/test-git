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
driver.find_element_by_id('com.tencent.mobileqq:id/password').send_keys("SJN1020..")  #输入密码
driver.find_element_by_id('com.tencent.mobileqq:id/login').click()  #点击登录
driver.find_element_by_id('com.tencent.mobileqq:id/dialogRightBtn').click()  #点击同意
driver.implicitly_wait(60)  #以秒为单位
driver.find_element_by_id('com.tencent.mobileqq:id/login').click()  #点击登录
driver.implicitly_wait(180)  #以秒为单位
driver.find_element_by_id('com.tencent.mobileqq:id/ba3').click()  #点击+号
driver.implicitly_wait(30)  #以秒为单位
driver.find_element_by_id('com.tencent.mobileqq:string/adp').click()  #点击加好友/群
driver.implicitly_wait(60)  #以秒为单位
driver.find_element_by_id('com.tencent.mobileqq:id/bz0').click()  #点击输入框
driver.implicitly_wait(60)  #以秒为单位
driver.find_element_by_id('com.tencent.mobileqq:id/et_search_keyword').send_keys("2118162939")  #输入QQ号
driver.implicitly_wait(60)  #以秒为单位
driver.find_element_by_id('com.tencent.mobileqq:id/czn').click()  #点击找人

