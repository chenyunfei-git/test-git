from appium import webdriver



def appnium_start():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'  # 设备版本信息
    desired_caps['platformVersion'] = '6.0.1'  # 设备版本号
    desired_caps['deviceName'] = '127.0.0.1:7555'  # 虚拟机名称
    desired_caps['appPackage'] = 'com.shmj.xiaoxiucai'  # 包名
    desired_caps['appActivity'] = 'com.qsmy.busniess.welcome.WelcomeActivity'
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver


if __name__ == '__main__':
    appnium_start()

