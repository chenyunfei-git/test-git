import time
from appium import webdriver

while True:
    desired_caps = {
        'platformName': 'Android',
        'deviceName': '127.0.0.1:7555',
        'platformVersion': '6.0.1',
        'appPackage': 'com.xiaoxian.cy.kantu.android.vivo',
        'appActivity': 'com.qsmy.busniess.welcome.WelcomeActivity',
        'noReset': "false"
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    time.sleep(5)


