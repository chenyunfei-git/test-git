from appium import webdriver


if __name__ == '__main__':
    desired_caps = {
        'platformName': 'Android',
        'deviceName': '127.0.0.1:62001',
        'platformVersion': '6.0.1',
        'appPackage': ' com.shmj.xiaoxiucai',
        'appActivity': 'com.qsmy.busniess.welcome.WelcomeActivity'
    }

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


