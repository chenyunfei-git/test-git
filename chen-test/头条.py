#!urs/bin/python
#!_*_ coding:UTF-8 _*_

from appium import webdriver


if __name__ == '__main__':
    desired_caps = {
        'platformName': 'Android',
        'deviceName': '127.0.0.1:62001',
        'platformVersion': '5.1.1',
        'appPackage': 'com.songheng.eastnews',
        'appActivity': 'com.oa.eastfirst.activity.MainActivity'
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


driver.implicitly_wait(60)  #以秒为单位
driver.find_element_by_id('com.songheng.eastnews:id/rb_bottom_mine').click()  #点击我的
driver.implicitly_wait(30)  #以秒为单
#driver.find_element_by_id('com.songheng.eastnews:id/iv_usr_image').click()  #点击头像
#driver.implicitly_wait(30)  #以秒为单
#driver.find_element_by_id('com.songheng.eastnews:id/btn_qq').click()  #点击QQ图标
#driver.implicitly_wait(120)  #以秒为单位
###跳转到QQ进行授权
#driver.find_element_by_id('com.tencent.mobileqq:id/btn_login').click()  #点击登录
#driver.implicitly_wait(60)  #以秒为单位
#driver.find_element_by_class_name("android.widget.TextView").click()
#driver.implicitly_wait(30)  #以秒为单位
#driver.find_element_by_class_name('android.widget.EditText').send_keys("1292394137")  #输入QQ号
##driver.find_element_by_id('com.tencent.mobileqq:id/password').send_keys("SJN1020..")  #输入密码
#driver.find_element_by_id('com.tencent.mobileqq:id/login').click()  #点击登录
#driver.implicitly_wait(60)  #以秒为单位
#driver.find_element_by_id('com.tencent.mobileqq:id/fds').click()  #点击QQ授权
driver.implicitly_wait(60)  #以秒为单位
driver.find_element_by_id('com.songheng.eastnews:id/rb_bottom_search').click()  #点击搜索
driver.implicitly_wait(60)  #以秒为单位
driver.find_element_by_id('com.songheng.eastnews:id/edit_search').send_keys("特朗普")  #点击输入框并输入搜索内容
driver.implicitly_wait(60)  #以秒为单位
driver.find_element_by_id('com.songheng.eastnews:id/btn_search').click()  #点击搜索按钮