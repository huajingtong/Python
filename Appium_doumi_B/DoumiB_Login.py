# -*- coding:utf-8 -*-
import os, time, unittest

from selenium import webdriver
from appium import webdriver

caps={}

caps['platformName'] = 'Android'
caps['platformVersion'] = '7.1.1'
caps['deviceName'] = 'e9bcac7b'
caps['appPackage'] = 'com.doumi.bclient'
caps['appActivity'] = 'com.doumi.bclient.activity.common.LaunchActivity'
#隐藏键盘
# caps['unicodeKeyboard'] = True
# caps['resetKeyboard'] = True
driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)

driver.implicitly_wait(10)
driver.find_element_by_xpath("//android.view.View[@content-desc='密码登录']").click()
# driver.find_element_by_accessibility_id('密码登录').click()
print driver.find_element_by_accessibility_id('密码登录').get_attribute('name')

print ("mima")

driver.implicitly_wait(5)
driver.find_element_by_xpath("//android.widget.EditText[@text='请输入11位常用手机号']").send_keys("17400200001")
driver.implicitly_wait(5)
driver.find_element_by_xpath("//android.widget.EditText[@text='••••••••••']").send_keys("123456")

driver.implicitly_wait(5)
driver.find_element_by_xpath("//android.widget.Button[@content-desc='登录']").click()


driver.implicitly_wait(10)

# driver.find_element_by_xpath("//android.widget.TextView[@text='直聘通']").click()
# #全部职位
# driver.implicitly_wait(2)
# driver.find_element_by_xpath("//android.widget.TextView[@text='全部职位']").click()
# #招聘中
# driver.implicitly_wait(2)
# driver.find_element_by_xpath("//android.widget.TextView[@text='招聘中']").click()
# #审核中
# driver.implicitly_wait(2)
# driver.find_element_by_xpath("//android.widget.TextView[@text='审核中']").click()
# #审核拒绝
# driver.implicitly_wait(2)
# driver.find_element_by_xpath("//android.widget.TextView[@text='审核拒绝']").click()
# #已结束
# driver.implicitly_wait(2)
# driver.find_element_by_xpath("//android.widget.TextView[@text='已结束']").click()


if __name__ == '__main__':

    pass