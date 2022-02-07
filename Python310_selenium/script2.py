#!/usr/bin/env python3
import sys
import os
import time
import json
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException        
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from var import x
from var import y
from var import keyword
from var import click_text_1
from var import click_text_2
from var import click_text_3
from var import click_text_4
from var import click_text_5
from var import click_text_6
from var import click_text_7
from var import click_text_8
from var import click_text_9
from var import click_text_10
from var import click_text_11
from var import click_text_12
from var import click_text_13
from var import click_text_14
from var import click_text_15
from var import click_text_16
from var import click_text_17
from var import click_text_18
from var import click_text_19
from var import click_text_20
from var import click_text_21
from var import click_text_22
from var import click_text_23
from var import click_text_24
from var import click_text_25
from var import click_text_26
from var import click_text_27

while x<=y :
    print("start")
    username = "geonode_GJkxCcMRU0-autoReplace-True"
    password = "99879a56-fed0-467a-af48-df19046284ae"
    GEONODE_DNS = "premium-residential.geonode.com:9003"
    proxy = "premium-residential.geonode.com:9003" # IP:PORT or HOST:PORT

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=http://%s' % proxy)





    # no picture
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    

    browser = webdriver.Chrome(chrome_options=chrome_options)


    try:

        browser.get("https://www.google.com/") 
        time.sleep(1)

        search = browser.find_element_by_name('q')
        search.send_keys(keyword)
        time.sleep(1)
        search.send_keys(Keys.RETURN)
        new_open = 0

        webs = browser.find_elements_by_partial_link_text(click_text_1)
        if webs:
                for web in webs:
                        web.send_keys(Keys.CONTROL,Keys.ENTER)
                        new_open = new_open + 1
                        time.sleep(0.5)

        webs = browser.find_elements_by_partial_link_text(click_text_2)
        if webs:
                for web in webs:
                        web.send_keys(Keys.CONTROL,Keys.ENTER)
                        new_open = new_open + 1
                        time.sleep(0.5)

        webs = browser.find_elements_by_partial_link_text(click_text_3)
        if webs:
                for web in webs:
                        web.send_keys(Keys.CONTROL,Keys.ENTER)
                        new_open = new_open + 1
                        time.sleep(0.5)

        webs = browser.find_elements_by_partial_link_text(click_text_4)
        if webs:
                for web in webs:
                        web.send_keys(Keys.CONTROL,Keys.ENTER)
                        new_open = new_open + 1
                        time.sleep(0.5)

        webs = browser.find_elements_by_partial_link_text(click_text_5)
        if webs:
                for web in webs:
                        web.send_keys(Keys.CONTROL,Keys.ENTER)
                        new_open = new_open + 1
                        time.sleep(0.5)


        webs = browser.find_elements_by_partial_link_text(click_text_6)
        if webs:
                for web in webs:
                        web.send_keys(Keys.CONTROL,Keys.ENTER)
                        new_open = new_open + 1
                        time.sleep(0.5)


        webs = browser.find_elements_by_partial_link_text(click_text_7)
        if webs:
                for web in webs:
                        web.send_keys(Keys.CONTROL,Keys.ENTER)
                        new_open = new_open + 1
                        time.sleep(0.5)

        webs = browser.find_elements_by_partial_link_text(click_text_8)
        if webs:
                for web in webs:
                        web.send_keys(Keys.CONTROL,Keys.ENTER)
                        new_open = new_open + 1
                        time.sleep(0.5)

        webs = browser.find_elements_by_partial_link_text(click_text_9)
        if webs:
                for web in webs:
                        web.send_keys(Keys.CONTROL,Keys.ENTER)
                        new_open = new_open + 1
                        time.sleep(0.5)

        webs = browser.find_elements_by_partial_link_text(click_text_10)
        if webs:
                for web in webs:
                        web.send_keys(Keys.CONTROL,Keys.ENTER)
                        new_open = new_open + 1
                        time.sleep(0.5)

        webs = browser.find_elements_by_partial_link_text(click_text_11)
        if webs:
                for web in webs:
                        web.send_keys(Keys.CONTROL,Keys.ENTER)
                        new_open = new_open + 1
                        time.sleep(0.5)

        webs = browser.find_elements_by_partial_link_text(click_text_12)
        if webs:
                for web in webs:
                        web.send_keys(Keys.CONTROL,Keys.ENTER)
                        new_open = new_open + 1
                        time.sleep(0.5)

        webs = browser.find_elements_by_partial_link_text(click_text_13)
        if webs:
                for web in webs:
                        web.send_keys(Keys.CONTROL,Keys.ENTER)
                        new_open = new_open + 1
                        time.sleep(0.5)

        webs = browser.find_elements_by_partial_link_text(click_text_14)
        if webs:
                for web in webs:
                        web.send_keys(Keys.CONTROL,Keys.ENTER)
                        new_open = new_open + 1
                        time.sleep(0.5)

        webs = browser.find_elements_by_partial_link_text(click_text_15)
        if webs:
                for web in webs:
                        web.send_keys(Keys.CONTROL,Keys.ENTER)
                        new_open = new_open + 1
                        time.sleep(0.5)

        webs = browser.find_elements_by_partial_link_text(click_text_16)
        if webs:
                for web in webs:
                        web.send_keys(Keys.CONTROL,Keys.ENTER)
                        new_open = new_open + 1
                        time.sleep(0.5)

        webs = browser.find_elements_by_partial_link_text(click_text_17)
        if webs:
                for web in webs:
                        web.send_keys(Keys.CONTROL,Keys.ENTER)
                        new_open = new_open + 1
                        time.sleep(0.5)

        webs = browser.find_elements_by_partial_link_text(click_text_18)
        if webs:
                for web in webs:
                        web.send_keys(Keys.CONTROL,Keys.ENTER)
                        new_open = new_open + 1
                        time.sleep(0.5)

        webs = browser.find_elements_by_partial_link_text(click_text_19)
        if webs:
                for web in webs:
                        web.send_keys(Keys.CONTROL,Keys.ENTER)
                        new_open = new_open + 1
                        time.sleep(0.5)

        webs = browser.find_elements_by_partial_link_text(click_text_20)
        if webs:
                for web in webs:
                        web.send_keys(Keys.CONTROL,Keys.ENTER)
                        new_open = new_open + 1
                        time.sleep(0.5)

        webs = browser.find_elements_by_partial_link_text(click_text_21)
        if webs:
                for web in webs:
                        web.send_keys(Keys.CONTROL,Keys.ENTER)
                        new_open = new_open + 1
                        time.sleep(0.5)

        webs = browser.find_elements_by_partial_link_text(click_text_22)
        if webs:
                for web in webs:
                        web.send_keys(Keys.CONTROL,Keys.ENTER)
                        new_open = new_open + 1
                        time.sleep(0.5)

        webs = browser.find_elements_by_partial_link_text(click_text_23)
        if webs:
                for web in webs:
                        web.send_keys(Keys.CONTROL,Keys.ENTER)
                        new_open = new_open + 1
                        time.sleep(0.5)

        webs = browser.find_elements_by_partial_link_text(click_text_24)
        if webs:
                for web in webs:
                        web.send_keys(Keys.CONTROL,Keys.ENTER)
                        new_open = new_open + 1
                        time.sleep(0.5)

        webs = browser.find_elements_by_partial_link_text(click_text_25)
        if webs:
                for web in webs:
                        web.send_keys(Keys.CONTROL,Keys.ENTER)
                        new_open = new_open + 1
                        time.sleep(0.5)

        webs = browser.find_elements_by_partial_link_text(click_text_26)
        if webs:
                for web in webs:
                        web.send_keys(Keys.CONTROL,Keys.ENTER)
                        new_open = new_open + 1
                        time.sleep(0.5)

        webs = browser.find_elements_by_partial_link_text(click_text_27)
        if webs:
                for web in webs:
                        web.send_keys(Keys.CONTROL,Keys.ENTER)
                        new_open = new_open + 1
                        time.sleep(0.5)

        windows = browser.window_handles
        browser.switch_to.window(windows[-1])

        WebDriverWait(browser,1).until(EC.title_contains(u"YouTube"))
        time.sleep(new_open * 0.5)

        print("ok")

    except:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


    time.sleep(2)
    x=x+1
    browser.quit()