#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''login ehall.ynu.edu.cn'''

__author__ = 'Hukuang'
__copyright__ = 'Copyright 2018, YNUOSA'

__lisense__ = 'GPL'
__version__ = '0.0.1'
__maintainer__ = 'Hukuang, Liudonghua'
__email__ = 'thiswind@gmail.com, liudonghua123@gmail.com'
__status__ = 'Development'

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

from selenium.webdriver.chrome.options import Options

def login_and_get_cookies():

    ## create driver
    chrome_options = Options()

    # read HEADLESS environment to detect whether to use --headless argument
    if 'HEADLESS' in os.environ:
        chrome_options.add_argument('--headless')

    driver = webdriver.Chrome(chrome_options=chrome_options)

    ## open home page
    driver.get('http://ehall.ynu.edu.cn')

    # create WebDriverWait instance
    wait = WebDriverWait(driver, 10)

    ## now in home page
    button = wait.until(EC.element_to_be_clickable((By.ID, 'ampHasNoLogin')))
    button.click()

    # wait for loading page
    username = wait.until(EC.element_to_be_clickable((By.ID, 'username')))
    password = driver.find_element_by_id('password')

    # fill username with USERNAME environment value
    username.send_keys(os.environ['USERNAME'])
    # fill password with USERNAME environment value
    password.send_keys(os.environ['PASSWORD'])
    password.submit()

    ## if there is Secondary validation
    try:
        kick_table = driver.find_element_by_class_name('kick_table')
        wait.until(EC.visibility_of(kick_table))
        continue_btn = driver.find_element_by_class_name('button_ok')
        continue_btn.click()
    finally:
        if '个人中心' in driver.page_source:
            cookies = driver.get_cookies()
            return cookies
        else:
            return None

cookies = login_and_get_cookies()

for cookie in cookies:
    print(cookie)