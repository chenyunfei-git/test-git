from time import sleep, time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {
        'platformName': 'Android',
        'deviceName': '127.0.0.1:7555',
        'platformVersion': '6.0.1',
        'appPackage': 'com.xiaoxian.cy.kantu.android',
        'appActivity': 'com.qsmy.busniess.welcome.WelcomeActivity',
        'noReset': "True"
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)
l = getSize()
print(l)

# 屏幕向上滑动
def swipeUp():
    sleep(15)
    s = driver.get_window_size()
    x1 = s['width'] * 0.5  # x坐标
    print(x1)
    y1 = s['height'] * 0.7  # 起点y坐标
    y2 = s['height'] * 0.3  # 终点y坐标
    for i in range(1):
        driver.swipe(x1, y1, x1, y2, 500)


# 屏幕向下滑动
def swipeDown():
    l = driver.get_window_size()
    x1 = l['width'] * 0.5          # x坐标
    y1 = l['height'] * 0.25        # 起始y坐标
    y2 = l['height'] * 0.75         # 终点y坐标
    for i in range(1):
        driver.swipe(x1, y1, x1, y2, 500)


def More(driver):
    TouchAction(driver).press(x=220,y=700)\
        .move_to(x=840, y=700)\
        .move_to(x=220, y=1530)\
        .move_to(x=810, y=1440)\
        .release().perform()


if __name__ == '__main__':
    #调用向上滑动
    swipeUp()
    More(driver)







