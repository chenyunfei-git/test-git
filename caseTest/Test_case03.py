from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {
        'platformName': 'Android',
        'deviceName': '127.0.0.1:7555',
        'platformVersion': '6.0.1',
        'appPackage': 'com.android.settings',
        'appActivity': '.Settings',
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


def More(driver):
    TouchAction(driver).press(x=220,y=700)\
        .move_to(x=840, y=700)\
        .move_to(x=220, y=1530)\
        .move_to(x=810, y=1440)\
        .release().perform()

def click():
    driver.find_element_by_xpath("//*[@text='安全']").click()  # 点击安全文字
    sleep(10)
    driver.find_element_by_xpath("//*[@text='屏幕锁定方式']").click()
    sleep(10)
    driver.find_element_by_xpath("//*[@text='图案']").click()

def lock_screen():
    a = driver.find_element_by_id('com.android.settings:id/lockPattern').click()
    # 元素大小
    size = a.size
    # 起始坐标点
    start_point = a.location
    # 步长
    step = size["height"] / 6
    '''第一个'''
    point1_x = start_point["x"] + step
    point1_y = start_point["y"] + step
    '''第二个'''
    point2_x = point1_x + step * 4
    point2_y = point1_y
    '''第三个'''
    point3_x = point2_x - step * 4
    point3_y = point2_y + step * 4
    '''第四个'''
    point4_x = point3_x + step * 4
    point4_y = point3_y

    lock = TouchAction(driver)
    lock.press(x=point1_x, y=point1_y).wait(200). \
        move_to(x=point2_x, y=point2_y).wait(200). \
        move_to(x=point3_x, y=point3_y).wait(200). \
        move_to(x=point4_x, y=point4_y).wait(200).release().perform()
if __name__ == '__main__':
    #调用向上滑动
    swipeUp()
    More(driver)
    click()
    sleep(15)
    lock_screen()


