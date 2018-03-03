#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''登录ehall.ynu.edu.cn'''

__author__ = 'Hukuang'
__copyright__ = 'Copyright 2018, YNUOSA'

__lisense__ = 'GPL'
__version__ = '0.0.1'
__maintainer__ = 'Hukuang'
__email__ = 'thiswind@gmail.com'
__status__ = 'Development'

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.chrome.options import Options

def login_and_get_cookies():

    ## create driver
    chrome_options = Options()

    # uncomment if running in visiable mode
    chrome_options.add_argument('--headless')

    driver = webdriver.Chrome(
        chrome_options=chrome_options, 
        executable_path='/usr/local/opt/chromedriver/chromedriver')

    ## open home page
    driver.get('http://ehall.ynu.edu.cn')

    ## now in home page
    button = driver.find_element_by_id('ampHasNoLogin')
    button.click()

    # wait for loading page
    sleep(3)

    ## now in ids loglin page
    # set username and password
    username = driver.find_element_by_id('username')
    password = driver.find_element_by_id('password')
    submit = driver.find_element_by_class_name('auth_login_btn')

    username.send_keys('')  # TODO an username must be set
    password.send_keys('')  # TODO a password must be set
    submit.submit()

    # wait for loading page
    sleep(3)

    ## if there is Secondary validation
    if driver.find_element_by_class_name('kick_table'):
        continue_btn = driver.find_element_by_class_name('button_ok')
        continue_btn.click()
    else:
        pass

    # wait for loading page
    sleep(3)

    if '新建的桌面' in driver.page_source:
        cookies = driver.get_cookies()
        return cookies
    else:
        return None

cookies = login_and_get_cookies()

for cookie in cookies:
    print(cookie)