#!/usr/bin/python3
# -*- coding:UTF-8-*-
'''
@File:
@Author: Yaochenglong
@Email: 289911401@qq.com
@Date :
@Desc: 滑动验证码
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

EMAIL = '289911401@QQ.COM'
PASSWORD = '123456789'

class CrackGeetest():
    def __init__(self):
        self.url = 'https://auth.geetest.com/login/'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser,20)
        self.email = EMAIL
        self.password = PASSWORD

    def get_geetest_button(self):
        """
        获取初始验证按钮
        :return:按钮对象
        """
        button = self.wait.until((By.CLASSNAME,'geetest_radar_tip'))
        button.click()


    def get_position(self):
        """
        获取验证码位置
        :return:验证码位置元组
        """
        img = self.wait.until(EC.presence_of_element_located(By.CLASS_NAME,'geetest_canvas_img'))
        time.sleep(2)
        location = img.location
        size = img.size
        top,bottom,left,right = location['y'],location['y']+ size['height'],location['x'],location['x'] + size['width']
        return (top,bottom,left,right)
    def get_geetest_image(self):
        pass
